def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")

    stripped_blocks = []
    stripped_lines = []
    for block in blocks:
        block_lines = block.split("\n")
        for line in block_lines:
            stripped_line = line.strip()
            if stripped_line:
                stripped_lines.append(stripped_line)
        stripped_blocks.append("\n".join(stripped_lines))
        stripped_lines = []

    return stripped_blocks
