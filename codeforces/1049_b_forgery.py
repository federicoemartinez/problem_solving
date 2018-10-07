# Problem: http://codeforces.com/problemset/problem/1059/B

def possible_strokes(x,y, n, m):
	return [z for z in [(x,y), (x-1,y), (x-2,y), (x,y-1), (x,y-2), (x-1,y-2), (x-2,y-2), (x-2, y-1)] if z[0] >= 0 and z[1] >= 0 and z[0] + 2 < n and z[1] + 2 < m]

def is_valid_stroke(upper_left_x, upper_left_y, grid):
	for x in range(3):
		for y in range(3):
			if x == y: continue
			if not grid[upper_left_x + x][upper_left_y + y]: return False
	return True

def can_be_painted(x,y,grid):
	for each in possible_strokes(x,y, len(grid), len(grid[0])):
			if is_valid_stroke(each[0], each[1], grid):
				return True
	return False


def can_paint_grid(grid):
	for x in range(len(grid)):
		for y in range(len(grid[x])):
			if grid[x][y] and not can_be_painted(x,y,grid):
				return False
	return True

import fileinput

first = True
y = 0
grid = None
for line in fileinput.input():
    if first:
    	first = False
    	n,m = line.split(' ')
    	grid = [[False for l in range(int(n))] for j in range(int(m))]
    else:
    	x = 0
    	for cell in line:
    		
    		if cell == '\n': continue
    		grid[x][y] = cell != '.'
    		x += 1
    	y+=1

if can_paint_grid(grid):
    print 'YES'
else:
	print 'NO'
