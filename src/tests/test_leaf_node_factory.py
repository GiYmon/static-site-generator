import unittest
from nodes.leaf_node_factory import create_leaf_node
from nodes.leafnode import LeafNode
from nodes.textnode import TextNode
from nodes.texttype import TextType


class TestLeafNodeFactory(unittest.TestCase):
    def test_create_leaf_node_text(self):
        text_node = TextNode("Hello, World!", TextType.TEXT)
        leaf_node = create_leaf_node(text_node)
        self.assertEqual(leaf_node.tag, None)
        self.assertEqual(leaf_node.value, "Hello, World!")
        self.assertIsNone(leaf_node.props)

    def test_create_leaf_node_bold(self):
        text_node = TextNode("Bold Text", TextType.BOLD)
        leaf_node = create_leaf_node(text_node)
        self.assertEqual(leaf_node.tag, "b")
        self.assertEqual(leaf_node.value, "Bold Text")
        self.assertIsNone(leaf_node.props)

    def test_create_leaf_node_italic(self):
        text_node = TextNode("Italic Text", TextType.ITALIC)
        leaf_node = create_leaf_node(text_node)
        self.assertEqual(leaf_node.tag, "i")
        self.assertEqual(leaf_node.value, "Italic Text")
        self.assertIsNone(leaf_node.props)

    def test_create_leaf_node_code(self):
        text_node = TextNode("Code Snippet", TextType.CODE)
        leaf_node = create_leaf_node(text_node)
        self.assertEqual(leaf_node.tag, "code")
        self.assertEqual(leaf_node.value, "Code Snippet")
        self.assertIsNone(leaf_node.props)

    def test_create_leaf_node_link(self):
        text_node = TextNode("Link", TextType.LINK, url="http://example.com")
        leaf_node = create_leaf_node(text_node)
        self.assertEqual(leaf_node.tag, "a")
        self.assertEqual(leaf_node.value, "Link")
        self.assertEqual(leaf_node.props, {"href": "http://example.com"})

    def test_create_leaf_node_image(self):
        text_node = TextNode("Image Alt", TextType.IMAGE, url="http://example.com/image.png")
        leaf_node = create_leaf_node(text_node)
        self.assertEqual(leaf_node.tag, "img")
        self.assertIsNone(leaf_node.value)
        self.assertEqual(leaf_node.props, {"src": "http://example.com/image.png", "alt": "Image Alt"})


if __name__ == "__main__":
    unittest.main()