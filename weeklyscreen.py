from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image

from kivy.uix.screenmanager import Screen


class Weekly_Screen(Screen):
    """Class that handles the screen containing all the widgets for the daily maps"""

    def __init__(self, **kwargs):
        super(Weekly_Screen, self).__init__(**kwargs)

        # // button used to switch to hourly maps
        hourly_button = Button(text='hourly')
        hourly_button.bind(on_press=self.hourly_button_callback)

        self.add_widget(WeeklyPage(hourly_button))

    def hourly_button_callback(self, instance) -> None:
        """Change current screen to hourly maps"""

        # // self.manager is screenmanager when called in a Screen class
        self.manager.current = 'hourly'


class WeeklyPage(BoxLayout):
    """Class containing all the widgets that make up the daily maps"""

    def __init__(self, hourly_button, **kwargs) -> None:
        super(WeeklyPage, self).__init__(**kwargs)

        self.hourly_button = hourly_button

        # // set orientation that the layout should go in
        self.orientation = 'vertical'

        # // Layout that contains widget to go to hourly maps
        self.other_pages_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.0725))

        self.other_pages_layout.add_widget(Label(text='', size_hint=(1.5, 1)))
        self.other_pages_layout.add_widget(self.hourly_button)
        self.other_pages_layout.add_widget(Label(text='', size_hint=(1.5, 1)))

        self.add_widget(self.other_pages_layout)

        # // layout containing maps of the 4 next days
        self.maps_layout = GridLayout(rows=2, cols=2)

        self.maps_layout.add_widget(Image(source=r'./pollen_maps_weekly/pollenmap_weekly_0.png'))
        self.maps_layout.add_widget(Image(source=r'./pollen_maps_weekly/pollenmap_weekly_2.png'))
        self.maps_layout.add_widget(Image(source=r'./pollen_maps_weekly/pollenmap_weekly_3.png'))
        self.maps_layout.add_widget(Image(source=r'./pollen_maps_weekly/pollenmap_weekly_4.png'))

        self.add_widget(self.maps_layout)
