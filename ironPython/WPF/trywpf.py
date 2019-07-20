import clr
import sys
sys.path.append("C:\Program Files (x86)\IronPython 2.7\Tutorial")
from avalon import *

w = Window()

w.Title = "WPF by ironPython"

w.Content = Button()
w.Content.Content = "ClickME"
w.Content.FontSize = 50
w.SizeToContent = SizeToContent.WidthAndHeight
w.Show()
