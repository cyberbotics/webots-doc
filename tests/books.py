"""Get the books paths."""
import os


class Books:
    """Helper class to retrieve the book paths."""

    def __init__(self):
        """Constructor. Initialize the properties."""
        self._project_path = os.path.abspath(os.path.join(
            os.path.dirname(os.path.realpath(__file__)), os.pardir))
        # discover the project path
        self._books = []
        self._books_paths = []
        for item in os.listdir(self._project_path):
            path = os.path.join(self._project_path, item)
            if (os.path.isdir(path) and
                    not item.startswith('.') and
                    not item == 'tests'):
                self._books.append(item)
                self._books_paths.append(path)

    @property
    def project_path(self):
        """Hold the path containing the books."""
        return self._project_path

    @property
    def books(self):
        """Hold the book names."""
        return self._books

    @property
    def books_paths(self):
        """Hold the paths to books."""
        return self._books_paths

    def get_md_files(self, book):
        """Retrieve all the MD files of a given book."""
        paths = []
        book_path = os.path.join(self._project_path, book)
        for filename in os.listdir(book_path):
            if not filename.endswith('.md'):
                continue
            path = os.path.join(book_path, filename)
            paths.append(path)
        return paths
