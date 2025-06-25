# 45colorname.py by Kassidy

import sys
import math

colorfile = sys.argv[1]
R = int(sys.argv[2])
G = int(sys.argv[3])
B = int(sys.argv[4])

min = math.sqrt(3 * 255**2) # initialize as the maximum distance possible

with open(colorfile) as fp:
	for line in fp:
		column = line.split()
		color_rgb = column[2].split(',') # obtain the color's rgb values
		r_diff = abs(R - int(color_rgb[0]))
		g_diff = abs(G - int(color_rgb[1]))
		b_diff = abs(B - int(color_rgb[2]))
		eudist = math.sqrt(r_diff**2 + g_diff**2 + b_diff**2)
		if eudist < min:      # using Euclidean distance, compare against min
			min = eudist      # update if lower
			color = column[0] # the closest color is now first column value

print(color) # display final color with lowest Euclidean distance