import unittest

from text_to_html import text_node_to_html_node, split_nodes_delimiter
from textnode import TextNode, TextType

class TestTextToHTMLFunc(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold node")

    def test_italics(self):
        node = TextNode("This is a italics node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is a italics node")
    
    def test_bold(self):
        node = TextNode("This is a code node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a code node")

    def test_link(self):
        node = TextNode("This is a link node", TextType.LINK, url="https://www.google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link node")
        self.assertEqual(html_node.props["href"], "https://www.google.com")

    def test_image(self):
        node = TextNode("This is an image node", TextType.IMAGE, url="https://www.google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props["src"], "https://www.google.com")
        self.assertEqual(html_node.props["alt"], "This is an image node")

class SplitNodesDelimiterFunc(unittest.TestCase):

    def test_text(self):
        test_node_1 = TextNode("Hello world, ", TextType.TEXT)
        test_node_2 = TextNode("My name is Dakota!", TextType.TEXT)
        new_nodes = split_nodes_delimiter([test_node_1, test_node_2], "", TextType.TEXT)
        self.assertEqual(new_nodes, [TextNode("Hello world, ", TextType.TEXT), TextNode("My name is Dakota!", TextType.TEXT)]) 

    def test_bold(self):
        test_node_1 = TextNode("Hello **world**, ", TextType.BOLD)
        test_node_2 = TextNode("My name is **Dakota**!", TextType.BOLD)
        new_nodes = split_nodes_delimiter([test_node_1, test_node_2], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [TextNode("Hello **world**, ", TextType.BOLD), TextNode("My name is **Dakota**!", TextType.BOLD)]) 

    def test_italics(self):
        test_node_1 = TextNode("Hello _world_, ", TextType.ITALIC)
        test_node_2 = TextNode("My name is _Dakota_!", TextType.ITALIC)
        new_nodes = split_nodes_delimiter([test_node_1, test_node_2], "", TextType.ITALIC)
        self.assertEqual(new_nodes, [TextNode("Hello _world_, ", TextType.ITALIC), TextNode("My name is _Dakota_!", TextType.ITALIC)]) 

    def test_code(self):
        test_node_1 = TextNode("Hello `world`, ", TextType.CODE)
        test_node_2 = TextNode("My name is `Dakota`!", TextType.CODE)
        new_nodes = split_nodes_delimiter([test_node_1, test_node_2], "`", TextType.CODE)
        self.assertEqual(new_nodes, [TextNode("Hello `world`, ", TextType.CODE), TextNode("My name is `Dakota`!", TextType.CODE)]) 

if __name__ == "__main__":
    unittest.main()