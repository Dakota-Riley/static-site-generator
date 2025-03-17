import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):

    # Tests for the HTMLNode

    def test_props_to_html_empty(self):
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), "")
    
    def test_props_to_html_single(self):
        node = HTMLNode(props={"href": "https://www.google.com"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com"')

    def test_props_to_html_multiple(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})

        possible_results = [
            ' href="https://www.google.com" target="_blank"',
            ' target="_blank" href="https://www.google.com"'
        ]
        self.assertIn(node.props_to_html(), possible_results)

    # Tests for the LeafNode
    
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_h1(self):
        node = LeafNode("h1", "Hello, world!")
        self.assertEqual(node.to_html(), "<h1>Hello, world!</h1>")

    def test_leaf_to_html_b(self):
        node = LeafNode("b", "Hello, world!")
        self.assertEqual(node.to_html(), "<b>Hello, world!</b>")

    def test_leaf_to_html_i(self):
        node = LeafNode("i", "Hello, world!")
        self.assertEqual(node.to_html(), "<i>Hello, world!</i>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Hello, world!")
        self.assertEqual(node.to_html(), "<a>Hello, world!</a>")

    # Tests for the ParentNode

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_empty_tag(self):
        child_node = LeafNode("div", "child")
        parent_node = ParentNode("", [child_node])
        with self.assertRaises(ValueError) as context:
            parent_node.to_html()
        self.assertEqual(str(context.exception), "Parent node must have a non-empty tag.")

    def test_to_html_with_no_child(self):
        child_node = LeafNode("div", "child")
        parent_node = ParentNode("span", "")
        with self.assertRaises(ValueError) as context:
            parent_node.to_html()
        self.assertEqual(str(context.exception), "Parent node must have non-empty children.")

if __name__ == "__main__":
    unittest.main()
