function replaceAll(find, replace, str) {
    while (str.indexOf(find) > -1) {
        str = str.replace(find, replace);
    }
    return str;
}

if (typeof String.prototype.startsWith != "function") {
    String.prototype.startsWith = function (prefix) {
        return this.slice(0, prefix.length) == prefix;
    }
}

if (typeof String.prototype.endsWith !== "function") {
    String.prototype.endsWith = function (suffix) {
        return this.indexOf(suffix, this.length - suffix.length) !== -1;
    };
}

function redirectUrls(node, targetPath) {
    var i;

    // hack a href
    var as = node.getElementsByTagName("a");
    for (i = 0; i < as.length; i++) {
        var a = as[i];
        var href = a.getAttribute("href");
        if (href.endsWith("md") || href.indexOf(".md#") > -1) {
            var match = /^([\w-]+).md(#[\w-]+)?$/.exec(href);
            if (match && match.length >= 2) {
                var newPage = match[1];
                // TODO: do something with the anchor :-)
                //var anchor = match[2]; // could be undefined
                var newHref = window.location.href.replace(/page=([\w-]+)/, "page=" + newPage);
                a.setAttribute("href", newHref);
            }
        }
    }

    // hack images src
    var imgs = node.getElementsByTagName("img");
    for (i = 0; i < imgs.length; i++) {
        var img = imgs[i];
        var src = img.getAttribute("src");
        var match = /^(\w*)\/([\w-\.]*)$/.exec(src);
        if (match && match.length == 3) {
            console.log('check:');
            console.log('  targetPath: ' + targetPath);
            console.log('  newPath: ' + targetPath + match[1] + "/" + match[2]);
            img.setAttribute("src", targetPath + match[1] + "/" + match[2]);
        }
    }
}

function populateViewDiv(mdContent) {
    console.log("Raw MD content:\n\n");
    console.log(mdContent);

    // markdown to html
    var converter = new showdown.Converter({tables: "True", extensions: ['wbFigure', 'wbVariables']});
    var html = converter.makeHtml(mdContent);

    var div = document.createElement("div");
    div.innerHTML = html;

    redirectUrls(div, this.setup.targetPath);

    document.getElementById("view").appendChild(div);

    $('pre code').each(function(i, block) {
        hljs.highlightBlock(block);
    });
}

function receiveTocContent(tocContent) {
    // convert the orderedlist to an unordered one: easier to deal with in jQuery menu
    tocContent = tocContent.replace(/\n( *)\d+\. /g, "\n$1- ");

    console.log("Toc content:\n\n");
    console.log(tocContent);

    var toc = null;


    var converter = new showdown.Converter();
    var html = converter.makeHtml(tocContent);
    var div = document.createElement("div");
    div.innerHTML = html;

    var i;
    for (i = 0; i < div.childNodes.length; i++) {
        var child = div.childNodes[i];
        if (child && child.tagName && child.tagName.length > 0 && child.tagName.toLowerCase() == "ul") {
            toc = child;
            break;
        }
    }

    // find the selected item
    var as = toc.getElementsByTagName("a");
    var selected = null;
    for (i = 0; i < as.length; i++) {
        var a = as[i];
        var href = a.getAttribute("href");
        if (href.indexOf(this.setup.page) > -1) {
            selected = a.parentNode;
            selected.setAttribute("class", "selected");
            if (selected.parentNode.parentNode.tagName.toLowerCase() == "li") {
                selected.parentNode.parentNode.setAttribute("class", "selected");
            }
            break;
        }
    }

    redirectUrls(toc, this.setup.targetPath);

    if (toc) {
        populateMenu(toc);
        populateNavigation(toc, selected);
    } else {
        console.error("Cannot extract TOC.");
    }
}

function populateNavigation(toc, selected) {
    if (!selected) {
        return;
    }

    var next = document.getElementById("next");
    if (next) {
        var nextElement = null;

        var nextLiSibling = selected.nextSibling;
        while (nextLiSibling) {
            if (nextLiSibling.tagName && nextLiSibling.tagName.toLowerCase() == "li") {
                break;
            }
            nextLiSibling = nextLiSibling.nextSibling;
        }
        if (nextLiSibling) {
            var as = nextLiSibling.getElementsByTagName("a");
            if (as.length > 0)
              nextElement = as[0];
        }

        if (nextElement) {
            next.setAttribute("href", nextElement.getAttribute("href"));
        } else {
            next.setAttribute("class", "disabled");
        }
    }

    var previous = document.getElementById("previous");
    if (previous) {
        var previousElement = null;

        var previousLiSibling = selected.previousSibling;
        while (previousLiSibling) {
            if (previousLiSibling.tagName && previousLiSibling.tagName.toLowerCase() == "li") {
                break;
            }
            previousLiSibling = previousLiSibling.previousSibling;
        }
        if (previousLiSibling) {
            var as = previousLiSibling.getElementsByTagName("a");
            if (as.length > 0)
              previousElement = as[0];
        }

        if (previousElement) {
            previous.setAttribute("href", previousElement.getAttribute("href"));
        } else {
            previous.setAttribute("class", "disabled");
        }
    }

    var up = document.getElementById("up");
    if (up) {
        var upElement = null;
        var parentLi = null;
        if (selected.parentNode.parentNode.tagName.toLowerCase() == "li") {
            parentLi = selected.parentNode.parentNode;
        }
        if (parentLi) {
            var as = parentLi.getElementsByTagName("a");
            if (as.length > 0)
              upElement = as[0];
        }

        if (upElement) {
            up.setAttribute("href", upElement.getAttribute("href"));
        } else {
            up.setAttribute("class", "disabled");
        }
    }
}

function populateMenu(toc) {
    var menu = document.getElementById("menu");
    menu.appendChild(toc);
    $(toc).menu();
}

document.addEventListener("DOMContentLoaded", function() {
    var book = getGETQueryValue("book", "guide");
    var page = getGETQueryValue("page", "guide.md");
    var branch = getGETQueryValue("branch", "feature-webots-doc-importer");
    var url = getGETQueryValue("url", "https://raw.githubusercontent.com/omichel/webots-doc/")
    var targetPath = url;
    if (url.startsWith("http")) {
        targetPath += branch + "/";
    }
    targetPath += book + "/";

    var targetUrl = targetPath + page;
    console.log("Target Url: " + targetUrl);

    // get the md file
    $.ajax({
        type: "GET",
        url: targetUrl,
        dataType: "text",
        setup : {
            'targetPath': targetPath
        },
        success: populateViewDiv,
        error: function(XMLHttpRequest, textStatus, errorThrown) { 
            console.log("Status: " + textStatus);
            console.log("Error: " + errorThrown); 
        }
    });

    var tocUrl = targetPath + "toc.md";
    console.log("TOC Url: " + tocUrl);

    // get the toc file
    $.ajax({
        type: "GET",
        url: tocUrl,
        dataType: "text",
        success: receiveTocContent,
        setup: {
            'targetPath': targetPath,
            'page': page
        },
        error: function(XMLHttpRequest, textStatus, errorThrown) { 
            console.log("Status: " + textStatus);
            console.log("Error: " + errorThrown); 
        }
    });
});
