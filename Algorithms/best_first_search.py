import pygame
from queue import PriorityQueue

def color_best(draw, grid, path):
	for node in path:
		grid[node[0]][node[1]].make_path()
		draw()

def h_best(node, end):

	x1 = node.row
	y1 = node.col
	x2 = end.row
	y2 = end.col
	return abs(x1 - x2) + abs(y1 - y2)

def best_first_search(draw, grid, start, end):

	path = []
	pqueue = PriorityQueue()
	t = (start.row, start.col)
	q = (h_best(start,end), t)
	pqueue.put(q)

	while pqueue:
		#print(pqueue)
		u = pqueue.get()
		#print(u)
		t = u[1]
		grid[t[0]][t[1]].make_closed()
		path.append(t)

		if grid[t[0]][t[1]] == end:
			color_best(draw, grid, path)
			return
		else:
			for neighbor in grid[t[0]][t[1]].neighbors:
				if neighbor.isVisited[0] == 0:
					neighbor.isVisited[0] = 1
					t = (neighbor.row,neighbor.col)
					q = (h_best(neighbor, end), t)
					pqueue.put(q)
			grid[t[0]][t[1]].make_open()
			grid[t[0]][t[1]].isVisited[0] = 1