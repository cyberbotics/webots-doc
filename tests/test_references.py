"""Test module of the references."""
import unittest
from books import Books

from email.utils import parseaddr
import os
import re


def slugify(txt):
    """Slugify function."""
    output = txt.lower()
    output = re.sub(r'<[^>]+>', '', output)
    output = output.replace('+', 'p')
    output = re.sub(r'[\(\):`]', '', output)
    output = re.sub(r'[\W-]+', '-', output)
    output = re.sub(r'^-*', '', output)
    output = re.sub(r'-*$', '', output)
    return output.strip(' ').strip('-')


class TestReferences(unittest.TestCase):
    """Unit test of the references."""

    def setUp(self):
        """Setup."""
        books = Books()
        self.anchors = {}
        for book in books.books:
            for md_path in book.md_paths:
                anchors = []
                with open(md_path) as f:
                    for line in f:
                        if '<a' in line and 'name=' in line:
                            for m in re.finditer(
                                    r'<a[^>]*name\s*=\s*"(.*)"[^>]*>',
                                    line.strip()):
                                anchors.append(m.group(1))
                        if line.startswith('#'):
                            title = re.sub(r'^#*', '', line)
                            anchors.append(slugify(title))
                        elif line.startswith('%figure'):
                            title = line.replace('%figure', '')
                            anchors.append(slugify(title))
                        elif line.startswith('%api'):
                            title = line.replace('%api', '')
                            anchors.append(slugify(title))
                self.anchors[md_path] = anchors

    def test_references_are_valid(self):
        """Test that the MD files are pointing on valid URLs."""
        books = Books()
        for book in books.books:
            for md_path in book.md_paths:
                with open(md_path) as f:
                    content = f.read()
                for m in re.finditer(r"[^!]\[(.*?)\]\(([^\)]+)\)", content):
                    # remove parameters
                    ref = m.group(2)
                    # 1. external link
                    if ref.startswith('www') or ref.startswith('http'):
                        continue
                    # 2. mailto
                    if ref.startswith('mailto:'):
                        mailto = ref[len('mailto:') + 1:]
                        (name, address) = parseaddr(mailto)
                        self.assertGreater(
                            address, 0,
                            msg='Invalid address "%s"' % (mailto)
                        )
                        continue
                    # 3. link to another MD file
                    ref = ref.split('#')
                    link = ref[0]
                    self.assertGreater(len(ref), 0, msg='Invalid reference')
                    self.assertTrue(
                        link.endswith('.md'),
                        msg='Invalid reference "%s" in %s:\n-> "%s"' %
                            (ref, md_path, m.group(0))
                    )
                    file_path = os.path.join(book.path, link)
                    self.assertTrue(
                        os.path.isfile(file_path),
                        msg='%s: "%s" not found' % (md_path, file_path)
                    )
                    # 4. Anchor
                    if len(ref) > 1:
                        anchor = ref[1]
                        found = anchor in self.anchors[file_path]
                        self.assertTrue(
                            found, msg='%s: %s#%s not found' %
                            (md_path, file_path, anchor)
                        )
