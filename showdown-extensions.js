showdown.extension("wbFigure", function() {
    return [
        { // figure with legend to HTML
            type: "lang",
            filter: function(text, converter, options) {
                text = text.replace(/%figure\s+"([^]+?)"([^]+?)%end/gi, function(match, title, content) {
                    var foo = converter.makeHtml(content);
                    return "<figure>" + foo + "<figcaption>" + title + "</figcaption></figure>";
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
            regex: /<figure><p><img([^]+?)<\/p>/gi,
            replace: function (match, content) {
                return "<figure><img" + content;
            }
        }
    ];
});

showdown.extension("wbVariables", function() {
    // static variables to maintain
    // TODO: could be computed
    var vars = {
      webots : {
        version : {
          major : 8,
          minor : 4,
          bugfix : 0
        }
      },
      date : {
        year : 2016
      }
    };

    return [
        { // replace '{{ var }}' by the vars dictionnary above
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
                        throw "Undefined value";
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
