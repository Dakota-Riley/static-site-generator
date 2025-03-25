import unittest

from copy_static import extract_title

class TestCopyStatic(unittest.TestCase):
    def test_first_line_Title(self):
        markdown = "# Title"
        title = extract_title(markdown)
        self.assertEqual("Title", title)

    def test_title_after_first_line(self):
        markdown = """
        ## This is a subtitle

        # This is the Title
        """
        title = extract_title(markdown)
        self.assertEqual("This is the Title", title)
    def test_multiple_titles(self):
        markdown = """
        # This is Title 1
        # This is Title 2
        """
        title = extract_title(markdown)
        self.assertEqual("This is Title 1", title)

if __name__ == "__main__":
    unittest.main()

