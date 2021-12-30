import os 
import time
os.system('cls')

filename=["file1.txt","file2.txt", "file3.txt","file4.txt", "file5.txt", "file6.txt"]

def animator(filename, delay=1, repeat=0):
	frames=[]
	for name in filename:
		with open(name, "r", encoding="utf-8") as f:
			frames.append(f.readlines())
	for i in range(repeat):
		for frame in frames:
			print("".join(frame))
			time.sleep(1)
			os.system('cls')


animator(filename, delay=0.5, repeat=10)

animator(filename, delay=0.1, repeat=20)

animator(filename, delay=2, repeat=5)