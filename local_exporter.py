#!/usr/bin/env python

"""Copy 'index.html' to 'local.html' and get JS dependencies locally."""

import os
import platform
import re
import ssl
import sys
try:
    # For Python 3.0 and later
    from urllib.request import urlopen, HTTPError, URLError
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen, HTTPError, URLError

silent = len(sys.argv) > 1 and (sys.argv[1] == '--silent')

dependencies = [
    'highlight/9.5.0/default.min.css',
    'highlight/9.5.0/highlight.min.js',
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
    'showdown/1.3.0/showdown.js',
    'showdown/1.3.0/showdown.js.map',
    'showdown/1.3.0/showdown.min.js',
    'showdown/1.3.0/showdown.min.js.map',
    'showdown/1.3.0/showdown-youtube.min.js',
    'wwi/R2018b/request_methods.js'
]


def download(url, target_file_path):
    """Download URL to file."""
    if not silent:
        print ('# downloading %s' % url)

    # Prepare the target directory
    target_directory = os.path.dirname(target_file_path)
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)

    # Sometimes Travis cannot get the file at the first trial
    nTrials = 3
    for i in range(nTrials):
        try:
            if platform.system() == 'Linux' and \
               hasattr(ssl, 'create_default_context'):
                # On Ubuntu 16.04 there are issues with the certificates.
                # But 'create_default_context' has been introduced in python
                # 2.7.9 and it is not available on Ubuntu 14.04.
                ctx = ssl.create_default_context()
                ctx.check_hostname = False
                ctx.verify_mode = ssl.CERT_NONE
                response = urlopen(url, timeout=5, context=ctx)
            else:
                response = urlopen(url, timeout=5)
            content = response.read()

            f = open(target_file_path, 'wb')
            f.write(content)
            os.chmod(target_file_path, 0o644)
            f.close()

            break
        except HTTPError as e:
            sys.stderr.write('HTTPError = ' + str(e.reason))
        except URLError as e:
            sys.stderr.write('URLError = ' + str(e.reason))
        if i == nTrials - 1:
            sys.exit('Cannot get url: ' + url)
    if i > 0:
        sys.stderr.write('# (number of trials: %d)' % (i + 1))


script_directory = os.path.dirname(os.path.realpath(__file__)) + os.sep

with open(script_directory + 'index.html', 'r') as file:
    content = file.read()

reg = r'"https://www\.cyberbotics\.com/([^"]*)"'
content = re.sub(reg, r'"dependencies/\1"', content)
if platform.system() == 'Darwin':
    content = content.replace('"css/main.css"', '"css/main.macos.css"')

html_file_path = script_directory + 'local_index.html'
with open(html_file_path, 'w') as file:
    file.write(content)
    os.chmod(html_file_path, 0o644)

for dependency in dependencies:
    download(
        'https://www.cyberbotics.com/' + dependency,
        script_directory + 'dependencies' + os.sep + dependency.replace("/", os.sep)
    )
