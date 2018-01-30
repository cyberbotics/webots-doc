<?php
  $request_uri = htmlspecialchars($_SERVER['REQUEST_URI']);
  if (substr($request_uri, 0, 5) != "/doc/") { # redirect aliases
    $request_uri = "/doc/".substr($request_uri, 1)."/index"; // we remove the "/" prefix
    header("Location: $request_uri");
    exit();
  }
  # the URL follow this format https://www.cyberbotics.com/doc/book/page?version=tagOrBranch#anchor where version and anchor are optional
  $uri = substr($request_uri, 5); // we remove the "/doc/" prefix
  $i = strpos($uri, '/');
  unset($repository);
  if ($i !== FALSE) {
    $book = substr($uri, 0, $i);
    $j = strpos($uri, '?version=');
    if ($j === FALSE) {
      $page = substr($uri, $i + 1);
      $branch = '';
    } else {
      $page = substr($uri, $i + 1, $j - $i - 1);
      $version = substr($uri, $j + 9);
      $n = strpos($version, ':');
      if ($n === FALSE)
        $branch = $version;
      else {
        $branch = substr($version, $n + 1);
        $repository = substr($version, 0, $n);
      }
    }
  } else {
    # default values:
    $book = $uri;
    $page = 'index';
    $branch = '';
    # anchor is not sent to the server, so it has to be computed by the javascript
  }
  if (!isset($repository))
    $repository = 'omichel';
  $url = "https://raw.githubusercontent.com/$repository/webots-doc/";
  $rawgiturl = "https://cdn.rawgit.com/$repository/webots-doc/";
  $scripts="
    <script>
      setup = {
        'book':       '$book',
        'page':       '$page',
        'anchor':     window.location.hash.substring(1),
        'branch':     '$branch',
        'repository': '$repository',
        'url':        '$url'
      }
      console.log('Setup: ' + JSON.stringify(setup));
    </script>
    <link rel='stylesheet' type='text/css' href='$rawgiturl$branch/css/webots-doc.css'/>
    <link rel='stylesheet' type='text/css' href='https://www.cyberbotics.com/highlight/9.5.0/default.min.css'/>
    <script src='https://www.cyberbotics.com/wwi/R2018a/request_methods.js'></script>
    <script src='https://www.cyberbotics.com/highlight/9.5.0/highlight.min.js'></script>
    <script src='https://www.cyberbotics.com/showdown/1.3.0/showdown.min.js'></script>
    <script src='https://www.cyberbotics.com/showdown/1.3.0/showdown-youtube.min.js'></script>
    <script src='$rawgiturl$branch/js/showdown-extensions.js'></script>
    <script src='$rawgiturl$branch/js/viewer.js'></script>
  ";
  include 'header.php';
?>
    <div class="webots-doc" id="webots-doc" style="padding:0;">
      <div id="left" style="top:46px;height:calc(100% - 46px)">
        <div id="navigation">
          <table>
            <tr>
              <td colspan="3"><a id="toc" title="Table of Contents">&equiv;</a></td>
            </tr>
            <tr>
              <td><a id="previous" title="Previous page">&#x25C0;</a></td>
              <td><a id="up" title="Up page">&#x25B2;</a></td>
              <td><a id="next" title="Next page">&#x25B6;</a></td>
            </tr>
          </table>
        </div>
        <div id="menu"></div>
      </div>
      <div id="handle"></div>
      <div id="center" style="top:46px">
        <div id="title">
          <h2 id="title-content">Documentation</h2>
        </div>
        <div id="view"></div>
      </div>
    </div>
<?php
  include 'footer.php';
?>
