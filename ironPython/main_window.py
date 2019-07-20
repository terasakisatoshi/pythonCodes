# -*- coding: UTF-8 -*-
 
import clr
 
clr.AddReferenceByPartialName("PresentationCore")
clr.AddReferenceByPartialName("PresentationFramework")
clr.AddReferenceByPartialName("WindowsBase")
 
from System import *
from System.Windows import *
from System.Windows.Controls import *
from System.Windows.Media.Imaging import *
 
class PicViewWindow(Window):
    def __init__(self):
        self.Title = "PicView"
        self.Drop += self.on_drop
        self.AllowDrop = True
        self.Width = 300
        self.Height = 300
        self.image = Image()
        self.Content = self.image
 
    def on_drop(self, sender, e):
        filename = e.Data.GetData(DataFormats.FileDrop)[0].ToString()
        self.image.Source = BitmapImage(Uri(filename))
 
def main():
    Application().Run(PicViewWindow())
 
if __name__ == "__main__":
    main()