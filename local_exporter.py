#!/usr/bin/env python

"""Copy 'index.html' to 'local.html' and get JS dependencies locally."""

import os
import platform
import re
import ssl
import sys
import urllib2

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
    'wwi/8.6/request_methods.js'
]


def download(url, target_file_path):
    """Download URL to file."""
    print '# downloading %s' % url

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
                response = urllib2.urlopen(url, timeout=5, context=ctx)
            else:
                response = urllib2.urlopen(url, timeout=5)
            content = response.read()

            f = open(target_file_path, 'w')
            f.write(content)
            f.close()

            break
        except urllib2.HTTPError, e:
            print 'HTTPError = ' + str(e.reason)
        except urllib2.URLError, e:
            print 'URLError = ' + str(e.reason)
        if i == nTrials - 1:
            sys.exit('Cannot get url: ' + url)
    if i > 0:
        print '# (number of trials: %d)' % (i + 1)


script_directory = os.path.dirname(os.path.realpath(__file__)) + os.sep

with open(script_directory + 'index.html', 'r') as file:
    content = file.read()

reg = r'"https://www\.cyberbotics\.com/([^"]*)"'
content = re.sub(reg, r'"dependencies/\1"', content)

with open(script_directory + 'local_index.html', 'w') as file:
    file.write(content)

for dependency in dependencies:
    download(
        'https://www.cyberbotics.com/' + dependency,
        script_directory + 'dependencies' + os.sep + dependency.replace(
            "/", os.sep)
    )
