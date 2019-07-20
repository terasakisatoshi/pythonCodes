#!/usr/bin/ipy

import clr

clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Drawing")

from System.Windows.Forms import Application, Form
from System.Windows.Forms import Button, ToolTip
from System.Drawing import Point, Size

class IForm(Form):

    def __init__(self):
        self.Text = 'Tooltips'
        self.CenterToScreen()
        xsize,ysize=300,200
        self.Size = Size(xsize, ysize)

        tooltip = ToolTip()
        tooltip.SetToolTip(self, "This is a Form")

        button = Button()
        button.Parent = self
        button.Text = "Button"
        xloc,yloc=50,70
        button.Location = Point(xloc,yloc)

        tooltip.SetToolTip(button, "This is a Button")

def main():
    form=IForm()
    Application.Run(form)
if __name__ == '__main__':
    main()
