import unittest

from split_nodes_delimiter import split_nodes_delimiter
from textnode import TextNode, TextType

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