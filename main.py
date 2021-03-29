from win import WindowApp
from kivy.config import Config

Config.set('graphics','fullscreen','auto')

if __name__ == "__main__":
	WindowApp().run()