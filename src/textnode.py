from enum import Enum

class TextType(Enum):
	TEXT = "text"
	BOLD = "bold text"
	ITALIC = "italic text"
	CODE = "code text"
	LINK = "link"
	IMAGE = "image"

class Textnode:
	def __init__(self, my_text, Texttype, my_url=None):
		self.text_type = Texttype
		self.text = my_text
		self.url = my_url

	def __eq__(self, other):
		if self.text_type == other.text_type and self.text == other.text and self.url == other.url:
			return True
		return False

	def __repr__(self):
		return f"TextNode({self.text}, {self.text_type.value}, {self.url})"