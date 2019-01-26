#!/usr/bin/python
import matplotlib.pyplot as plt
def transform(track, handle):
	arr = []
	with open(track, "r") as f:
		next(f)
		for line in f:
			curv = float(line.strip())
			if curv != -1.0:
				vmax = (handle * curv/1000000)**0.5
			else:
				vmax = 1000
			arr.append(vmax)
	x = [i for i in range(1000)]		
	plt.plot(x, arr)
	#print(len(arr))

transform('track_1.csv', 12)
