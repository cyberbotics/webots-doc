"""Copy 'index.html' to 'local.html' and get JS dependencies locally."""

import re


if __name__ == '__main__':
    with open('index.html', 'r') as file:
        content = file.read()

    with open('local.html', 'w') as file:
        content = re.sub(
            r'"https://www\.cyberbotics\.com/([^"]*)"',
            r'"\1"', content
        )
        file.write(content)
