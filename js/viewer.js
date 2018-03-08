/* eslint no-extend-native: ["error", { "exceptions": ["String"] }] */
/* global getGETQueryValue */
/* global setup */
/* global showdown */
/* global hljs */

var handle;

if (typeof String.prototype.startsWith !== 'function') {
  String.prototype.startsWith = function(prefix) {
    return this.slice(0, prefix.length) === prefix;
  };
}

if (typeof String.prototype.endsWith !== 'function') {
  String.prototype.endsWith = function(suffix) {
    return this.indexOf(suffix, this.length - suffix.length) !== -1;
  };
}

var localSetup = (typeof setup === 'undefined') ? {} : setup;

var isCyberboticsUrl = location.href.indexOf('cyberbotics.com/doc') !== -1;

function setupCyberboticsUrl(url) {
  localSetup.book = 'guide';
  localSetup.page = 'index';
  localSetup.anchor = '';

  var m = url.match(new RegExp('/([^/]+)/([^/\\?#]+)([^/]*)$'));
  if (m) {
    localSetup.book = m[1];
    localSetup.page = m[2];
    var args = m[3];

    m = url.match(/version=([^&#]*)/);
    if (m) {
      var version = m[1];
      var n = version.indexOf(':');
      if (n === -1)
        localSetup.branch = version;
      else
        localSetup.branch = version.substr(n + 1);
    }

    m = args.match(/#([^&#]*)/);
    if (m)
      localSetup.anchor = m[1];
    else
      localSetup.anchor = '';
  }
}

function setupDefaultUrl(url) {
  var m;

  m = url.match(/page=([^&#]*)/);
  if (m)
    localSetup.page = m[1].replace(/.md$/, '');
  else
    localSetup.page = 'index';

  m = url.match(/book=([^&#]*)/);
  if (m)
    localSetup.book = m[1];
  else if (!localSetup.book)
    localSetup.book = 'guide';

  m = url.match(/#([^&#]*)/);
  if (m)
    localSetup.anchor = m[1];
  else
    localSetup.anchor = '';
}

function setupUrl(url) {
  if (isCyberboticsUrl)
    setupCyberboticsUrl(url);
  else
    setupDefaultUrl(url);
  console.log('book=' + localSetup.book + ' page=' + localSetup.page + ' branch=' + localSetup.branch + ' anchor=' + localSetup.anchor);
}

function computeTargetPath() {
  var branch = 'master';
  var targetPath = '';
  if (localSetup.branch)
    branch = localSetup.branch;
  if (localSetup.url.startsWith('http'))
    targetPath = localSetup.url + branch + '/';
  targetPath += localSetup.book + '/';
  return targetPath;
}

function redirectUrls(node) {
  // redirect a's href
  var as = node.querySelectorAll('a');
  for (var i = 0; i < as.length; i++) {
    var a = as[i];
    var href = a.getAttribute('href');
    if (!href)
      continue;
    else if (href.startsWith('#'))
      addDynamicAnchorEvent(a); // on firefox, the second click on the anchor is not dealt cleanly
    else if (href.startsWith('http')) // open external links in a new window
      a.setAttribute('target', '_blank');
    else if (href.endsWith('.md') || href.indexOf('.md#') > -1) {
      var match, newPage, anchor;
      if (href.startsWith('../')) { // Cross-book hyperlink case.
        match = /^..\/([\w-]+)\/([\w-]+).md(#[\w-]+)?$/.exec(href);
        if (match && match.length >= 3) {
          var book = match[1];
          newPage = match[2];
          anchor = match[3];
          if (anchor)
            anchor = anchor.substring(1); // remove the '#' character
          a.setAttribute('href', forgeUrl(book, newPage, anchor));
        }
      } else { // Cross-page hyperlink case.
        addDynamicLoadEvent(a);
        match = /^([\w-]+).md(#[\w-]+)?$/.exec(href);
        if (match && match.length >= 2) {
          newPage = match[1];
          anchor = match[2];
          if (anchor)
            anchor = anchor.substring(1); // remove the '#' character
          a.setAttribute('href', forgeUrl(localSetup.book, newPage, anchor));
        }
      }
    }
  }
}

function forgeUrl(book, page, anchor) {
  var anchorString = (anchor && anchor.length > 0) ? ('#' + anchor) : '';
  var url = location.href;
  if (isCyberboticsUrl) {
    var i = location.href.indexOf('cyberbotics.com/doc');
    url = location.href.substr(0, i) + 'cyberbotics.com/doc/' + book + '/' + page;
    if (localSetup.branch !== '' && localSetup.repository && localSetup.repository !== 'omichel')
      url += '?version=' + localSetup.repository + ':' + localSetup.branch;
    else if (localSetup.branch !== '')
      url += '?version=' + localSetup.branch;
    url += anchorString;
  } else {
    var isFirstArgument;

    // Add or replace the book argument.
    if (url.indexOf('book=') > -1)
      url = url.replace(/book=([^&]+)?/, 'book=' + book);
    else {
      isFirstArgument = (url.indexOf('?') < 0);
      url = url + (isFirstArgument ? '?' : '&') + 'book=' + book;
    }

    // Add or replace the page argument.
    if (url.indexOf('page=') > -1)
      url = url.replace(/page=([\w-]+)(#[\w-]+)?/, 'page=' + page + anchorString);
    else {
      isFirstArgument = (url.indexOf('?') < 0);
      url = url + (isFirstArgument ? '?' : '&') + 'page=' + page + anchorString;
    }
  }
  return url;
}

function addDynamicAnchorEvent(el) {
  if (el.classList.contains('dynamicAnchor'))
    return;
  el.addEventListener('click',
    function(event) {
      var node = event.target;
      while (node && !node.hasAttribute('href'))
        node = node.getParent();
      if (node) {
        localSetup.anchor = extractAnchor(node.getAttribute('href'));
        applyAnchor();
        event.preventDefault();
      }
    },
    false
  );
  el.classList.add('dynamicAnchor');
}

function addDynamicLoadEvent(el) {
  if (el.classList.contains('dynamicLoad'))
    return;
  el.addEventListener('click',
    function(event) {
      aClick(event.target);
      event.preventDefault();
    },
    false
  );
  el.classList.add('dynamicLoad');
}

function aClick(el) {
  setupUrl(el.getAttribute('href'));
  getMDFile();
  updateBrowserUrl();
}

function redirectImages(node) {
  // redirect img's src
  var imgs = node.querySelectorAll('img');
  var targetPath = computeTargetPath();
  for (var i = 0; i < imgs.length; i++) {
    var img = imgs[i];
    var src = img.getAttribute('src');
    var match = /^images\/(.*)$/.exec(src);
    if (match && match.length === 2)
      img.setAttribute('src', targetPath + 'images/' + match[1]);
  }
}

function applyAnchor() {
  var firstAnchor = document.querySelector("[name='" +localSetup.anchor +"']");
  if (firstAnchor) {
    firstAnchor.scrollIntoView(true);
    window.scrollBy(0, -80);
  } else
    window.scrollTo(0, 0);
}

function applyToTitleDiv() {
  var titleContentElement = document.querySelector('#title-content');
  if (titleContentElement) {
    var newTitle;
    if (localSetup.book === 'guide')
      newTitle = 'Webots User Guide';
    else if (localSetup.book === 'reference')
      newTitle = 'Webots Reference Manual';
    else if (localSetup.book === 'blog')
      newTitle = 'Webots Blog';
    else if (localSetup.book === 'automobile')
      newTitle = 'Webots for automobiles';
    else if (localSetup.book === 'robotis-op2')
      newTitle = 'Webots for ROBOTIS OP2';
    else
      newTitle = '';
    if (newTitle.length > 0) {
      newTitle += " <div class='release-tag'>" + getWebotsVersion() + '</div>';
      titleContentElement.innerHTML = newTitle;
    }
  }
}

function addContributionBanner() {
  // if we're on the website we need to move the banner down by the height of the navbar
  var displacement = document.querySelector("#footer") ? "44px" : "0px";

  // append contribution sticker to primary doc element
  document.querySelector("#center").innerHTML += "<div style='top:" + displacement + "' class='contribution-banner'>" +
                                                 "Found an error?" +
                                                 "<a target='_blank' href='https://github.com/omichel/webots-doc'> " +
                                                 "Contribute on GitHub!" +
                                                 "<span class=github-logo />" +
                                                 "</a>" +
                                                 "<p id='contribution-close'>X</p>" +
                                                 "</div>";

  var contributionBanner = document.querySelector(".contribution-banner");

  document.querySelector("#contribution-close").onclick = function () {
    contributionBanner.setAttribute("class", "contribution-banner");
  };

  setTimeout(function() { contributionBanner.setAttribute("class", "contribution-banner visible-banner"); }, 1500);
}

function setUpBlogStyleIfNeeded() {
  if (localSetup.book === 'blog') {
    var center = document.querySelector('#center');
    center.setAttribute('class', 'blog');

    setHandleWidth(0);

    document.title = 'Webots Blog';

    var figures = document.querySelectorAll('figure');
    if (figures.length > 0) {
      var modal = document.createElement('div');
      var caption = document.createElement('div');
      var close = document.createElement('span');
      var modalContent = document.createElement('img');

      modal.setAttribute('class', 'modal');
      modalContent.setAttribute('class', 'modal-content');
      caption.setAttribute('id', 'caption');

      close.setAttribute('class', 'close');
      close.innerHTML = '&times;';
      close.onclick = function() {
        modal.style.display = 'none';
      };

      modal.appendChild(close);
      modal.appendChild(modalContent);
      modal.appendChild(caption);

      figures[0].parentNode.appendChild(modal);

      window.onclick = function(event) {
        if (event.target === modal)
          modal.style.display = 'none';
      };

      var images = [];
      for (var i = figures.length - 1; i >= 0; i--) {
        figures[i].onclick = null;
        images[i] = figures[i].firstChild;
        images[i].onclick = function() {
          modal.style.display = 'block';
          modalContent.src = this.src;
          caption.innerHTML = this.parentNode.childNodes[1].innerHTML;
        };
      }
    }
  }
}

function getWebotsVersion() {
  if (localSetup.branch)
    return localSetup.branch;
  // Get the Webots version from the showdown wbVariables extension
  var version = '{{ webots.version.full }}';
  var converter = new showdown.Converter({extensions: ['wbVariables']});
  var html = converter.makeHtml(version);
  var tmp = document.createElement('div');
  tmp.innerHTML = html;
  return tmp.textContent || tmp.innerText || '';
}

function applyToPageTitle(mdContent) {
  var hashtagIndex = mdContent.indexOf('#');
  if (hashtagIndex >= 0) {
    while (hashtagIndex + 1 < mdContent.length && mdContent[hashtagIndex + 1] === '#')
      hashtagIndex += 1;
    var hashtagCarriageReturn = mdContent.indexOf('\n', hashtagIndex);
    if (hashtagCarriageReturn >= 0) {
      var title = mdContent.substring(hashtagIndex + 1, hashtagCarriageReturn).trim();
      document.title = 'Webots documentation: ' + title;
    }
  }
}

function populateViewDiv(mdContent) {
  setupUrl(document.location.href);

  var view = document.querySelector('#view');
  while (view.firstChild)
    view.removeChild(view.firstChild);

  // console.log('Raw MD content:\n\n');
  // console.log(mdContent);

  applyToPageTitle(mdContent);

  // markdown to html
  window.mermaidGraphCounter = 0;
  window.mermaidGraphs = {};
  var converter = new showdown.Converter({tables: 'True', extensions: ['wbChart', 'wbVariables', 'wbAPI', 'wbFigure', 'wbAnchors', 'wbIllustratedSection', 'youtube']});
  var html = converter.makeHtml(mdContent);

  // console.log('HTML content: \n\n')
  // console.log(html);

  view.innerHTML = html;

  renderGraphs();
  redirectImages(view);
  redirectUrls(view);

  var images = view.querySelectorAll('img');
  if (images.length > 0) {
    // apply the anchor only when the images are loaded,
    // otherwise, the anchor can be overestimated.
    var lastImage = images[images.length - 1];
    $(lastImage).load(applyAnchor);
  } else
    applyAnchor();

  applyAnchorIcons(view);
  highlightCode(view);

  updateSelection();
  setUpBlogStyleIfNeeded();
}

// replace the browser URL after a dynamic load
function updateBrowserUrl() {
  var url = forgeUrl(localSetup.book, localSetup.page, localSetup.anchor);
  if (history.pushState) {
    try {
      history.pushState({state: 'new'}, null, url);
    } catch (err) {
    }
  }
}

// Make in order that the back button is working correctly
window.onpopstate = function(event) {
  setupUrl(document.location.href);
  getMDFile();
};

function highlightCode(view) {
  var supportedLanguages = ['c', 'c++', 'java', 'python', 'matlab', 'sh', 'ini', 'tex', 'makefile', 'lua', 'xml'];

  for (var i = 0; i < supportedLanguages.length; i++) {
    var language = supportedLanguages[i];
    hljs.configure({languages: [ language ]});
    var codes = document.querySelectorAll("[class='language-" + language + "']");
    for (var j = 0; j < codes.length; j++) {
      var code = codes[j];
      hljs.highlightBlock(code);
    }
  }
}

function renderGraphs() {
  for (var id in window.mermaidGraphs) {
    window.mermaidAPI.render(id, window.mermaidGraphs[id], function(svgCode, bindFunctions) {
      document.querySelector('#' + id + 'Div').innerHTML = svgCode;
    });
  }
}

function applyAnchorIcons(view) {
  var elements = [];
  var tags = ['figcaption', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6'];
  var i;
  for (i = 0; i < tags.length; i++) {
    var array = Array.prototype.slice.call(view.querySelectorAll(tags[i]));
    elements = elements.concat(array);
  }
  for (i = 0; i < elements.length; i++) {
    var el = elements[i];
    var name = null;
    if (el.parentNode && el.tagName.toLowerCase() === 'figcaption' && el.parentNode.tagName.toLowerCase() === 'figure')
      name = el.parentNode.getAttribute('name');
    else
      name = el.getAttribute('name');
    if (name) {
      el.classList.add('anchor-header');
      var span = document.createElement('span');
      span.classList.add('anchor-link-image');
      var a = document.createElement('a');
      a.setAttribute('href', '#' + name);
      a.classList.add('anchor-link');
      a.appendChild(span);
      el.insertBefore(a, el.firstChild);
    }
  }
}

function receiveMenuContent(menuContent) {
  // console.log('Menu content:\n\n');
  // console.log(menuContent);

  var menu = null;

  var converter = new showdown.Converter();
  var html = converter.makeHtml(menuContent);
  var div = document.createElement('div');
  div.innerHTML = html;

  for (var i = 0; i < div.childNodes.length; i++) {
    var child = div.childNodes[i];
    if (child && child.tagName && child.tagName.length > 0 && child.tagName.toLowerCase() === 'ul') {
      menu = child;
      break;
    }
  }

  if (!menu) {
    console.error('Cannot extract Menu.');
    return;
  }

  populateMenu(menu);
  redirectUrls(menu);
  updateSelection();
}

function updateMenuScrollbar() {
  var e = document.documentElement;
  var t = document.documentElement.scrollTop || document.body.scrollTop;
  var p = e.scrollHeight - t - e.clientHeight;
  if (p < 244) // 244 is the height in pixels of the footer of Cyberbotics web page
    document.querySelector('#left').style.height = (e.clientHeight - 290 + p) + 'px';
  else // 44 is the height in pixels of the header of Cyberbotics web page (44 + 244 = 290)
    document.querySelector('#left').style.height = 'calc(100% - 44px)';
}

function updateSelection() {
  var selected = changeMenuSelection();
  populateNavigation(selected);
  if (isCyberboticsUrl)
    updateMenuScrollbar();
}

function changeMenuSelection() {
  var menu = document.querySelector('#menu');
  var selecteds = [].slice.call(menu.querySelectorAll('.selected'));
  var i;
  var selected;
  for (i = 0; i < selecteds.length; i++) {
    selected = selecteds[i];
    selected.classList.remove('selected');
  }
  var as = menu.querySelectorAll('a');
  for (i = 0; i < as.length; i++) {
    var a = as[i];
    var href = a.getAttribute('href');
    var selection;
    if (!isCyberboticsUrl) {
      var pageIndex = href.indexOf('page=' + localSetup.page);
      // Notes:
      // - the string length test is done to avoid wrong positive cases
      //   where a page is a prefix of another.
      // - 5 matches with the 'page=' string length.
      if (pageIndex > -1 && (5 + pageIndex + localSetup.page.length) === href.length)
        selection = true;
      else
        selection = false;
    } else {
      var n = href.indexOf('?');
      if (n > -1)
        href = href.substring(0, n);
      n = href.indexOf('#');
      if (n > -1)
        href = href.substring(0, n);
      if (href.endsWith('/doc/' + localSetup.book + '/' + localSetup.page))
        selection = true;
      else
        selection = false;
    }
    if (selection) {
      selected = a.parentNode;
      selected.classList.add('selected');
      if (selected.parentNode.parentNode.tagName.toLowerCase() === 'li') {
        selected.parentNode.parentNode.classList.add('selected');
        var firstChild = selected.parentNode.parentNode.firstChild;
        if (firstChild.tagName.toLowerCase() === 'a')
          showAccodionItem(firstChild);
      } else
        showAccodionItem(a);
      return selected;
    }
  }
}

function populateNavigation(selected) {
  var next = document.querySelector('#next');
  var previous = document.querySelector('#previous');
  var up = document.querySelector('#up');
  var toc = document.querySelector('#toc');
  var as;

  toc.setAttribute('href', forgeUrl(localSetup.book, 'menu'));
  addDynamicLoadEvent(toc);

  if (!selected) {
    next.classList.add('disabled');
    previous.classList.add('disabled');
    up.classList.add('disabled');
    return;
  }

  if (next) {
    var nextElement = null;

    var nextLiSibling = selected.nextSibling;
    while (nextLiSibling) {
      if (nextLiSibling.tagName && nextLiSibling.tagName.toLowerCase() === 'li')
        break;
      nextLiSibling = nextLiSibling.nextSibling;
    }
    if (nextLiSibling) {
      as = nextLiSibling.querySelectorAll('a');
      if (as.length > 0)
        nextElement = as[0];
    }

    if (nextElement) {
      next.classList.remove('disabled');
      next.setAttribute('href', nextElement.getAttribute('href'));
      addDynamicLoadEvent(next);
    } else
      next.classList.add('disabled');
  }

  if (previous) {
    var previousElement = null;

    var previousLiSibling = selected.previousSibling;
    while (previousLiSibling) {
      if (previousLiSibling.tagName && previousLiSibling.tagName.toLowerCase() === 'li')
        break;
      previousLiSibling = previousLiSibling.previousSibling;
    }
    if (previousLiSibling) {
      as = previousLiSibling.querySelectorAll('a');
      if (as.length > 0)
        previousElement = as[0];
    }

    if (previousElement) {
      previous.classList.remove('disabled');
      previous.setAttribute('href', previousElement.getAttribute('href'));
      addDynamicLoadEvent(previous);
    } else
      previous.classList.add('disabled');
  }

  if (up) {
    var upElement = null;
    var parentLi = null;
    if (selected.parentNode.parentNode.tagName.toLowerCase() === 'li')
      parentLi = selected.parentNode.parentNode;
    if (parentLi) {
      as = parentLi.querySelectorAll('a');
      if (as.length > 0)
        upElement = as[0];
    }

    if (upElement) {
      up.classList.remove('disabled');
      up.setAttribute('href', upElement.getAttribute('href'));
      addDynamicLoadEvent(up);
    } else {
      up.setAttribute('href', forgeUrl(localSetup.book, 'index'));
      addDynamicLoadEvent(up);
      up.classList.remove('disabled');
    }
  }
}

function populateMenu(menu) {
  // make in order that the <li> tags above the <a> are also clickable
  var lis = menu.querySelectorAll('li');
  for (var i = 0; i < lis.length; i++) {
    var li = lis[i];
    li.addEventListener('click',
      function(event) {
        var as = event.target.querySelectorAll('a');
        if (as.length > 0)
          aClick(as[0]);
      }
    );
  }

  var menuDiv = document.querySelector('#menu');
  menuDiv.appendChild(menu);

  menu.setAttribute('id', 'accordion');
  $('#accordion > li > a').click(function() {
    showAccodionItem(this);
  });
}

function showAccodionItem(item) {
  if (!$(item).hasClass('active')) {
    $('#accordion li ul').slideUp();
    $(item).next().slideToggle();
    $('#accordion li a').removeClass('active');
    $(item).addClass('active');
  }
}

function getMDFile() {
  var target = computeTargetPath() + localSetup.page + '.md';
  console.log('Get MD file: ' + target);
  $.ajax({
    type: 'GET',
    url: target,
    dataType: 'text',
    success: populateViewDiv,
    error: function(XMLHttpRequest, textStatus, errorThrown) {
      console.log('Status: ' + textStatus);
      console.log('Error: ' + errorThrown);
      var mainPage = 'index';
      // get the main page instead
      if (localSetup.page !== mainPage) {
        localSetup.page = mainPage;
        getMDFile();
      }
    }
  });
}

function getMenuFile() {
  var target = computeTargetPath() + 'menu.md';
  console.log('Get menu file: ' + target);
  $.ajax({
    type: 'GET',
    url: target,
    dataType: 'text',
    success: receiveMenuContent,
    error: function(XMLHttpRequest, textStatus, errorThrown) {
      console.log('Status: ' + textStatus);
      console.log('Error: ' + errorThrown);
    }
  });
}

function extractAnchor(url) {
  var match = /#([\w-]+)/.exec(url);
  if (match && match.length === 2)
    return match[1];
  return '';
}

// width: in pixels
function setHandleWidth(width) {
  handle.left.css('width', width + 'px');
  handle.handle.css('left', width + 'px');
  handle.center.css('left', width + 'px');
  handle.center.css('width', 'calc(100% - ' + width + 'px)');
}

function initializeHandle() {
  // inspired from: http://stackoverflow.com/questions/17855401/how-do-i-make-a-div-width-draggable
  handle = {}; // structure where all the handle info is stored

  handle.left = $('#left');
  handle.center = $('#center');
  handle.handle = $('#handle');
  handle.container = $('#webots-doc');

  // dimension bounds of the handle in pixels
  handle.min = 0;
  handle.minThreshold = 75; // under this threshold, the handle is totally hidden
  if (localSetup.menuWidth && localSetup.menuWidth !== '')
    handle.initialWidth = localSetup.menuWidth;
  else
    handle.initialWidth = handle.left.width();
  handle.max = Math.max(250, handle.initialWidth);

  handle.isResizing = false;
  handle.lastDownX = 0;

  if (isCyberboticsUrl) {
    handle.left.addClass('cyberbotics');
    handle.handle.addClass('cyberbotics');
    handle.center.addClass('cyberbotics');
  } else {
    handle.left.addClass('default');
    handle.handle.addClass('default');
    handle.center.addClass('default');
  }

  setHandleWidth(handle.initialWidth);

  handle.handle.on('mousedown', function(e) {
    handle.isResizing = true;
    handle.lastDownX = e.clientX;
    handle.container.css('user-select', 'none');
  }).on('dblclick', function(e) {
    if (handle.left.css('width').startsWith('0'))
      setHandleWidth(handle.initialWidth);
    else
      setHandleWidth(0);
  });

  $(document).on('mousemove', function(e) {
    if (!handle.isResizing)
      return;
    var mousePosition = e.clientX - handle.container.offset().left; // in pixels
    if (mousePosition < handle.minThreshold / 2) {
      setHandleWidth(0);
      return;
    } else if (mousePosition < handle.minThreshold)
      return;
    if (mousePosition < handle.min || mousePosition > handle.max)
      return;
    setHandleWidth(mousePosition);
  }).on('mouseup', function(e) {
    handle.isResizing = false;
    handle.container.css('user-select', 'auto');
  });
}

window.onscroll = function() {
  if (!isCyberboticsUrl)
    return;
  updateMenuScrollbar();
};

document.addEventListener('DOMContentLoaded', function() {
  window.mermaidAPI.initialize({startOnLoad: false});
  initializeHandle();

  if (!isCyberboticsUrl) {
    if (!localSetup.url)
      localSetup.url = getGETQueryValue('url', 'https://raw.githubusercontent.com/omichel/webots-doc/');
    if (!localSetup.book)
      localSetup.book = getGETQueryValue('book', 'guide');
    if (!localSetup.page)
      localSetup.page = getGETQueryValue('page', 'index');
    if (!localSetup.anchor)
      localSetup.anchor = window.location.hash.substring(1);
    if (!localSetup.branch)
      localSetup.branch = getGETQueryValue('branch', 'master');
  }

  applyToTitleDiv();
  getMDFile();
  getMenuFile();
  addContributionBanner();
});
