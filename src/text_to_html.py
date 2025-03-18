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
    

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    if not delimiter:
        return old_nodes

    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
        split_text = node.text.split(delimiter)

        for index, part in enumerate(split_text):
            if index % 2 == 0:
                new_nodes.append(TextNode(part, TextType.TEXT))
            else: 
                new_nodes.append(TextNode(part, text_type))
    print(new_nodes)
    return new_nodes