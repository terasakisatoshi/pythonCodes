import os
import subprocess

file = "some_file.txt"
with open(file, 'w') as opened_file:
    opened_file.write('Hola!')

subprocess.run(["cat", file])

if os.path.exists(file):
    os.remove(file)
assert not os.path.exists(file)
