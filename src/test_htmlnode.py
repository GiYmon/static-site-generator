import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_init(self):
        node = HTMLNode("div", "Hello, World!", [], {"class": "greeting"})
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "Hello, World!")
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, {"class": "greeting"})

    def test_repr(self):
        node = HTMLNode("span", "Text", [{"tag": "b"}], {"style": "color: red;"})
        expected_repr = "HTMLNode('span', 'Text', [{'tag': 'b'}], {'style': 'color: red;'})"
        self.assertEqual(repr(node), expected_repr)

    def test_props_to_html(self):
        node = HTMLNode("a", "Link", [], {"href": "https://example.com", "target": "_blank"})
        expected_html = 'href="https://example.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected_html)

    def test_props_to_html_no_props(self):
        node = HTMLNode("p", "Paragraph")
        self.assertEqual(node.props_to_html(), "")


if __name__ == "__main__":
    unittest.main()