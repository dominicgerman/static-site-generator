import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("a", "Hi Mom!", None, {"href": "https://dominicgerman.com", "target": "_blank"})
        output = node.props_to_html()
        expecting = " href=\"https://dominicgerman.com\" target=\"_blank\""
        self.assertEqual(output, expecting)
    
class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode("a", "Hi Mom!", {"href": "https://dominicgerman.com", "target": "_blank"})
        output = node.to_html()     
        expecting = "<a href=\"https://dominicgerman.com\" target=\"_blank\">Hi Mom!</a>"
        self.assertEqual(output, expecting)

class TestParentNode(unittest.TestCase):
    def test_with_children(self):
        child_node = LeafNode("strong", "fuck you")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><strong>fuck you</strong></div>")

    def test_with_grandchildren(self):
        first_grandchild_node = LeafNode(None, "fuck you")
        second_grandchild_node = LeafNode("em", "bitch")
        child_node = ParentNode("strong", [first_grandchild_node, second_grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><strong>fuck you<em>bitch</em></strong></div>")
        

if __name__ == "__main__":
    unittest.main()

