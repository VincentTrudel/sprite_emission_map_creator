from PIL import Image
import numpy as np
#from tkinter.filedialog import askopenfilename
#filename = askopenfilename(filetypes=[("PNG","*.png")])

import re

#arr = np.array(Image.open(filename))

print("Please enter RGB values of color to change")

red =-1
green = -1
blue = -1
p = re.compile("([0-1]+\d+\d|2[0-4][0-9]|2[5][0-5])[\s,;:]{2}\0")
colors = []
inp = None
while inp !="c":
	inp = input("Add another color (c to continue):\n").lower()
	invalid = True
	match = re.match(p, inp)
	
	print(match)
exit()
while not (red > -1 and red < 256):
	red = int(input("R: ").rstrip())
while not (green > -1 and red < 256): 
	green = int(input("G: ").rstrip())
	
while not (blue > -1 and blue < 256):
	blue = int(input("B: ").rstrip())

height = len(arr)
width = len(arr[0])

for r in range(height):
	for c in range(width):
		if np.array_equal(arr[r][c][0:3], [red,green,blue]):
			arr[r][c] = [255,255,255,255]
		else:
			arr[r][c] = [0,0,0,255]
filename = filename.replace(".png", "_Emission.png")			
Image.fromarray(arr).save( filename, "PNG")
print(filename + " saved!")




