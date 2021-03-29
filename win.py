from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from random import randint
import codecs

# The base window
class WindowApp(App):

	# Lable Text
	def making_label_text(self):
		file = open("var.txt", "r")
		file_to_open = file.read()
		file.close()

		# Countries and capitals
		if file_to_open == "c-s":
			file = codecs.open( "country-sity.txt", "r", "utf_8_sig" )

		labeles = file.read().split("\n")
		self.label = labeles[randint(0, len(labeles)-1)]

	# Closing window
	def end_callback(self, instance):
		self.stop()

	# Builder
	def build(self):

		# To make lable text from file
		self.making_label_text()

		# Making button 
		but = Button(size_hint = [.1,.1], on_release = self.end_callback)		
		end_button = AnchorLayout(anchor_x = "right", anchor_y = "bottom")
		end_button.add_widget(but)

		# Making text 
		text = Label(text = self.label, font_size = 10)
		text_layout = AnchorLayout()
		text_layout.add_widget(text)

		# Returning in one window
		returner = AnchorLayout()
		returner.add_widget(text_layout)
		returner.add_widget(end_button)

		return returner
