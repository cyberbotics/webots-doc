function replaceAll(find, replace, str) {
    while (str.indexOf(find) > -1) {
        str = str.replace(find, replace);
    }
    return str;
}

if (typeof String.prototype.startsWith != "function") {
    String.prototype.startsWith = function (prefix) {
        return this.slice(0, prefix.length) == prefix;
    };
}

if (typeof String.prototype.endsWith !== "function") {
    String.prototype.endsWith = function (suffix) {
        return this.indexOf(suffix, this.length - suffix.length) !== -1;
    };
}

function redirectUrls(node, targetPath) {
    var i;

    // redirect a's href
    var as = node.getElementsByTagName("a");
    for (i = 0; i < as.length; i++) {
        var a = as[i];
        var href = a.getAttribute("href");
        if (! href) {
            continue;
        }
        if (href.startsWith("www") || href.startsWith("http")) {
            // open external links in a new window
            a.setAttribute("target", "_blank");
        } else if (href.endsWith("md") || href.indexOf(".md#") > -1) {
            var match = /^([\w-]+).md(#[\w-]+)?$/.exec(href);
            if (match && match.length >= 2) {
                var newPage = match[1];
                var anchor = match[2]; // could be undefined
                var anchorString = (anchor && anchor.length > 0) ? anchor : "";
                var currentUrl = window.location.href;
                var newUrl = currentUrl;
                if (currentUrl.indexOf("page=") > -1) {
                    newUrl = currentUrl.replace(/page=([\w-]+)\.md(#[\w-]+)?/, "page=" + newPage + ".md" + anchorString);
                } else {
                    newUrl = currentUrl + "&page=" + newPage + ".md" + anchorString;
                }
                a.setAttribute("href", newUrl);
            }
        }
    }

    // redirect img's src
    var imgs = node.getElementsByTagName("img");
    for (i = 0; i < imgs.length; i++) {
        var img = imgs[i];
        var src = img.getAttribute("src");
        var match = /^(\w*)\/([\w-\.]*)$/.exec(src);
        if (match && match.length == 3) {
            img.setAttribute("src", targetPath + match[1] + "/" + match[2]);
        }
    }
}

function applyAnchor() {
    var currentUrl = window.location.href;
    var match = /#([\w-]+)/.exec(currentUrl);
    if (match && match.length == 2) {
        var anchorId = match[1];
        console.log("anchorId: " + anchorId);
        var anchors = document.getElementsByName(anchorId);
        if (anchors.length > 0) {
            anchors[0].scrollIntoView(true);
        }
    }
}

function applyToTitle(mdContent) {
    var hashtagIndex = mdContent.indexOf("#");
    if (hashtagIndex >= 0) {
        while (hashtagIndex + 1 < mdContent.length && mdContent[hashtagIndex + 1] == "#") {
            hashtagIndex += 1;
        }
        var hashtagCarriageReturn = mdContent.indexOf("\n", hashtagIndex);
        if (hashtagCarriageReturn >= 0) {
            var title = mdContent.substring(hashtagIndex + 1, hashtagCarriageReturn).trim();
            document.title = "Webots documentation: " + title;
        }
    }
}

function populateViewDiv(mdContent) {
    console.log("Raw MD content:\n\n");
    console.log(mdContent);

    applyToTitle(mdContent);

    // markdown to html
    var converter = new showdown.Converter({tables: "True", extensions: ["wbVariables", "wbAPI", "wbFigure", "wbAnchors"]});
    var html = converter.makeHtml(mdContent);

    // console.log("HTML content: \n\n")
    // console.log(html);

    var div = document.createElement("div");
    div.innerHTML = html;

    redirectUrls(div, this.setup.targetPath);

    var view = document.getElementById("view");
    view.appendChild(div);

    applyAnchor();
    applyAnchorIcons(view);
    highlightCode(view);
}

function highlightCode(view) {
    var pres = view.getElementsByTagName("pre"); 
    for (var i = 0; i < pres.length; i++) {
        var pre = pres[i];
        var codes = pre.getElementsByTagName("code"); 
        for (var j = 0; j < codes.length; j++) {
            var code = codes[j];
            hljs.highlightBlock(code);
        }
    }
}

function applyAnchorIcons(view) {
    var elements = [];
    var tags = ["figcaption", "h1", "h2", "h3", "h4", "h5", "h6"];
    for (var i = 0; i < tags.length; i++) {
        var array = Array.prototype.slice.call(view.getElementsByTagName(tags[i]));
        elements = elements.concat(array);
    }
    for (var i = 0; i < elements.length; i++) {
        var el = elements[i];
        var icon, id;
        var name = null;
        if (el.parentNode && el.tagName.toLowerCase() == "figcaption" && el.parentNode.tagName.toLowerCase() == "figure") {
            name = el.parentNode.getAttribute("name");
        } else {
            name = el.getAttribute("name");
        }
        if (name) {
            el.setAttribute("class", "anchor-header");
            var span = document.createElement("span");
            span.setAttribute("class", "anchor-link-image");
            var a = document.createElement("a");
            a.setAttribute("href", "#" + name);
            a.setAttribute("class", "anchor-link");
            a.appendChild(span);
            el.insertBefore(a, el.firstChild);
        }
    }
}

function receiveMenuContent(menuContent) {
    // console.log("Menu content:\n\n");
    // console.log(menuContent);

    var menu = null;

    var converter = new showdown.Converter();
    var html = converter.makeHtml(menuContent);
    var div = document.createElement("div");
    div.innerHTML = html;

    var i;
    for (i = 0; i < div.childNodes.length; i++) {
        var child = div.childNodes[i];
        if (child && child.tagName && child.tagName.length > 0 && child.tagName.toLowerCase() == "ul") {
            menu = child;
            break;
        }
    }

    // find the selected item
    var as = menu.getElementsByTagName("a");
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

    redirectUrls(menu, this.setup.targetPath);

    if (menu) {
        populateMenu(menu);
        populateNavigation(menu, selected);
    } else {
        console.error("Cannot extract Menu.");
    }
}

function populateNavigation(menu, selected) {
    var next = document.getElementById("next");
    var previous = document.getElementById("previous");
    var up = document.getElementById("up");

    if (!selected) {
        next.setAttribute("class", "disabled");
        previous.setAttribute("class", "disabled");
        up.setAttribute("class", "disabled");
        return;
    }

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
            if (as.length > 0) {
                nextElement = as[0];
            }
        }

        if (nextElement) {
            next.setAttribute("href", nextElement.getAttribute("href"));
        } else {
            next.setAttribute("class", "disabled");
        }
    }

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
            if (as.length > 0) {
                previousElement = as[0];
            }
        }

        if (previousElement) {
            previous.setAttribute("href", previousElement.getAttribute("href"));
        } else {
            previous.setAttribute("class", "disabled");
        }
    }

    if (up) {
        var upElement = null;
        var parentLi = null;
        if (selected.parentNode.parentNode.tagName.toLowerCase() == "li") {
            parentLi = selected.parentNode.parentNode;
        }
        if (parentLi) {
            var as = parentLi.getElementsByTagName("a");
            if (as.length > 0) {
                upElement = as[0];
            }
        }

        if (upElement) {
            up.setAttribute("href", upElement.getAttribute("href"));
        } else {
            up.setAttribute("class", "disabled");
        }
    }
}

