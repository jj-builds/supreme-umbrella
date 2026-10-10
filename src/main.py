from textnode import *
def main():
	my_thing = Textnode("texT", TextType.TEXT, "onetwothree")
	my_second_thing = my_thing.__repr__()
	print(my_second_thing)
main()