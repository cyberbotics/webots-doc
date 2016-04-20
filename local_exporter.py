#!/usr/bin/env python

"""Copy 'index.html' to 'local.html' and get JS dependencies locally."""

import os
import re
import urllib2

dependencies = [
    'highlight/9.2.0/default.min.css',
    'highlight/9.2.0/highlight.min.js',
    'jquery/1.11.3/jquery.min.js',
    'jquery/1.11.3/jquery.min.map',
    'jquery-ui/1.11.4/jquery-ui.min.css',
    'jquery-ui/1.11.4/jquery-ui.min.js',
    'jquery-ui/1.11.4/theme.css',
    'jquery-ui/1.11.4/images/ui-bg_flat_0_aaaaaa_40x100.png',
    'jquery-ui/1.11.4/images/ui-bg_flat_75_ffffff_40x100.png',
    'jquery-ui/1.11.4/images/ui-bg_glass_55_fbf9ee_1x400.png',
    'jquery-ui/1.11.4/images/ui-bg_glass_65_ffffff_1x400.png',
    'jquery-ui/1.11.4/images/ui-bg_glass_75_dadada_1x400.png',
    'jquery-ui/1.11.4/images/ui-bg_glass_75_e6e6e6_1x400.png',
    'jquery-ui/1.11.4/images/ui-bg_glass_95_fef1ec_1x400.png',
    'jquery-ui/1.11.4/images/ui-bg_highlight-soft_75_cccccc_1x100.png',
    'jquery-ui/1.11.4/images/ui-icons_222222_256x240.png',
    'jquery-ui/1.11.4/images/ui-icons_2e83ff_256x240.png',
    'jquery-ui/1.11.4/images/ui-icons_454545_256x240.png',
    'jquery-ui/1.11.4/images/ui-icons_888888_256x240.png',
    'jquery-ui/1.11.4/images/ui-icons_cd0a0a_256x240.png',
    'mathjax/2.6.1/extensions/MathEvents.js',
    'mathjax/2.6.1/extensions/MathMenu.js',
    'mathjax/2.6.1/extensions/MathZoom.js',
    'mathjax/2.6.1/fonts/HTML-CSS/TeX/otf/MathJax_Script-Regular.otf',
    'mathjax/2.6.1/fonts/HTML-CSS/TeX/otf/MathJax_Math-Regular.otf',
    'mathjax/2.6.1/fonts/HTML-CSS/TeX/otf/MathJax_Typewriter-Regular.otf',
    'mathjax/2.6.1/fonts/HTML-CSS/TeX/otf/MathJax_Main-Italic.otf',
    'mathjax/2.6.1/fonts/HTML-CSS/TeX/otf/MathJax_Math-BoldItalic.otf',
    'mathjax/2.6.1/fonts/HTML-CSS/TeX/otf/MathJax_Size2-Regular.otf',
    'mathjax/2.6.1/fonts/HTML-CSS/TeX/otf/MathJax_Main-Regular.otf',
    'mathjax/2.6.1/fonts/HTML-CSS/TeX/otf/MathJax_Fraktur-Bold.otf',
    'mathjax/2.6.1/fonts/HTML-CSS/TeX/otf/MathJax_SansSerif-Italic.otf',
    'mathjax/2.6.1/fonts/HTML-CSS/TeX/otf/MathJax_Size1-Regular.otf',
    'mathjax/2.6.1/fonts/HTML-CSS/TeX/otf/MathJax_Size4-Regular.otf',
    'mathjax/2.6.1/fonts/HTML-CSS/TeX/otf/MathJax_WinChrome-Regular.otf',
    'mathjax/2.6.1/fonts/HTML-CSS/TeX/otf/MathJax_SansSerif-Regular.otf',
    'mathjax/2.6.1/fonts/HTML-CSS/TeX/otf/MathJax_AMS-Regular.otf',
    'mathjax/2.6.1/fonts/HTML-CSS/TeX/otf/MathJax_Main-Bold.otf',
    'mathjax/2.6.1/fonts/HTML-CSS/TeX/otf/MathJax_Size3-Regular.otf',
    'mathjax/2.6.1/fonts/HTML-CSS/TeX/otf/MathJax_Math-Italic.otf',
    'mathjax/2.6.1/fonts/HTML-CSS/TeX/otf/MathJax_Fraktur-Regular.otf',
    'mathjax/2.6.1/fonts/HTML-CSS/TeX/otf/MathJax_Caligraphic-Regular.otf',
    'mathjax/2.6.1/fonts/HTML-CSS/TeX/otf/MathJax_SansSerif-Bold.otf',
    'mathjax/2.6.1/fonts/HTML-CSS/TeX/otf/MathJax_Caligraphic-Bold.otf',
    'mathjax/2.6.1/fonts/HTML-CSS/TeX/otf/MathJax_WinIE6-Regular.otf',
    'mathjax/2.6.1/fonts/HTML-CSS/TeX/woff/MathJax_Fraktur-Regular.woff',
    'mathjax/2.6.1/fonts/HTML-CSS/TeX/woff/MathJax_Script-Regular.woff',
    'mathjax/2.6.1/fonts/HTML-CSS/TeX/woff/MathJax_Caligraphic-Regular.woff',
    'mathjax/2.6.1/fonts/HTML-CSS/TeX/woff/MathJax_AMS-Regular.woff',
    'mathjax/2.6.1/fonts/HTML-CSS/TeX/woff/MathJax_Caligraphic-Bold.woff',
    'mathjax/2.6.1/fonts/HTML-CSS/TeX/woff/MathJax_Size1-Regular.woff',
    'mathjax/2.6.1/fonts/HTML-CSS/TeX/woff/MathJax_SansSerif-Regular.woff',
    'mathjax/2.6.1/fonts/HTML-CSS/TeX/woff/MathJax_Main-Regular.woff',
    'mathjax/2.6.1/fonts/HTML-CSS/TeX/woff/MathJax_SansSerif-Bold.woff',
    'mathjax/2.6.1/fonts/HTML-CSS/TeX/woff/MathJax_Size2-Regular.woff',
    'mathjax/2.6.1/fonts/HTML-CSS/TeX/woff/MathJax_Main-Italic.woff',
    'mathjax/2.6.1/fonts/HTML-CSS/TeX/woff/MathJax_Typewriter-Regular.woff',
    'mathjax/2.6.1/fonts/HTML-CSS/TeX/woff/MathJax_Fraktur-Bold.woff',
    'mathjax/2.6.1/fonts/HTML-CSS/TeX/woff/MathJax_Size4-Regular.woff',
    'mathjax/2.6.1/fonts/HTML-CSS/TeX/woff/MathJax_Math-BoldItalic.woff',
    'mathjax/2.6.1/fonts/HTML-CSS/TeX/woff/MathJax_Main-Bold.woff',
    'mathjax/2.6.1/fonts/HTML-CSS/TeX/woff/MathJax_Math-Italic.woff',
    'mathjax/2.6.1/fonts/HTML-CSS/TeX/woff/MathJax_SansSerif-Italic.woff',
    'mathjax/2.6.1/fonts/HTML-CSS/TeX/woff/MathJax_Size3-Regular.woff',
    'mathjax/2.6.1/fonts/HTML-CSS/TeX/woff/MathJax_Math-Regular.woff',
    'mathjax/2.6.1/jax/element/mml/jax.js',
    'mathjax/2.6.1/jax/input/TeX/config.js',
    'mathjax/2.6.1/jax/input/TeX/jax.js',
    'mathjax/2.6.1/jax/output/HTML-CSS/autoload/mtable.js',
    'mathjax/2.6.1/jax/output/HTML-CSS/config.js',
    'mathjax/2.6.1/jax/output/HTML-CSS/fonts/imageFonts.js',
    'mathjax/2.6.1/jax/output/HTML-CSS/fonts/STIX/fontdata.js',
    'mathjax/2.6.1/jax/output/HTML-CSS/fonts/TeX/fontdata.js',
    'mathjax/2.6.1/jax/output/HTML-CSS/config.js',
    'mathjax/2.6.1/jax/output/HTML-CSS/jax.js',
    'mathjax/2.6.1/jax/output/HTML-CSS/autoload/mtable.js',
    'mathjax/2.6.1/MathJax.js',
    'showdown/1.3.0/showdown.js',
    'showdown/1.3.0/showdown.js.map',
    'showdown/1.3.0/showdown.min.js',
    'showdown/1.3.0/showdown.min.js.map',
    'wwi/8.3/request_methods.js'
]


def download(url, target_file_path):
    """Download URL to file."""
    print 'Download "%s" to "%s"' % (url, target_file_path)

    response = urllib2.urlopen(url, timeout=5)
    content = response.read()

    target_directory = os.path.dirname(target_file_path)
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)

    f = open(target_file_path, 'w')
    f.write(content)
    f.close()


script_directory = os.path.dirname(os.path.realpath(__file__)) + os.sep

with open(script_directory + 'index.html', 'r') as file:
    content = file.read()

reg = r'"https://www\.cyberbotics\.com/([^"]*)"'
content = re.sub(reg, r'"dependencies/\1"', content)

with open(script_directory + 'local_index.html', 'w') as file:
    file.write(content)

for dependency in dependencies:
    download(
        'http://www.cyberbotics.com/' + dependency,
        script_directory + 'dependencies' + os.sep + dependency.replace(
            "/", os.sep)
    )
