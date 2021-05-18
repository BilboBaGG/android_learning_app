from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.core.window import Window

Window.clearcolor = (1, .97 , .86 , 1)

class MainApp(App):

	def vibor(self, instance):
		
		a = str(instance.text)
		
		for i in range(8):
			self.massiv[i].text = "0"
			if a == self.arr[i]:
				self.massiv[i].text = "1"

	def build(self):

		self.arr = ["География","Английский язык","Математика","Информатика","Русский язык","Физика","*","№","Главный экран"]
		self.i = 0
			
		self.gl_layout = GridLayout (cols = 2,spacing = 5, size_hint = (1, .75))

		self.gl_layout1 = GridLayout(cols = 1, spacing = 16, size_hint = (.82, 1))
		
		self.gl_layout1.add_widget (Button (text = "География", background_color = (.91, .77, .5, 1), background_normal = '' , color = (.13, .07, .01, 1), on_release = self.vibor))
		self.gl_layout1.add_widget (Button (text = "Английский язык", background_color = (.91, .77, .5, 1), background_normal = '', color = (.13, .07, .01, 1),on_release = self.vibor))
		self.gl_layout1.add_widget (Button (text = "Математика", background_color = (.91, .77, .5, 1), background_normal = '', color = (.13, .07, .01, 1),on_release = self.vibor))
		self.gl_layout1.add_widget (Button (text = "Информатика", background_color = (.91, .77, .5, 1), background_normal = '', color = (.13, .07, .01, 1),on_release = self.vibor))
		self.gl_layout1.add_widget (Button (text = "Русский язык", background_color = (.91, .77, .5, 1), background_normal = '', color = (.13, .07, .01, 1),on_release = self.vibor))
		self.gl_layout1.add_widget (Button (text = "Физика", background_color = (.91, .77, .5, 1), background_normal = '', color = (.13, .07, .01, 1),on_release = self.vibor))
		self.gl_layout1.add_widget (Button (text = "*", background_color = (.91, .77, .5, 1), background_normal = '', color = (.13, .07, .01, 1),on_release = self.vibor))
		self.gl_layout1.add_widget (Button (text = "№", background_color = (.91, .77, .5, 1), background_normal = '', color = (.13, .07, .01, 1),on_release = self.vibor))

		self.gl_layout2 = GridLayout (cols = 1, spacing = 16, size_hint = (.15, 1))
			
		self.massiv = [Label(text = "0", font_size = 40, color = (.13, .07, .01, 1)) for _ in range(8)]
		for i in range(8):
			self.gl_layout2.add_widget(self.massiv[i])

		self.gl_layout.add_widget(self.gl_layout1)
		self.gl_layout.add_widget(self.gl_layout2)
		
		self.lb = Label (text = "ADRON", color = (.13, .07, .01, 1), font_size = 50, size_hint = (1, .1))

		self.bl_layout = BoxLayout (size_hint = (1, .07), spacing = 16)
		self.bl_layout.add_widget (Button (text = "назад", background_color = (.91, .77, .5, 1), background_normal = '', color = (.13, .07, .01, 1)))
		self.bl_layout.add_widget (Button (text= "вперёд", background_color = (.91, .77, .5, 1), background_normal = '', color = (.13, .07, .01, 1)))

		self.vse = BoxLayout(orientation = "vertical", padding = 20,spacing = 10)
		self.vse.add_widget(self.lb)
		self.vse.add_widget(self.gl_layout)
		self.vse.add_widget(self.bl_layout)
		
		return self.vse

if __name__ == "__main__":
	MainApp().run()