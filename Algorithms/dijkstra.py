import pygame
import math

def min_dijkstra(Q, grid):
    	
	t_min1 = -1
	t_min2 = -1
	min_value = math.inf
	
	for rows in grid:
		for spot in rows:
			if spot.isVisited[0] == 0 and spot.distance < min_value:
				t_min1 = spot.row
				t_min2 = spot.col
				min_value = spot.distance

	return (t_min1, t_min2)		

def draw_dijkstra(draw, grid, end):

	if end.previous[0] != (-1) and end.previous[1] != (-1):
		grid[end.previous[0]][end.previous[1]].make_path()
		draw()
		draw_dijkstra(draw, grid, grid[end.previous[0]][end.previous[1]])

def dijkstra(draw, grid, start, end):
	
	Q = []

	for rows in grid:
		for spot in rows:
			t = (spot.row, spot.col)
			Q.append(t)

	grid[start.row][start.col].distance = 0

	while len(Q) > 0:
		u = min_dijkstra(Q, grid)

		if(u[0] == end.row and u[1] == end.col):
			draw_dijkstra(draw, grid, end)
			return
		#print(u)
		#print(Q)
		Q.remove(u)
		grid[u[0]][u[1]].isVisited[0] = 1
		#print("Ajunge aici macar o data")
		grid[u[0]][u[1]].make_closed()

		if(grid[u[0]][u[1]].distance == math.inf):
    		
			return

		for neighbor in grid[u[0]][u[1]].neighbors:
			alt = grid[u[0]][u[1]].distance + 1
			if alt < neighbor.distance:
				neighbor.distance = alt
				neighbor.previous = [u[0],u[1]]
				neighbor.make_open()
				draw()