import unittest
from htmlnode import HTMLNode
from leafnode import LeafNode
class Test_HTML(unittest.TestCase):
	def test_1(self):
		Node1 = HTMLNode("<a>", "blahblahblah", {"href": "https://www.google.com"}, None)
		self.assertEqual(Node1.props_to_html(), ' href="https://www.google.com"')
	def test_extract_markdown_images(self):
	    matches = HTMLNode.extract_markdown_images(
	        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
	    )
	    self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
	def test_extract_markdown_links(self):
	    matches = HTMLNode.extract_markdown_links(
	        "This is text with an [image](https://i.imgur.com/zjjcJKZ.png)"
	    )
	    self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
	def test_leaf_to_html_p(self):
	    node = LeafNode("p", "Hello, world!")
	    self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
	def test_leaf_to_html_a(self):
	    node = LeafNode("a", "this is a link", {"href": "https://www.google.com"})
	    self.assertEqual(node.to_html(), '<a href="https://www.google.com">this is a link</a>')
	def test_leaf_to_html_b(self):
	    node = LeafNode("b", "Hello, world!")
	    self.assertEqual(node.to_html(), "<b>Hello, world!</b>")
if __name__ == "__main__":
    unittest.main()