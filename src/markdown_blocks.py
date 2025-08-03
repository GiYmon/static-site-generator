from block_type import BlockType
from inline_markdown import text_to_textnodes
from nodes.htmlnode import HTMLNode
from nodes.parentnode import ParentNode
from nodes.textnode import TextNode
from nodes.texttype import TextType
from nodes.leaf_node_factory import create_leaf_node


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
    
def markdown_to_html_node(markdown: str) -> HTMLNode:
    blocks = markdown_to_blocks(markdown)
    child_nodes = []

    for block in blocks:
        html_node = block_to_html_node(block)
        child_nodes.append(html_node)

    return ParentNode(
        tag="div",
        children=child_nodes,
        props=None,
    )

def block_to_html_node(block: str) -> HTMLNode:
    block_type = block_to_block_type(block)

    match block_type:
        case BlockType.PARAGRAPH:
            return paragraph_to_html_node(block)
        case BlockType.HEADING:
            return heading_to_html_node(block)
        case BlockType.CODE:
            return code_to_html_node(block)
        case BlockType.QUOTE:
            return quote_to_html_node(block)
        case BlockType.UNORDERED_LIST:
            return unordered_list_to_html_node(block)
        case BlockType.ORDERED_LIST:
            return ordered_list_to_html_node(block)
        case _:
            raise ValueError("invalid block type")
        
def text_to_children(text: str) -> list[HTMLNode]:
    text_nodes = text_to_textnodes(text)
    children = []
    
    for text_node in text_nodes:
        html_node = create_leaf_node(text_node)
        children.append(html_node)

    return children

def paragraph_to_html_node(block: str) -> HTMLNode:
    lines = block.split("\n")
    children = text_to_children(" ".join(lines))
    return ParentNode(
        tag="p",
        children=children
    )

def heading_to_html_node(block: str) -> HTMLNode:
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break
    if level + 1 >= len(block):
        raise ValueError(f"invalid heading level: {level}")
    text = block[level + 1 :]
    children = text_to_children(text)
    return ParentNode(f"h{level}", children)


def code_to_html_node(block: str) -> HTMLNode:
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("invalid code block")
    text = block[4:-3]
    raw_text_node = TextNode(text, TextType.TEXT)
    child = create_leaf_node(raw_text_node)
    code = ParentNode("code", [child])
    return ParentNode("pre", [code])


def ordered_list_to_html_node(block: str) -> HTMLNode:
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[3:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)


def unordered_list_to_html_node(block: str) -> HTMLNode:
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)


def quote_to_html_node(block: str) -> HTMLNode:
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("invalid quote block")
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)
