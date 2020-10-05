import pygame

def color_bfs_path(path, grid, draw):
    	
	for node in path:
		grid[node[0]][node[1]].make_path()
		draw()

def bfs(draw, grid, start, end):
	
	queue = []
	t = (start.row, start.col)
	queue.append([t])

	while queue:
    	
		path = []
		path = queue.pop(0)
		node = path[-1]

		grid[node[0]][node[1]].isVisited[0] = 1;

		grid[node[0]][node[1]].make_closed()

		if grid[node[0]][node[1]] == end:    			
			color_bfs_path(path, grid, draw)
			return
		
		for adjacent in grid[node[0]][node[1]].neighbors:
    			
			if (grid[adjacent.row][adjacent.col]).isVisited[0] == 0:
    				
				adjacent.make_open()
				new_path = list(path)
				t = (adjacent.row, adjacent.col)
				new_path.append(t)
				queue.append(new_path)
				grid[adjacent.row][adjacent.col].isVisited[0] = 1
				draw()