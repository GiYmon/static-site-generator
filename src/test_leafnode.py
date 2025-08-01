import unittest
from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_init(self):
        node = LeafNode("p", "This is a leaf node", {"class": "leaf"})
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "This is a leaf node")
        self.assertIsNone(node.children)
        self.assertEqual(node.props, {"class": "leaf"})

    def test_to_html_span(self):
        node = LeafNode("span", "Leaf content", {"style": "color: blue;"})
        expected_html = '<span style="color: blue;">Leaf content</span>'
        self.assertEqual(node.to_html(), expected_html)

    def test_to_html_a(self):
        node = LeafNode("a", "Click here", {"href": "https://example.com"})
        expected_html = '<a href="https://example.com">Click here</a>'
        self.assertEqual(node.to_html(), expected_html)

    def test_repr(self):
        node = LeafNode("h1", "Heading", {"id": "main-heading"})
        expected_repr = "LeafNode('h1', 'Heading', {'id': 'main-heading'})"
        self.assertEqual(repr(node), expected_repr)

    def test_to_html_no_value(self):
        node = LeafNode("div", None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Just text")
        expected_html = "Just text"
        self.assertEqual(node.to_html(), expected_html)

if __name__ == "__main__":
    unittest.main()