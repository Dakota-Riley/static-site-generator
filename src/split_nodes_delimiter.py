from textnode import TextNode, TextType

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