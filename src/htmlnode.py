import re
class HTMLNode():
	def __init__(self, tag=None, value=None, props=None, children=None):
		self.tag = tag
		self.value = value
		self.children = children
		self.props = props

	def to_html(self):
		raise NotImplementedError

	def props_to_html(self):
		return_string = f""
		if self.props != None:
			for key in self.props:
				return_string += f' {key}="{self.props[key]}"'
		return return_string
	def __repr__(self):
		return f"self.tag = {self.tag}, self.value = {self.value}, self.children = {self.children}, self.props = {self.props}"
	def extract_markdown_images(text):
		return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
	def extract_markdown_links(text):
		return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)