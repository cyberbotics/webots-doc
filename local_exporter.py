#!/usr/bin/env python

"""Copy 'index.template.html' to 'index.html' and get JS dependencies locally."""

import os
import platform
import shutil
import ssl
import sys

try:
    # For Python 3.0 and later
    from urllib.request import urlopen, HTTPError, URLError
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen, HTTPError, URLError


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


if __name__ == "__main__":
    silent = '--silent' in sys.argv
    script_directory = os.path.dirname(os.path.realpath(__file__)) + os.sep

    with open(script_directory + 'index.template.html', 'r') as file:
        content = file.read()

    dependencies = []
    with open('dependencies.txt', 'r') as f:
        for line in f:
            line = line.replace('\n', '')
            if line and not line.startswith('#'):
                dependencies.append(line)
    jsString = ''
    cssString = ''
    for dependency in dependencies:
        if dependency.endswith('.css'):
            cssString += '<link type="text/css" rel="stylesheet" href="dependencies/%s"/>' % dependency
        if dependency.endswith('.js'):
            jsString += '<script src="dependencies/%s"></script>' % dependency

    content = content.replace('%{ JS }%', jsString)
    content = content.replace('%{ CSS }%', cssString)
    if platform.system() == 'Darwin':
        content = content.replace('"css/main.css"', '"css/main.macos.css"')

    html_file_path = script_directory + 'index.html'
    with open(html_file_path, 'w') as file:
        file.write(content)
        os.chmod(html_file_path, 0o644)

    shutil.rmtree(script_directory + 'dependencies')
    for dependency in dependencies:
        download(
            'https://www.cyberbotics.com/' + dependency,
            script_directory + 'dependencies' + os.sep + dependency.replace("/", os.sep)
        )
