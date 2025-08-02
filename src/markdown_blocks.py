import re
from block_type import BlockType


def markdown_to_blocks(markdown: str) -> list[str]:
    raw_blocks = markdown.strip().split("\n\n")
    blocks = []
    for block in raw_blocks:
        lines = [line.strip() for line in block.splitlines() if line.strip() != ""]
        if lines:
            blocks.append("\n".join(lines))
    return blocks

def block_to_block_type(block: str) -> BlockType:
    lines = block.splitlines()

    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE
    if all(line.startswith(">") for line in lines):
        return BlockType.QUOTE
    if all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST
    ordered = True
    for idx, line in enumerate(lines):
        if not line.startswith(f"{idx + 1}. "):
            ordered = False
            break
    if ordered and lines:
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH
    