from itertools import product
import numpy as np
import z3
from z3solver import Z3Solver
from kivy.app import App
from kivy.uix.button import Label, Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.boxlayout import BoxLayout


class MainGrid(FocusBehavior, GridLayout):

    def __init__(self, **kwargs):
        super(MainGrid, self).__init__(**kwargs)
        self.shift_down = False

    def keyboard_on_key_down(self, window, keycode, text, modifiers):
        """Based on FocusBehavior that provides automatic keyboard
        access, key presses will be used to select children.
        """
        if 'shift' in keycode[1]:
            self.shift_down = True

    def keyboard_on_key_up(self, window, keycode):
        """Based on FocusBehavior that provides automatic keyboard
        access, key release will be used to select children.
        """
        if 'shift' in keycode[1]:
            self.shift_down = False

    def add_widget(self, widget):
        """ Override the adding of widgets so we can bind and catch their
        *on_touch_down* events. """
        widget.bind(on_touch_down=self.button_touch_down)
        return super(MainGrid, self).add_widget(widget)

    def button_touch_down(self, button, touch):
        """ Use collision detection to select buttons when the touch occurs
        within their area. """
        if button.collide_point(*touch.pos):
            self.update_button_text(button)

    def update_button_text(self, button):
        if self.shift_down:
            button.countdown()
        else:
            button.countup()


class CustomButton(Button):
    DIC = {0: "*", 1: "1", 2: "2", 3: "3", 4: "4",
           5: "5", 6: "6", 7: "7", 8: "8", 9: "9"}

    def __init__(self, **kwargs):
        super(CustomButton, self).__init__(**kwargs)
        self.counter = 0
        self.text = CustomButton.DIC[0]

    def countup(self):
        self.counter = (self.counter+1) % 10
        self.text = CustomButton.DIC[self.counter]

    def countdown(self):
        self.counter = (self.counter-1) % 10
        self.text = CustomButton.DIC[self.counter]


class SudokuApp(App):

    def on_start(self):
        main_grid = self.root.ids.main_grid
        for (k, l) in product(range(9), repeat=2):
            main_grid.add_widget(CustomButton(
                id="v_{}_{}".format(str(k), str(l))))

    def solve(self):
        grid = lambda i, j: z3.Int("grid[%d,%d]" % (i, j))
        print("Start to solve")
        children = self.root.ids.main_grid.children
        problem = [[0]*9 for _ in range(9)]
        for child in children:
            i, j = child.id.split("_")[1:]
            i, j = int(i), int(j)
            if child.text.isnumeric():
                problem[i][j] = int(child.text)
            else:
                problem[i][j] = 0
        solver = Z3Solver(problem)
        result = solver.solve()
        if result == z3.sat:
            model = solver.model()
            for child in children:
                i, j = child.id.split("_")[1:]
                i, j = int(i), int(j)
                child.text = str(model[grid(i, j)])
        else:
            print(result)

    def reset(self):
        print("Reset")
        children = self.root.ids.main_grid.children
        for child in children:
            child.text = "*"


def main():
    SudokuApp().run()


if __name__ == '__main__':
    main()
