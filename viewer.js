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

function redirectUrls(node) {
    var i;

    // hack a href
    var as = node.getElementsByTagName("a");
    for (i = 0; i < as.length; i++) {
        var a = as[i];
        var href = a.getAttribute("href");
        if (href.endsWith("md") && (href.startsWith("guide") || href.startsWith("reference"))) {
            var match = /^([\w-]+)\/([\w-]+).md$/.exec(href);
            if (match && match.length == 3) {
                var newBook = match[1];
                var newPage = match[2];
                var newHref = window.location.href.replace(/book=([\w-]+)/, "book=" + newBook).replace(/page=([\w-]+)/, "page=" + newPage);
                a.setAttribute("href", newHref);
            }
        }
    }

    // hack images src
    var imgs = node.getElementsByTagName("img");
    for (i = 0; i < imgs.length; i++) {
        var img = imgs[i];
        var src = img.getAttribute("src");
        var match = /^png\/([\w-\.]*)$/.exec(src);
        if (match && match.length == 2) {
            img.setAttribute("src", targetPath + "png/" + match[1]);
        }
    }
}

function populateViewDiv(mdContent) {
    console.log("Raw MD content:\n\n");
    console.log(mdContent);

    // markdown to html
    var converter = new showdown.Converter({tables: "True"});
    var html = converter.makeHtml(mdContent);

    var div = document.createElement("div");
    div.innerHTML = html;

    redirectUrls(div);

    var view = document.getElementById("view");
    for (i = 0; i < div.childNodes.length; i++) {
        child = div.childNodes[i];
        view.appendChild(child);
    }
}

function receiveTocContent(tocContent) {
    // convert the orderedlist to an unordered one: easier to deal with in jQuery menu
    tocContent = tocContent.replace(/\n( *)\d+\. /g, '\n$1- ');

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
    var page = getGETQueryValue("page", "guide.md"); // TODO: pass this as argument
    for (i = 0; i < as.length; i++) {
        var a = as[i];
        var href = a.getAttribute("href");
        if (href.indexOf(page) > -1) {
            a.parentNode.setAttribute("class", "selected");
            if (a.parentNode.parentNode.parentNode.tagName.toLowerCase() == "li") {
                a.parentNode.parentNode.parentNode.setAttribute("class", "selected");
            }
            break;
        } else {
          a.parentNode.setAttribute("class", "unselected");
        }
    }

    redirectUrls(toc);

    if (toc) {
        populateNavigation(toc);
        populateMenu(toc);
    } else {
        console.error("Cannot extract TOC.");
    }
}

function populateNavigation(toc) {
    var navigation = document.getElementById("navigation");
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
        error: function(XMLHttpRequest, textStatus, errorThrown) { 
            console.log("Status: " + textStatus);
            console.log("Error: " + errorThrown); 
        }
    });
});
