from textnode import TextNode, TextType
from extract_markdown_links import extract_markdown_links

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        links = extract_markdown_links(node.text)

        if not links:
            new_nodes.append(node)
            continue

        current_text = node.text

        for link_text, link_href in links:
            # Split around the link markdown
            parts = current_text.split(f"[{link_text}]({link_href})", 1)

            # Add text before the link if not empty
            if parts[0]:
                new_nodes.append(TextNode(parts[0], TextType.TEXT))

            # Add the link node
            new_nodes.append(TextNode(link_text, TextType.LINK, link_href))

            # Update current_text to be the text after the link
            if len(parts) > 1:
                current_text = parts[1]
            else:
                current_text = ""

        # Add any remaining text
        if current_text:
            new_nodes.append(TextNode(current_text, TextType.TEXT))
                
    return new_nodes