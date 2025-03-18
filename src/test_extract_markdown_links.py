import unittest

from extract_markdown_links import extract_markdown_links

class ExtractMarkdownLinksFunc(unittest.TestCase):
    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text that goes [to boot.dev](https://www.boot.dev)"
        )
        self.assertListEqual([("to boot.dev", "https://www.boot.dev")], matches)

if __name__ == "__main__":
    unittest.main()