#!/usr/bin/env python

"""Copy 'index.html' to 'local.html' and get JS dependencies locally."""

import os
import re
import urllib2


def download(url, target_file_path):
    """Download URL to file."""
    print 'Download "%s" to "%s"' % (url, target_file_path)
    response = urllib2.urlopen(url, timeout=5)
    content = response.read()
    f = open(target_file_path, 'w')
    f.write(content)
    f.close()


if __name__ == '__main__':
    script_directory = os.path.dirname(os.path.realpath(__file__)) + os.sep

    with open(script_directory + 'index.html', 'r') as file:
        content = file.readlines()

    reg = r'"https://www\.cyberbotics\.com/([^"]*)"'

    with open(script_directory + 'local.html', 'w') as file:
        for line in content:
            m = re.search(reg, line)
            if m:
                line = re.sub(reg, r'"dependencies/\1"', line)
                relative_path = m.group(1)
                target_path = script_directory + 'dependencies' + os.sep + m.group(1)
                target_directory = os.path.dirname(target_path)
                if not os.path.exists(target_directory):
                    os.makedirs(target_directory)
                download(
                    'https://www.cyberbotics.com/' + relative_path,
                    target_path
                )
            file.write(line)
