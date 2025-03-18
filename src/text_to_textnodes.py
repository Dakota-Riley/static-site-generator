from split_nodes_delimiter import split_nodes_delimiter
from split_nodes_image import split_nodes_image
from split_nodes_link import split_nodes_link
from textnode import TextType, TextNode

def text_to_textnodes(text):
    # Start with a single text node
    nodes = [TextNode(text, TextType.TEXT)]

    # Apply each splitting function in sequence
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes
