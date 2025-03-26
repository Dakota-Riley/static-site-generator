import os
import shutil

from markdown_blocks import (
    markdown_to_blocks,
    markdown_to_html_node,
    BlockType
)

from htmlnode import HTMLNode

def copy_static_to_public(source_path, destination_path, is_root_call=True):
    # Print what we're currently processing
    print(f"Processing: {source_path}")

    # Only delete and recreate the destination at the top level
    if is_root_call:
        print(f"Starting copy from {source_path} to {destination_path}")
        if os.path.exists(destination_path):
            shutil.rmtree(destination_path)
        os.makedirs(destination_path)
    else:
        print(f"Processing subdirectory: {source_path}")

    # List all items in the source directory
    items = os.listdir(source_path)

    for item in items:
        # Build full paths
        source_item_path = os.path.join(source_path, item)
        dest_item_path = os.path.join(destination_path, item)
        # If it's a directory, recursively process it
        if os.path.isdir(source_item_path):
            # Make sure the destination directory exists
            if not os.path.exists(dest_item_path):
                os.mkdir(dest_item_path)
            # Recursive call for subdirectory
            copy_static_to_public(source_item_path, dest_item_path, False)
        # If it's a file, process it according to your needs
        elif os.path.isfile(source_item_path):
            print(f"Found file: {source_item_path}")
            # Here you would do something with the file
            # For example: shutil.copy(source_item_path, dest_item_path)
            shutil.copy(source_item_path, dest_item_path)

def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        lines = block.split("\n")
        for line in lines:
            if line.startswith("# "):
                # Remove the "# " and strip any leading/trailing whitespace
                return line[2:].strip()
    raise Exception("No H1 header found in the markdown")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}.")

    # Read the markdown file
    with open(from_path, mode="r") as file:
        markdown = file.read()
        file.close()
    
    # Read the template file
    with open(template_path, mode="r") as file:
        template = file.read()
        file.close()
    
    # Convert markdown to HTML
    content = markdown_to_html_node(markdown).to_html()

    # Extract title
    title = extract_title(markdown)

    # Replace placeholders 
    final_html = template.replace("{{ Title }}", title).replace("{{ Content }}", content)

    # Create directory if it doesn't exist
    directory = os.path.dirname(dest_path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)

    # Write the final HTML to the destination
    with open(dest_path, "w") as file:
        file.write(final_html)
        file.close()

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    directory_items = os.listdir(dir_path_content)
    for item in os.listdir(dir_path_content):
        print(f"Directory Item: {item}")

        source_path = os.path.join(dir_path_content, item)
        dest_path = os.path.join(dest_dir_path, item)
        print(f"Source Path: {source_path}")
        print(f"Destination Path: {dest_path}")

        # Check item to see if it is a file
        if os.path.isfile(source_path):
            print(f"{item} is a file")
            final_html = dest_path.replace(".md", ".html")

            generate_page(source_path, template_path, final_html)
            print("Page Generated")
        
        if os.path.isdir(source_path):
            print(f"{item} is a directory")
            generate_pages_recursive(source_path, template_path, dest_path)
            print("New Subdirectory Generated")


if __name__ == "__main__":
    # This will delete and recreate the public directory
    copy_static_to_public("static", "public")
    
    # Generate pages
    generate_pages_recursive("content", "template.html", "public")

