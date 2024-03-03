import kivy
from kivy.app import App
from kivy.core.audio import SoundLoader
from kivy.uix.gridlayout import GridLayout

class MainWidget(GridLayout):
    sound1 = SoundLoader.load("yt1s.com - Fart sound effect.mp3")
    sound2 = SoundLoader.load("yt1s.com - MEME SOUND 2.mp3")
    sound3 = SoundLoader.load("yt1s.com - MEMEYeet Sound Effect.mp3")
    sound4 = SoundLoader.load("yt1s.com - root beer no .mp3")
    sound3.volume = 0.3
    sound4.volume = 0.2

class myApp(App):
    def build(self):
        return MainWidget()
 
if __name__ == '__main__':
    myApp().run()
