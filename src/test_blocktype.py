import unittest

from blocktype import block_to_block_type, BlockType

class TestBlockToBlockType(unittest.TestCase):
    def test_heading(self):
        block = "## This is a Heading"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.HEADING)

    def test_code(self):
        block = "```\nThis is a code block\n```"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.CODE)

    def test_quote(self):
        block = "> This \n> is> a\n> quote."
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.QUOTE)

    def test_unordered_list(self):
        block = """- This\n- is\n- an\n- unordered\n- list."""
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.UNORDERED_LIST)

    def test_ordered_list(self):
        block = """1. This\n2. is\n3. an\n4. ordered\n5. list."""
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.ORDERED_LIST)

    def test_paragraph(self):
        block = "This is a paragraph."
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)


if __name__ == "__main__":
    unittest.main()
