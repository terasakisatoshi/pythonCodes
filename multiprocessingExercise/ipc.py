"""
reference
http://momijiame.tumblr.com/post/20221894597/python-%E3%81%AE-multiprocessing-%E3%83%A2%E3%82%B8%E3%83%A5%E3%83%BC%E3%83%AB%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%9F%E3%83%97%E3%83%AD%E3%82%BB%E3%82%B9%E9%96%93%E9%80%9A%E4%BF%A1-ipc
"""

import os
import time 
import multiprocessing
import random

class Daemon():
	def __init__(self,nproc):
		self.nproc=nproc
		self.queue=multiprocessing.Queue()

	def start(self):
		for i in range(self.nproc):
			p=multiprocessing.Process(
				target=self._child_main_loop,
				args=(self.queue,)
			)
			
			p.daemon=True
			p.start()
		self._parent_main_loop()

	def _parent_main_loop(self):
		while True:
			print (self.queue.get())

	def _child_main_loop(self,queue):
		items=["A","B","C"]
		while True:
			item=items[random.randrange(0,len(items))]
			price=random.randrange(2000,10000)
			queue.put((item,price,os.getpid()))
			time.sleep(1)

def main():
	nproc=3
	daemon=Daemon(nproc)
	daemon.start()

if __name__ == '__main__':
	main()