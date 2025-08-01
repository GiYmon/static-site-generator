import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq_different_text(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a different text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_not_eq_different_type(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_not_eq_different_url(self):
        node = TextNode("This is a text node", TextType.BOLD, url="https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.BOLD, url="https://www.example.com")
        self.assertNotEqual(node, node2)

    def test_not_eq_with_none_url(self):
        node = TextNode("This is a text node", TextType.BOLD, url="https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.BOLD, url="https://www.boot.dev")
        expected_repr = "TextNode('This is a text node', 'bold', 'https://www.boot.dev')"
        self.assertEqual(repr(node), expected_repr)
if __name__ == "__main__":
    unittest.main()
