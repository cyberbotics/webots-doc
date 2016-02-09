showdown.extension("wbFigure", function() {
    'use strict';

    return [
        {
            type: "lang",
            filter: function(text, converter, options) {
                text = text.replace(/%figure\s+"([^]+?)"([^]+?)%end/gi, function(match, title, content) {
                    var foo = converter.makeHtml(content);
                    return "<figure>" + foo + "<figcaption>" + title + "</figcaption></figure>";
                });
                return text;
            }
        },
        {
            type: "html",
            regex: /<figure><p><img([^]+?)<\/p><figcaption>/gi,
            replace: function (match, content) {
                return "<figure><img" + content + "<figcaption>";
            }
        }
    ]
});

showdown.extension("wbSuperscript", function() {
    'use strict';

    return [
        {
            type: "html",
            regex: /\^\s*\(([^]+?)\)/gi,
            replace: function (match, content) {
                return "<sup>" + content + "</sup>";
            }
        }
    ]
});
