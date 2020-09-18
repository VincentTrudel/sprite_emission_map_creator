from PIL import Image
import numpy as np

from tkinter.filedialog import askopenfilename
filename = askopenfilename(filetypes=[("PNG","*.png")])
from copy import deepcopy
import re

arr = np.array(Image.open(filename))

print("Please enter RGB values of color to change")

red =-1
green = -1
blue = -1

colors = []
inp = None
while inp !="c":
	inp = input("Add another color (c to continue):\n").rstrip()
	invalid = True
	if inp == "c":
		break
	try:
		color = [int(x) for x in inp.split(" ")]
		for x in color:
			if x > 255 or x < 0:
				raise "Invalid color"
		colors.append(color)
	except Exception as e:
		print(e)
		print("Invalid color")

	

height = len(arr)
width = len(arr[0])
i=1
for col in colors:
	arr1 = deepcopy(arr)
	for r in range(height):
		for c in range(width):
			if np.array_equal(arr1[r][c][0:3], [col[0],col[1],col[2]]):
				arr1[r][c] = [255,255,255,255]
			else:
				arr1[r][c] = [0,0,0,255]

	filename1 = filename.replace(".png", "_Emission"+str(i)+".png")			
	Image.fromarray(arr1).save( filename1, "PNG")
	print(filename1 + " saved!")
	i+=1



