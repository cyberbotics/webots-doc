// function allowing to convert some text to its slug
function wbSlugify(obj) {
    var text = '';
    if (typeof obj === 'string') {
        text = obj;
    } else if (obj instanceof HTMLElement) {
        text = obj.textContent;
    } else {
        console.error("wbSlugify: Unsupported input");
    }
    return text.
        trim().
        toLowerCase().
        replace(/[\s\.]/g, '-').
        replace(/[-]+/g, '-').
        replace(/^-*/, '').
        replace(/-*$/, '').
        replace('+', 'p').
        replace(/[^\w-]+/g, '');
}

// This extension is a template-like mechanism, allowing
// to replace variables by a static content.
// For example, the markdown string "{{ date.year }}" is replaced by "2016"
showdown.extension("wbVariables", function() {
    // static variables to maintain
    // TODO: could be computed
    var vars = {
      webots : {
        version : {
          major : "R2018a",
          // full is equal to major for the first major version
          // and contains the revision number for subsequent versions
          full : "R2018a",
          package : "R2018a"
        }
      },
      date : {
        year : 2018
      }
    };
    // compute debian package version format by removing initial 'R'
    vars.webots.version.debian_package = vars.webots.version.package.substring(1);

    return [
        { // replace '{{ var }}' by the vars dictionary above
            type: "html",
            //regex: /\^\s*\(([^]+?)\)/gi,
            regex: /\{\{([^]+?)\}\}/gi,
            replace: function (match, content) {
                var key = content.replace(/\s/g, ""); // remove spaces
                try {
                    // cf: http://stackoverflow.com/questions/6393943/convert-javascript-string-in-dot-notation-into-an-object-reference
                    function index(obj, i) { return obj[i]; }
                    var value = key.split('.').reduce(index, vars);
                    if (value === undefined) {
                        console.error("wbVariables: Undefined value");
                        return "";
                    }
                    return value;
                } catch (err) {
                    console.log("Variable '" + key + "' not found: " + err);
                    return key;
                }
            }
        }
    ];
});

// This extension is dealing with some figure content (data with legend having an anchor)
// For example, the markdown string `%figure "legend"\ncontent\n%end` is replaced by
// "<figure>content<figcaption>legend</figcaption></figure>"
showdown.extension("wbFigure", function() {
    return [
        { // figure with legend to HTML
            type: "lang",
            filter: function(text, converter, options) {
                text = text.replace(/%figure\s+"([^]+?)"([^]+?)%end/gi, function(match, title, content) {
                    var foo = converter.makeHtml(content);
                    return "<figure name=\"" + wbSlugify(title) + "\">" + foo + "<figcaption>" + title + "</figcaption></figure>";
                });
                return text;
            }
        },
        { // figure without legend to HTML
            type: "lang",
            filter: function(text, converter, options) {
                text = text.replace(/%figure\s+([^"][^]+?)%end/gi, function(match, content) {
                    console.log("content " + content);
                    var foo = converter.makeHtml(content);
                    return "<figure>" + foo + "</figure>";
                });
                return text;
            }
        },
        { // remove <p> tags inside the <figure> tag
            type: "html",
            regex: /<figure([^>]*)><p><img([^]+?)<\/p>/gi,
            replace: function (match, arguments, content) {
                return "<figure" + arguments + "><img" + content;
            }
        }
    ];
});


// This extension is dealing with some API content
showdown.extension("wbAPI", function() {
    return [
        { // api tag to HTML
            type: "lang",
            filter: function(text, converter, options) {
                text = text.replace(/%api\s+"([^]+?)"([^]+?)%end/gi, function(match, anchor, content) {
                    var foo = converter.makeHtml(content);
                    return "<div name=\"" + anchor + "\" class=\"api\">" + foo + "</div>";
                });
                return text;
            }
        },
        { // "\*\*wb.*\*\*" to anchor
            type: "lang",
            filter: function(text, converter, options) {
                text = text.replace(/\*\*(wb\\_[^\*]+?)\*\*/gi, function(match, content) {
                    var protectedContent = content.replace(/\\_/g, "_");
                    return "<strong name=\"" + protectedContent + "\">" + content + "</strong>";
                });
                return text;
            }
        }
    ];
});


// This extension is defining an id with a custom slug on the headers and on the figures
// Note: showdown is already generating the ids with a slug function, but only for
// headers, and without hyphens.
showdown.extension("wbAnchors", function() {
    return [
        {
            type: "html",
            regex: /<h(\d) id=\"([^]+?)\">([^]+?)<\/h(\d)>/gi,
            replace: function (match, level1, showdownId, content, level2) {
                if (level1 !== level2) {
                    console.error("wbAnchors: level mismatch");
                    return "";
                }

                var tmpDiv = document.createElement("DIV");
                tmpDiv.innerHTML = content;
                var rawContent = tmpDiv.textContent || tmpDiv.innerText || "";

                return "<h" + level1 + " name=\"" + wbSlugify(rawContent) + "\">" + content + "</h" + level1 + ">";
            }
        }
    ];
});

 // This extension allows to define an illustrated section, simply if a paragraph is starting with an image:
 // e.g:
 //     `![battery.png](images/battery.png) In this example, etc.`
showdown.extension("wbIllustratedSection", function() {
    return [
        { // TODO: comment
            type: "lang",
            filter: function(text, converter, options) {
                text = text.replace(/\n(!\[[^\]]*\]\s*\([^\)]*\)) ([^\n]*)/gi, function(match, image, content) {
                    var htmlImage = converter.makeHtml(image);
                    if (htmlImage.startsWith('<p>') && htmlImage.endsWith('</p>'))  // Remove useless "p" encapsulation.
                      htmlImage = htmlImage.substr(3, htmlImage.length - 7);
                    var htmlContent = converter.makeHtml(content);
                    return '<section class="illustrated-section">' + htmlImage + htmlContent + '</section>';
                });
                return text;
            }
        }
    ];
});
