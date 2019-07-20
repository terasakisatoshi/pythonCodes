import clr
import System
from System import IO

print("hello")
sr=IO.StreamReader("helloiron.py")
data=sr.ReadToEnd()
sr.Close()

print(data)


