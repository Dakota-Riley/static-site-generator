from textnode import TextNode, TextType
from extract_markdown_images import extract_markdown_images

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


        