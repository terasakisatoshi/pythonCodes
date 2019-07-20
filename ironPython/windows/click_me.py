import clr 

"""
create button its label is ClickMe
its action is showing MessageBox 
"""

clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Drawing")

from System.Windows.Forms import Application, Form, Button, Label, MessageBox
from System import Drawing

def on_button_clicked(sender,eventargs):
    print("Hello")
    MessageBox.Show("Hi Welcome to ironPython")

class Myform(Form):
    def __init__(self):
        self.Text="HelloIronPython"
        self.button=Button()
        self.button.Text="ClickMe"
        self.Controls.Add(self.button)
        self.button.Top=(self.ClientSize.Height-self.button.Height)/2
        self.button.Left=(self.ClientSize.Width-self.button.Width)/2

        self.label=Label()
        self.label.Top=(self.ClientSize.Height-self.label.Height)/3
        self.label.Left=(self.ClientSize.Width-self.label.Width)/3
        self.label.Text="Please Click it "
        self.Controls.Add(self.label)

def main():
    myform=Myform()
    Application.Run(myform)

def create_form():
    f=Form()
    f.Text="HelloIronPython"

    btn=Button()
    btn.Text="ClickMe"

    f.Controls.Add(btn)

    btn.Top=(f.ClientSize.Height-btn.Height)/2
    btn.Left=(f.ClientSize.Width-btn.Width)/2

    Application.Run(f)

if __name__ == '__main__':
    main()