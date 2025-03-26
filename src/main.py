from copy_static import copy_static_to_public, generate_pages_recursive
from textnode import TextNode, TextType

def main():
    # This will delete and recreate the public directory
    copy_static_to_public("static", "public")
    
    # Generate pages
    generate_pages_recursive("content", "template.html", "public")

if __name__ == "__main__":
    main()