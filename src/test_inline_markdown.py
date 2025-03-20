import unittest
from inline_markdown import (
    split_nodes_delimiter,
    split_nodes_image,
    split_nodes_link,
    text_to_textnodes,
    extract_markdown_links,
    extract_markdown_images,
)

from textnode import TextNode, TextType

class TestInlineMarkdown(unittest.TestCase):
    def test_delim_text(self):
        test_node_1 = TextNode("Hello world, ", TextType.TEXT)
        test_node_2 = TextNode("My name is Dakota!", TextType.TEXT)
        new_nodes = split_nodes_delimiter([test_node_1, test_node_2], "", TextType.TEXT)
        self.assertEqual(new_nodes, [TextNode("Hello world, ", TextType.TEXT), TextNode("My name is Dakota!", TextType.TEXT)]) 

    def test_delim_bold(self):
        test_node_1 = TextNode("Hello **world**, ", TextType.BOLD)
        test_node_2 = TextNode("My name is **Dakota**!", TextType.BOLD)
        new_nodes = split_nodes_delimiter([test_node_1, test_node_2], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [TextNode("Hello **world**, ", TextType.BOLD), TextNode("My name is **Dakota**!", TextType.BOLD)]) 

    def test_delim_italics(self):
        test_node_1 = TextNode("Hello _world_, ", TextType.ITALIC)
        test_node_2 = TextNode("My name is _Dakota_!", TextType.ITALIC)
        new_nodes = split_nodes_delimiter([test_node_1, test_node_2], "", TextType.ITALIC)
        self.assertEqual(new_nodes, [TextNode("Hello _world_, ", TextType.ITALIC), TextNode("My name is _Dakota_!", TextType.ITALIC)]) 

    def test_delim_code(self):
        test_node_1 = TextNode("Hello `world`, ", TextType.CODE)
        test_node_2 = TextNode("My name is `Dakota`!", TextType.CODE)
        new_nodes = split_nodes_delimiter([test_node_1, test_node_2], "`", TextType.CODE)
        self.assertEqual(new_nodes, [TextNode("Hello `world`, ", TextType.CODE), TextNode("My name is `Dakota`!", TextType.CODE)]) 

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text that goes [to boot.dev](https://www.boot.dev)"
        )
        self.assertListEqual([("to boot.dev", "https://www.boot.dev")], matches)

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with an [image](https://i.imgur.com/zjjcJKZ.png) and another [second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.LINK, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_text_to_textnodes_1(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
            nodes
        )


    def test_text_to_textnodes_2(self):
        text = "**This is bold text** with some _italic words_ and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("This is bold text", TextType.BOLD),
                TextNode(" with some ", TextType.TEXT),
                TextNode("italic words", TextType.ITALIC),
                TextNode(" and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
            nodes
        )

    
        
if __name__ == "__main__":
    unittest.main()