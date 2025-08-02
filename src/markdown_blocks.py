


def markdown_to_blocks(markdown: str) -> list[str]:
    raw_blocks = markdown.strip().split("\n\n")
    blocks = []
    for block in raw_blocks:
        lines = [line.strip() for line in block.splitlines() if line.strip() != ""]
        if lines:
            blocks.append("\n".join(lines))
    return blocks