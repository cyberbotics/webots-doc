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

function decomposePage(page) {
    var match = /([\w-]+).md(#[\w-]+)?$/.exec(page);
    if (match && match.length >= 2) {
        var mdFile = match[1] + ".md";
        var anchor = match[2] ? match[2].substring(1) : "";
        return [mdFile, anchor];
    }
    return ["", ""];
}

function computeTargetPath() {
    var targetPath = window.setup.url;
    if (targetPath.startsWith("http")) {
        targetPath += window.setup.branch + "/";
    }
    targetPath += window.setup.book + "/";
    return targetPath;
}

function redirectUrls(node) {
    // redirect a's href
    var as = node.getElementsByTagName("a");
    var targetPath = computeTargetPath();
    for (var i = 0; i < as.length; i++) {
        var a = as[i];
        var href = a.getAttribute("href");
        if (! href) {
            continue;
        }
        if (href.startsWith("http")) {
            // open external links in a new window
            a.setAttribute("target", "_blank");
        } else if (href.endsWith("md") || href.indexOf(".md#") > -1) {
            addOnTheFlyEvent(a);
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
}

function addOnTheFlyEvent(el) {
    if (el.classList.contains("on-the-fly")) {
        return;
    }

    el.addEventListener("click",
        function (event) {
            aClick(event);
            event.preventDefault();
        },
        false
    );
    el.classList.add("on-the-fly");
}

function aClick(event) {
    var el = event.target;
    var decomposition = decomposePage(el.getAttribute('href'));
    window.setup.page = decomposition[0];
    window.setup.anchor = decomposition[1];
    console.log('page = ' + window.setup.page);
    console.log('anchor = ' + window.setup.anchor);
    getMDFile();
}

function redirectImages(node) {
    // redirect img's src
    var imgs = node.getElementsByTagName("img");
    var targetPath = computeTargetPath();
    for (var i = 0; i < imgs.length; i++) {
        var img = imgs[i];
        var src = img.getAttribute("src");
        var match = /^(\w*)\/([\w-\.]*)$/.exec(src);
        if (match && match.length == 3) {
            img.setAttribute("src", targetPath + match[1] + "/" + match[2]);
        }
    }
}

function applyAnchor() {
    console.log("Anchor: " + window.setup.anchor);
    var anchors = document.getElementsByName(window.setup.anchor);
    if (anchors.length > 0) {
        anchors[0].scrollIntoView(true);
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
    var view = document.getElementById("view");
    while (view.firstChild) {
        view.removeChild(view.firstChild);
    }

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

    redirectImages(div);
    redirectUrls(div);

    view.appendChild(div);
    applyAnchor();

    applyAnchorIcons(view);
    highlightCode(view);

    updateSelection();
}

function highlightCode(view) {
    hljs.configure({languages: ['c', 'cpp', 'java', 'python', 'matlab', 'bash', 'nohighlight']});

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
            el.classList.add("anchor-header");
            var span = document.createElement("span");
            span.classList.add("anchor-link-image");
            var a = document.createElement("a");
            a.setAttribute("href", "#" + name);
            a.classList.add("anchor-link");
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

    for (var i = 0; i < div.childNodes.length; i++) {
        var child = div.childNodes[i];
        if (child && child.tagName && child.tagName.length > 0 && child.tagName.toLowerCase() == "ul") {
            menu = child;
            break;
        }
    }

    if (!menu) {
        console.error("Cannot extract Menu.");
        return;
    }

    populateMenu(menu);
    redirectUrls(menu);

    updateSelection();
}

function updateSelection() {
    var selected = changeMenuSelection();
    populateNavigation(selected);
}

function getSelected() {
    var menu = document.getElementById("menu");
    var selecteds = menu.getElementsByClassName("selected");
    if (selecteds.length > 0) {
        return selecteds[selecteds.length - 1];
    }
    return null;
}

function changeMenuSelection() {
    var menu = document.getElementById("menu");
    var selecteds = [].slice.call(menu.getElementsByClassName("selected"));
    for (var i = 0; i < selecteds.length; i++) {
        var selected = selecteds[i];
        selected.classList.remove("selected");
    }

    var as = menu.getElementsByTagName("a");
    for (var i = 0; i < as.length; i++) {
        var a = as[i];
        var href = a.getAttribute("href");
        if (href.indexOf(window.setup.page) > -1) {
            var selected = a.parentNode;
            selected.classList.add("selected");
            if (selected.parentNode.parentNode.tagName.toLowerCase() == "li") {
                selected.parentNode.parentNode.classList.add("selected");
            }
            return selected;
        }
    }
}

function populateNavigation(selected) {
    var next = document.getElementById("next");
    var previous = document.getElementById("previous");
    var up = document.getElementById("up");

    if (!selected) {
        next.classList.add("disabled");
        previous.classList.add("disabled");
        up.classList.add("disabled");
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
            next.classList.remove("disabled");
            next.setAttribute("href", nextElement.getAttribute("href"));
            addOnTheFlyEvent(next);
        } else {
            next.classList.add("disabled");
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
            previous.classList.remove("disabled");
            previous.setAttribute("href", previousElement.getAttribute("href"));
            addOnTheFlyEvent(previous);
        } else {
            previous.classList.add("disabled");
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
            up.classList.remove("disabled");
            up.setAttribute("href", upElement.getAttribute("href"));
            addOnTheFlyEvent(up);
        } else {
            up.classList.add("disabled");
        }
    }
}

function populateMenu(menu) {
    var menuDiv = document.getElementById("menu");
    menuDiv.appendChild(menu);
    $(menu).menu();
}

function getMDFile() {
    var target = computeTargetPath() + window.setup.page;
    console.log("Get MD file: " + target);
    $.ajax({
        type: "GET",
        url: target,
        dataType: "text",
        success: populateViewDiv,
        error: function(XMLHttpRequest, textStatus, errorThrown) {
            console.log("Status: " + textStatus);
            console.log("Error: " + errorThrown);
            var mainPage = window.setup.book + ".md";
            // get the main page instead
            if (window.setup.page != mainPage) {
                window.setup.page = mainPage;
                getMDFile();
            }
        }
    });
}

function getMenuFile() {
    var target = computeTargetPath() + "menu.md";
    console.log("Get menu file: " + target);
    $.ajax({
        type: "GET",
        url: target,
        dataType: "text",
        success: receiveMenuContent,
        error: function(XMLHttpRequest, textStatus, errorThrown) {
            console.log("Status: " + textStatus);
            console.log("Error: " + errorThrown);
        }
    });
}

function extractAnchor() {
    var currentUrl = window.location.href;
    var match = /#([\w-]+)/.exec(currentUrl);
    if (match && match.length == 2) {
        return match[1];
    }
    return '';
}

document.addEventListener("DOMContentLoaded", function() {
    var page = getGETQueryValue("page", "guide.md");
    window.setup = {
        "book":   getGETQueryValue("book", "guide"),
        "page":   getGETQueryValue("page", "guide.md"),
        "anchor": extractAnchor(),
        "branch": getGETQueryValue("branch", "gh-pages"),
        "url":    getGETQueryValue("url", "https://raw.githubusercontent.com/omichel/webots-doc/")
    }
    console.log("Setup: " + JSON.stringify(window.setup));

    getMDFile();
    getMenuFile();
});
