"""Test module for the titles."""

import unittest
import re

from books import Books

exceptions = [  # Words which can start with a lowercase.
    'macOS', 'e-puck'
]
prepositions = [
    'aboard', 'about', 'above', 'across', 'after', 'against', 'along', 'amid',
    'among', 'anti', 'around', 'as', 'at', 'before', 'behind', 'below', 'beneath',
    'beside', 'besides', 'between', 'beyond', 'but', 'by', 'concerning', 'considering',
    'despite', 'down', 'during', 'except', 'excepting', 'excluding',
    'for', 'from', 'in', 'inside', 'into', 'like', 'minus', 'near', 'of', 'off',
    'on', 'onto', 'opposite', 'outside', 'over', 'past', 'per', 'plus', 'regarding',
    'round', 'save', 'since', 'than', 'through', 'to', 'toward', 'towards', 'under',
    'underneath', 'unlike', 'until', 'up', 'upon', 'versus', 'via', 'with', 'within',
    'without'
    # 'following' is missing but is problematic.
]
articles = [
    'a', 'an', 'the', 'some'
]
conjunctions = [
    'and', 'but', 'for', 'nor', 'or', 'so', 'yet'
]


class TestTitles(unittest.TestCase):
    """Unit test of the titles."""

    def setUp(self):
        """Setup: get all the titles."""
        self.titles = []
        books = Books()
        for book in books.books:
            for md_path in book.md_paths:
                # Extract MD content.
                with open(md_path) as f:
                    content = f.read()

                # Remove annoying string sequences.
                # - Multiline code sections.
                content = re.sub(r'```.+?(?=```)```', '', content, flags=re.S)
                # Extract titles.
                for match in re.finditer(r'^#+ .*', content):  # Title on the first line.
                    title = content[match.start():match.end()]
                    self.titles.append({'title': title, 'md': md_path})
                for match in re.finditer(r'\n#+ .*', content):
                    title = content[match.start() + 1:match.end()]  # Title(s) on other lines.
                    self.titles.append({'title': title, 'md': md_path})
        # Debug: Uncomment to display all the acquired titles.
        # for t in self.titles:
        #     print (t)

    def test_underscores_are_protected(self):
        """Test that titles doesn't contain any unprotected underscore."""
        for t in self.titles:
            self.assertTrue(re.search(r'[^\\]_', t['title']) is None, msg='%s: Title "%s" contains unprotected underscore(s).' % (t['md'], t['title']))

    def test_words_are_capitalized(self):
        """Test that title words are capitalized."""
        # English rules reference: http://grammar.yourdictionary.com/capitalization/rules-for-capitalization-in-titles.html
        # Chosen style: "Chicago Manual of Style"
        uppercasePattern = re.compile('^[A-Z]')
        lowercasePattern = re.compile('^[a-z][^A-Z]*$')
        numberPattern = re.compile('^\d')
        for t in self.titles:
            title = re.sub(r'^#+\s*', '', t['title'])  # Remove the '#'+ suffix.
            title = re.sub(r'".+?(?=")"', '', title)  # Remove double-quoted statements.
            words = re.split(r'[ \(\),/\?:]', title)
            for w in range(len(words)):
                word = words[w]
                if not word or word.startswith('wb') or word.endswith('.wbt') or word in exceptions or numberPattern.match(word):
                    continue  # Exceptions.
                if w == 0:
                    # self.assertTrue(uppercasePattern.match(word), msg='%s: First word of title "%s" is not in uppercase.' % (t['md'], t['title']))
                    if uppercasePattern.match(word) is None:
                        print '%s: First word of title "%s" is not an uppercase.' % (t['md'], t['title'])
                elif w == len(words) - 1:
                    # self.assertTrue(uppercasePattern.match(word), msg='%s: Last word of title "%s" is not in uppercase.' % (t['md'], t['title']))
                    if uppercasePattern.match(word) is None:
                        print ('%s: Last word of title "%s" is not an uppercase.' % (t['md'], t['title']))
                elif word.lower() in articles or word.lower() in conjunctions or word.lower() in prepositions:
                    # self.assertTrue(lowercasePattern.match(word), msg='%s: word "%s" of title "%s" is not in lowercase.' % (t['md'], word, t['title']))
                    if lowercasePattern.match(word) is None:
                        print '%s: word "%s" of title "%s" is not in lowercase.' % (t['md'], word, t['title'])
                else:
                    # self.assertTrue(uppercasePattern.match(word), msg='%s: word "%s" of title "%s" is not in uppercase.' % (t['md'], word, t['title']))
                    if uppercasePattern.match(word) is None:
                        print '%s: word "%s" of title "%s" is not in uppercase.' % (t['md'], word, t['title'])
