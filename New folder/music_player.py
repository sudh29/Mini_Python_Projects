from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

import os

os.environ["KIVY_METRICS_DENSITY"] = "2.0"
os.environ["KIVY_GL_BACKEND"] = "angle_sdl2"


class MusicPlayerApp(App):
    def build(self):
        self.root = BoxLayout(orientation="vertical")

        self.label = Label(text="Now Playing: None")
        self.play_button = Button(text="Play", size_hint=(None, None))
        self.play_button.bind(on_release=self.play_music)

        self.root.add_widget(self.label)
        self.root.add_widget(self.play_button)

        return self.root

    def play_music(self, instance):
        self.label.text = "Now Playing: Your Favorite Song"


if __name__ == "__main__":
    MusicPlayerApp().run()
