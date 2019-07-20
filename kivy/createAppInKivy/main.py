from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

class AddLocationForm(BoxLayout):
    search_input=ObjectProperty()
    def send_message(self):
        msg=self.search_input.text
        self.record_message(msg)

    def record_message(self,msg):
        self.search_results.item_strings.append(msg)


class WeatherApp(App):
    pass

if __name__ == '__main__':
    WeatherApp().run()