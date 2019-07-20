import clr 
clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Drawing")

from System import TimeSpan, DateTime
from System.Windows.Forms import Application, Form, Label, Timer,Button
from System.Windows.Forms import FormStartPosition
from System.Drawing import Font, FontStyle, Point, Size

class App(Form):
    def __init__(self):
        self.Title="Timer"
        self.timer1=Timer()
        self.timer1.Interval=1000
        self.timer1.Tick+=self.timer1_tick
        label1=Label()
        label1.AutoSize=True
        label1.Location=Point(41,22)
        label1.Text="00:00:00"
        label1.Font=Font("MS UI Gothic",24.0,FontStyle.Regular)
        self.label1=label1
        self.Controls.Add(self.label1)

        clientwidth=255

        b1=Button()
        b1.Location=Point((clientwidth-b1.Width*2)/3,68)
        b1.Text="Click"
        b1.Click+=self.start_Click
        self.Controls.Add(b1)

        b2=Button()
        b2.Location=Point((clientwidth-b1.Width*2)*2/3+b1.Width,68)
        b2.Text="Stop"

        b2.Click+=self.stop_Click
        self.Controls.Add(b2)
        self.ClientSize=Size(clientwidth,103)
        self.Text="Stop Watch"
        self.StartPosition=FormStartPosition.CenterScreen

    def timer1_tick(self,sender,e):
        self.starttime=self.starttime+TimeSpan(0,0,1)
        self.label1.Text=self.starttime.ToString()

    def start_Click(self,sender,e):
        self.starttime=TimeSpan(0,0,0)
        self.label1.Text=self.starttime.ToString()
        self.timer1.Start()

    def stop_Click(self,sender,e):
        self.timer1.Stop()

def main():
    app=App()
    Application.Run(app)

if __name__ == '__main__':
    main()