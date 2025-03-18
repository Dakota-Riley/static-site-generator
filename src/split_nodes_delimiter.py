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

        for i in range(len(split_text)):
            if split_text[i] == "":
                continue  # Skip empty strings

            if i % 2 == 0:
                if split_text[i]:
                    new_nodes.append(TextNode(split_text[i], TextType.TEXT))
            else: 
                new_nodes.append(TextNode(split_text[i], text_type))

    return new_nodes