from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.behaviors.focus import FocusBehavior
from kivy.uix.button import Button
from kivy.uix.label import Label

class FocusLabel(FocusBehavior, Label):
  pass




class MyApp(App):

    def build(self):
        grid = GridLayout(cols=4)
        for i in range(40):
            focus_obj=FocusLabel(text=str(i))
            if i ==1:
                focus_obj.focus=True
            grid.add_widget(focus_obj)
        return grid

def main():
    MyApp().run()
if __name__ == '__main__':
    main()
