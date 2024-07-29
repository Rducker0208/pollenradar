import kivy
import download_images

from hourlyscreen import Hourly_Screen
from weeklyscreen import Weekly_Screen

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, NoTransition
from kivy.core.window import Window

kivy.require('2.3.0')


class Pollenapp(App):
    def __init__(self, **kwargs):
        super(Pollenapp, self).__init__(**kwargs)

        # // Screen manager is used to switch between different screens
        self.sm = ScreenManager(transition=NoTransition())

    def build(self) -> ScreenManager:
        Window.clearcolor = (1, 1, .9, .9)

        self.sm.add_widget(Hourly_Screen(name='hourly'))
        self.sm.add_widget(Weekly_Screen(name='weekly'))
        self.sm.current = 'weekly'

        return self.sm


if __name__ == '__main__':
    download_images.check_last_login()
    Pollenapp().run()
