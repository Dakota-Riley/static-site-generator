from htmlnode import LeafNode
from textnode import TextNode, TextType

def text_node_to_html_node(text_node):
    if text_node.text_type not in TextType:
        raise Exception("Not a valid Text Type")
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)
    if text_node.text_type == TextType.BOLD:
        return LeafNode("b" , text_node.text)
    if text_node.text_type == TextType.ITALIC:
        return LeafNode("i" , text_node.text)
    if text_node.text_type == TextType.CODE:
        return LeafNode("code" , text_node.text)
    if text_node.text_type == TextType.LINK:
        return LeafNode("a" , text_node.text, {"href": text_node.url})
    if text_node.text_type == TextType.IMAGE:
        return LeafNode("img" , "", {"src": text_node.url, "alt" : text_node.text})
