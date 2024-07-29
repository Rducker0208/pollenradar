from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label


class Hourly_Screen(Screen):
    """Class that handles the screen containing all the widgets used to display the hourly maps"""

    def __init__(self, **kwargs) -> None:
        super(Hourly_Screen, self).__init__(**kwargs)

        # // button used to switch to weekly maps
        weekly_button = Button(background_normal=r'./images/this_week.png')
        weekly_button.bind(on_press=self.weekly_button_callback)

        self.add_widget(HourlyPage(weekly_button))

    def weekly_button_callback(self, instance) -> None:
        """Change current screen to weekly maps"""

        # // self.manager is screenmanager when called in a Screen class
        self.manager.current = 'weekly'


class HourlyPage(BoxLayout):
    """Class containing all the widgets that make up the hourly maps"""

    def __init__(self, weekly_button, **kwargs) -> None:
        super(HourlyPage, self).__init__(**kwargs)
        self.weekly_button = weekly_button

        self.polmap = Pollenmap()

        # // set orientation that the layout should go in
        self.orientation = 'vertical'

        # // Layout that contains widget to go to weekly maps
        self.weekly_button_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.45))

        self.weekly_button_layout.add_widget(Label(text='', size_hint=(.4, 1)))
        self.weekly_button_layout.add_widget(self.weekly_button)
        self.weekly_button_layout.add_widget(Label(text='', size_hint=(.4, 1)))

        self.add_widget(self.weekly_button_layout)

        # // layout containing pollenmap, see Pollenmap class for more information
        self.add_widget(self.polmap)

        # // layout containing buttons to switch between maps, see pollenmap.next/last_image for more info
        self.add_widget(Pagebuttons(self.polmap))

        # // layout containing a legend for the pollenmap
        self.add_widget(Image(source=r'./images/pollenlegenda.png', size_hint=(1, 0.6)))


class Pollenmap(Image):
    """Class containing buienradar's pollenmap and the functions used to switch between hours"""

    def __init__(self, **kwargs) -> None:
        super(Pollenmap, self).__init__(**kwargs)

        self.source = r'./pollen_maps_daily/pollenmap_0.png'
        self.size_hint = (1, 3)
        self.pos_hint = {'x': 0, 'top': 0}

        self.current_image = 0

    def next_image(self, instance) -> None:
        """Function to get the card portraying the next hour compared to the current"""

        if self.current_image == 23:
            self.current_image = 0
        else:
            self.current_image += 1

        self.source = rf'./pollen_maps_daily/pollenmap_{self.current_image}.png'

    def last_image(self, instance) -> None:
        """Function to get the card portraying the last hour compared to the current"""

        if self.current_image == 0:
            self.current_image = 23
        else:
            self.current_image -= 1

        self.source = rf'./pollen_maps_daily/pollenmap_{self.current_image}.png'


class Pagebuttons(BoxLayout):
    """Class that contains 2 buttons, next and last, used to switch between hourly maps"""

    def __init__(self, polmap, **kwargs):
        super(Pagebuttons, self).__init__(**kwargs)
        self.orientation = 'horizontal'
        self.size_hint = (1, 0.5)

        self.polmap = polmap

        last_page_button = Button(background_normal=r'./images/arrow_left.png',
                                  background_down=r'./images/arrow_left.png',
                                  size_hint=(1, 1))

        last_page_button.bind(on_press=self.polmap.last_image)

        next_page_button = Button(background_normal=r'./images/arrow_right.png',
                                  background_down=r'./images/arrow_right.png',
                                  size_hint=(1, 1))

        next_page_button.bind(on_press=self.polmap.next_image)

        self.add_widget(Label())
        self.add_widget(last_page_button)
        self.add_widget(Label(size_hint=(1.5, 1)))
        self.add_widget(next_page_button)
        self.add_widget(Label())
