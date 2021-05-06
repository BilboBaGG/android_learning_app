from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class MainApp(App):

	def making_mainscreen(self,instance):

		self.vse.clear_widgets()
		self.gl_layout.clear_widgets()
		self.gl_layout1.clear_widgets()
		self.gl_layout2.clear_widgets()
		self.bl_layout.clear_widgets()
	
		self.gl_layout1.add_widget (Button (text = "География", on_release = self.making_stranica))
		self.gl_layout1.add_widget (Button (text = "Английский язык", on_release = self.making_stranica))
		self.gl_layout1.add_widget (Button (text = "Математика", on_release = self.making_stranica))
		self.gl_layout1.add_widget (Button (text = "Информатика", on_release = self.making_stranica))
		self.gl_layout1.add_widget (Button (text = "Русский язык", on_release = self.making_stranica))
		self.gl_layout1.add_widget (Button (text = "Физика", on_release = self.making_stranica))
		self.gl_layout1.add_widget (Button (text = "*", on_release = self.making_stranica))
		self.gl_layout1.add_widget (Button (text = "№", on_release = self.making_stranica))
		
		self.gl_layout2.add_widget(Label(text = "0"))
		self.gl_layout2.add_widget(Label(text = "0"))
		self.gl_layout2.add_widget(Label(text = "0"))
		self.gl_layout2.add_widget(Label(text = "0"))
		self.gl_layout2.add_widget(Label(text = "0"))
		self.gl_layout2.add_widget(Label(text = "0"))
		self.gl_layout2.add_widget(Label(text = "0"))
		self.gl_layout2.add_widget(Label(text = "0"))

		self.gl_layout.add_widget(self.gl_layout1)
		self.gl_layout.add_widget(self.gl_layout2)
		
		self.lb = Label (text = "ADRON", font_size = 30, size_hint = (1, .07))

		self.bl_layout.add_widget (Button (text = "left"))
		self.bl_layout.add_widget (Button (text= "right"))

		self.vse.add_widget(self.lb)
		self.vse.add_widget(self.gl_layout)
		self.vse.add_widget(self.bl_layout)

	def making_stranica(self, instance):
		
		a = str(instance.text)
		for self.i in range(len(self.arr)): 
			if a == self.arr[self.i]:
				self.stranica = self.i
		
		self.vse.clear_widgets()
		self.bl_layout.clear_widgets()
		

		self.gl_layout3 = GridLayout (cols = 1,spacing = 5, size_hint = (1, .75))

		self.gl_layout3.add_widget(Button(text = "1"))
		self.gl_layout3.add_widget(Button(text = "2"))
		self.gl_layout3.add_widget(Button(text = "3"))
		self.gl_layout3.add_widget(Button(text = "4"))
		self.gl_layout3.add_widget(Button(text = "5"))
		self.gl_layout3.add_widget(Button(text = "6"))
		self.gl_layout3.add_widget(Button(text = "7"))
		self.gl_layout3.add_widget(Button(text = "8"))

		self.bl_layout.add_widget(Button(text ="Главный экран", on_release = self.making_mainscreen))

		self.lb = Label(text = self.arr[self.stranica], font_size = 30, size_hint = (1, .07))

		self.vse.add_widget(self.lb)
		self.vse.add_widget(self.gl_layout3)
		self.vse.add_widget(self.bl_layout)

	def build(self):

		self.arr = ["Главный экран","География","Английский язык","Математика","Информатика","Русский язык","Физика","*","№"]
		self.i = 0
			
		self.gl_layout = GridLayout (cols = 2,spacing = 5, size_hint = (1, .75))

		self.gl_layout1 = GridLayout(cols = 1, spacing = 5, size_hint = (.92, 1))
		
		self.gl_layout1.add_widget (Button (text = "География", on_release = self.making_stranica))
		self.gl_layout1.add_widget (Button (text = "Английский язык", on_release = self.making_stranica))
		self.gl_layout1.add_widget (Button (text = "Математика", on_release = self.making_stranica))
		self.gl_layout1.add_widget (Button (text = "Информатика", on_release = self.making_stranica))
		self.gl_layout1.add_widget (Button (text = "Русский язык", on_release = self.making_stranica))
		self.gl_layout1.add_widget (Button (text = "Физика", on_release = self.making_stranica))
		self.gl_layout1.add_widget (Button (text = "*", on_release = self.making_stranica))
		self.gl_layout1.add_widget (Button (text = "№", on_release = self.making_stranica))

		self.gl_layout2 = GridLayout (cols = 1, spacing = 5, size_hint = (.05, 1))
		
		self.gl_layout2.add_widget(Label(text = "0"))
		self.gl_layout2.add_widget(Label(text = "0"))
		self.gl_layout2.add_widget(Label(text = "0"))
		self.gl_layout2.add_widget(Label(text = "0"))
		self.gl_layout2.add_widget(Label(text = "0"))
		self.gl_layout2.add_widget(Label(text = "0"))
		self.gl_layout2.add_widget(Label(text = "0"))
		self.gl_layout2.add_widget(Label(text = "0"))

		self.gl_layout.add_widget(self.gl_layout1)
		self.gl_layout.add_widget(self.gl_layout2)
		
		self.lb = Label (text = "ADRON", font_size = 30, size_hint = (1, .07))

		self.bl_layout = BoxLayout (size_hint = (1, .1), spacing = 5)
		self.bl_layout.add_widget (Button (text = "left"))
		self.bl_layout.add_widget (Button (text= "right"))

		self.vse = BoxLayout(orientation = "vertical", padding = 20,spacing = 10)
		self.vse.add_widget(self.lb)
		self.vse.add_widget(self.gl_layout)
		self.vse.add_widget(self.bl_layout)
		
		return self.vse

if __name__ == "__main__":
	MainApp().run()