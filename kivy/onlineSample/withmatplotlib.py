import matplotlib
matplotlib.use('module://kivy.garden.matplotlib.backend_kivy')
from kivy.app import App
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvas, NavigationToolbar2Kivy
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

import matplotlib.pyplot as plt
import csv

with open("c:/Users/Niels/Desktop/uranite_23_03_2017.csv", 'rb') as f:
    reader = csv.reader(f, delimiter=';')
    data = []
    for column in reader:
        data.append(column[1])

    results = data
    results = [int(i) for i in results]

bins = 200
plt.hist(results, bins=bins)
plt.title("Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")

fig = plt.gcf()
canvas = fig.canvas

def callback(self):

    global fig, results
    #bins = 50
    plt.hist(results,bins=bins)
    canvas.draw()

class HistogramApp(App):
    title = 'Histogram data'

    def build(self):
        fl = BoxLayout(orientation="vertical")

        self.btn1 = Button(text="Update", height=40, size_hint_y=None)
        self.btn1.bind(on_press=callback)

        self.tekstvak = TextInput(height=30, size_hint_y=None, multiline=False)

        nav1 = NavigationToolbar2Kivy(canvas)

        fl.add_widget(nav1.actionbar)
        fl.add_widget(canvas)
        fl.add_widget(self.tekstvak)
        fl.add_widget(self.btn1)
        return fl

if __name__ == '__main__':
    HistogramApp().run()