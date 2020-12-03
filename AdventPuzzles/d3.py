import os

inputs = open(os.getcwd() + '/inputs/d3.txt', 'r') 
lines = inputs.readlines()

def pattern(x, y):
	cx, cy, hits = 0, 0 ,0
	for yIndex, line in enumerate(lines):
		line = line.strip('\n') * 100 
		if yIndex == 0:
			cx += x
			continue	
		elif cy + y == yIndex:	
			if line[cx] == '#':
				hits += 1
		else:
			continue

		cx += x
		cy += y
	return hits

print('Part 1:', pattern(3,1))

p2 = pattern(1,1) * pattern(3,1) * pattern(5,1) *	pattern(7,1) * pattern(1,2)

print('Part 2:', p2)
