import unittest
from nodes.parentnode import ParentNode
from nodes.leafnode import LeafNode


class TestParentNode(unittest.TestCase):
    def test_init(self):
        node = ParentNode("div", [], {"class": "container"})
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, {"class": "container"})

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_no_children(self):
        parent_node = ParentNode("div", [])
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_to_html_many_children(self):
        child1 = LeafNode("p", "First child")
        child2 = LeafNode("p", "Second child")
        parent_node = ParentNode("div", [child1, child2])
        expected_html = "<div><p>First child</p><p>Second child</p></div>"
        self.assertEqual(parent_node.to_html(), expected_html)

    def test_headings(self):
        child1 = LeafNode("h1", "Heading")
        child2 = LeafNode("h2", "Subheading")
        parent_node = ParentNode("section", [child1, child2])
        expected_html = "<section><h1>Heading</h1><h2>Subheading</h2></section>"
        self.assertEqual(parent_node.to_html(), expected_html)
    
    def test_to_html_with_props(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node], {"class": "container"})
        self.assertEqual(
            parent_node.to_html(),
            '<div class="container"><span>child</span></div>'
        )

    def test_repr(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node], {"class": "container"})
        expected_repr = "ParentNode('div', [LeafNode('span', 'child', None)], {'class': 'container'})"
        self.assertEqual(repr(parent_node), expected_repr)

if __name__ == "__main__":
    unittest.main()
    