import re

from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block):
    block_lines = block.split("\n")

    # Heading check
    if bool(re.match(r'^#{1,6} ', block_lines[0])):
        return BlockType.HEADING
    
    # Code block check
    if block_lines[0] == "```" and block_lines[-1] == "```":
        return BlockType.CODE
    
    # Quote block check - every line must start with >
    all_lines_are_quotes = True
    for line in block_lines:
        if not line.startswith(">"):
            all_lines_are_quotes = False
            break
    if all_lines_are_quotes:
        return BlockType.QUOTE
    
    # Unordered list check - every line must start with - followed by space
    all_lines_are_unordered = True
    for line in block_lines:
        if not line.startswith("- "):
            all_lines_are_unordered = False
            break
    if all_lines_are_unordered:
        return BlockType.UNORDERED_LIST
    
    # Unordered list check - every line must start with a number followed by space
    all_lines_are_ordered = True
    expected_number = 1

    for line in block_lines:
        if not line.startswith(f"{expected_number}. "):
            all_lines_are_ordered = False
            break
        expected_number += 1
    if all_lines_are_ordered:
        return BlockType.ORDERED_LIST
    
    return BlockType.PARAGRAPH
