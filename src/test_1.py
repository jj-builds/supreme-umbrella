import unittest
from textnode import Textnode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = Textnode("This is a text node", TextType.BOLD)
        node2 = Textnode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = Textnode("This is a text node", TextType.BOLD)
        node2 = Textnode("This is a test node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_not_eq2(self):
        node = Textnode("This is a text node", TextType.BOLD)
        node2 = Textnode("This is a test node", TextType.BOLD)
        self.assertFalse(node.__eq__(node2))

    def test_eq2(self):
        node = Textnode("This is a text node", TextType.BOLD)
        node2 = Textnode("This is a text node", TextType.BOLD)
        self.assertTrue(node.__eq__(node2))

    def test_repr(self):
        node = Textnode("This is a text node", TextType.BOLD)
        self.assertMultiLineEqual("TextNode(This is a text node, bold text, None)", node.__repr__())

if __name__ == "__main__":
    unittest.main()