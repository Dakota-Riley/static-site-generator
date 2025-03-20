import re

from textnode import TextNode, TextType

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

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        images = extract_markdown_images(node.text)
        if not images:
            new_nodes.append(node)
            continue
        current_text = node.text
        for image_alt, image_link in images:
            # Split around the image markdown
            parts = current_text.split(f"![{image_alt}]({image_link})", 1)
            # Add text before the image if not empty
            if parts[0]:
                new_nodes.append(TextNode(parts[0], TextType.TEXT))
            # Add the image node
            new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_link))
            # Update current_text to be the text after the image
            if len(parts) > 1:
                current_text = parts[1]
            else:
                current_text = ""
        # Add any remaining text
        if current_text:
            new_nodes.append(TextNode(current_text, TextType.TEXT))
    return new_nodes

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

def extract_markdown_images(text):
    image = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return image

def extract_markdown_links(text):
    link = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return link