function populateMenu(menu) {
    var menuDiv = document.getElementById("menu");
    menuDiv.appendChild(menu);
    $(menu).menu();
}

function getMDFile(target, setup) {
    console.log("Get MD file: " + target);
    $.ajax({
        type: "GET",
        url: target,
        dataType: "text",
        setup : setup,
        success: populateViewDiv,
        error: function(XMLHttpRequest, textStatus, errorThrown) { 
            console.log("Status: " + textStatus);
            console.log("Error: " + errorThrown);
            var mainPage = setup.targetPath + setup.book + ".md";
            // get the main page instead
            if (target != mainPage) {
                getMDFile(mainPage, setup);
            }
        }
    });
}

function getMenuFile(target, setup) {
    console.log("Get menu file: " + target);
    $.ajax({
        type: "GET",
        url: target,
        dataType: "text",
        success: receiveMenuContent,
        setup: setup,
        error: function(XMLHttpRequest, textStatus, errorThrown) {
            console.log("Status: " + textStatus);
            console.log("Error: " + errorThrown);
        }
    });
}

document.addEventListener("DOMContentLoaded", function() {
    var book = getGETQueryValue("book", "guide");
    var page = getGETQueryValue("page", "guide.md");
    var branch = getGETQueryValue("branch", "feature-webots-doc-importer");
    var url = getGETQueryValue("url", "https://raw.githubusercontent.com/omichel/webots-doc/");

    var targetPath = url;
    if (url.startsWith("http")) {
        targetPath += branch + "/";
    }
    targetPath += book + "/";

    var targetUrl = targetPath + page;
    getMDFile(targetUrl, { "targetPath": targetPath, "book": book });

    var menuUrl = targetPath + "menu.md";
    getMenuFile(menuUrl, {"targetPath": targetPath, "page": page});
});
