import os 
import subprocess

def run_openssl(data):
	env=os.environ.copy()
	env['password']=u'\\xe24U\\n\\xd0Ql3S\\x11'
	proc=subprocess.Popen(
		['openssl enc -des3 -pass env:password'],
		shell=True,
		env=env,
		stdin=subprocess.PIPE,
		stdout=subprocess.PIPE
	)
	
	proc.stdin.write(data)
	proc.stdin.flush()
	return proc

procs=[]
for _ in range(3):
	data=os.urandom(10)
	proc=run_openssl(data)
	procs.append(proc)

for proc in procs:
	out, err = proc.communicate()
	print(out[-10:])

