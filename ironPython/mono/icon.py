#!/usr/bin/ipy

import clr
import sys

clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Drawing")

from System.Windows.Forms import Application, Form
from System.Drawing import Icon

class IForm(Form):

    def __init__(self):
        self.Text = 'Icon'
        self.Width = 250
        self.Height = 200
        
        #try:
        #    self.Icon = Icon("web.ico")
        #except Exception, e:
        #    print e
        #    sys.exit(1)       
        
        self.CenterToScreen()

Application.Run(IForm())