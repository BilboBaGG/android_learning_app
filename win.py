from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from random import randint
import codecs

from kivy.core.window import Window
Window.clearcolor = (1, .97 , .86 , 1)

# The base window
class WindowApp(App):
	

	# Lable Text
	def making_label_text(self):
		file = open("var.txt", "r")
		file_to_open = file.read()
		file.close()

		# Countries and capitals
		if file_to_open == "country_city":
			file = codecs.open( "country-sity.txt", "r", "utf_8_sig")

		labeles = file.read().split("\n")
		self.label = labeles[randint(0, len(labeles)-1)]

	# Closing window
	def end_callback(self, instance):
		self.stop()

	def color_making(self, instance):
		instance.background_color = (1, .97 , .86 , 1)

	# Builder
	def build(self):

		# To make lable text from file
		self.making_label_text()

		# Making button 
		but = Button(size_hint = [1,.2], background_color = [1, .97 , .86 , 1], background_normal = '', color = (.13, .07, .01, 1), on_release = self.end_callback, text="Выучил!",)		
		end_button = AnchorLayout(anchor_x = "right", anchor_y = "bottom")
		end_button.add_widget(but)

		# Making text 
		text = Label(text = self.label, font_size = 50, color = (.13, .07, .01, 1))
		text_layout = AnchorLayout()
		text_layout.add_widget(text)

		# Returning in one window
		returner = AnchorLayout()
		returner.add_widget(text_layout)
		returner.add_widget(end_button)

		return returner
