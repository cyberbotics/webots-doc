<?php
  include 'header.php';
  # the URL follow this format https://www.cyberbotics.com/doc/book/page?v=version#anchor where version and anchor are optional
  $uri = substr(htmlspecialchars($_SERVER['REQUEST_URI']), 5); // we remove the "/doc/" prefix
  $i = strpos($uri, '/');
  if ($i !== FALSE) {
    $book = substr($uri, 0, $i);
    $j = strpos($uri, '?version=');
    if ($j === FALSE) {
      $page = substr($uri, $i + 1);
      $branch = '';
      $tag = '';
    } else {
      $page = substr($uri, $i + 1, $j - $i - 1);
      $version = substr($uri, $j + 9);
      if (preg_match('/^\d+\.\d*(.)+$/',$version)) {
        $branch = '';
        $tag = $version;
      } else {
        $branch = $version;
        $tag = '';
      }
    }
  } else {
    # default values:
    $book = 'guide';
    $page = 'guide'; # FIXME: should be 'index'
    $branch = '';
    $tag = '';
    # anchor is not sent to the server, so it has to be computed by the javascript
  }
?>
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
    <div id="center" style="top:46px">
      <div id="title">
        <h2 id="title-content">Documentation</h2>
      </div>
      <div id="view"></div>
    </div>
    <script src="https://www.cyberbotics.com/wwi/8.3/request_methods.js"></script>
    <script src="https://www.cyberbotics.com/highlight/9.2.0/highlight.min.js"></script>
    <script src="https://www.cyberbotics.com/showdown/1.3.0/showdown.min.js"></script>
    <script src="https://www.cyberbotics.com/files/repository/doc/showdown-extensions.js"></script>
    <script src="https://www.cyberbotics.com/files/repository/doc/viewer.js"></script>
    <script>
    setup = {
        "book":   "<?=$book?>",
        "page":   "<?=$page?>",
        "anchor": extractAnchor(),
        "branch": "<?=$branch?>",
        "tag":    "<?=$tag?>",
        "url":    "https://raw.githubusercontent.com/omichel/webots-doc/"
    }
    console.log("Setup: " + JSON.stringify(setup));
    </script>
<?php
  include 'footer.php';
?>