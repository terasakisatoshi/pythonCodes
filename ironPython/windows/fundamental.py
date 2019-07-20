import clr 

clr.AddReference("System.Windows.Forms")

from System.Windows.Forms import Application, Form

def main():
    f=Form()
    f.Text="HelloIronPython"
    Application.Run(f)
if __name__ == '__main__':
    main()