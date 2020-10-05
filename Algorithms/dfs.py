import pygame

def color_dfs_path(path, grid, draw):
	for node in path:
		grid[node[0]][node[1]].make_path()
		draw()

def dfs(draw, grid, start, end, path, visited):
    	
	start_t = (start.row, start.col)
	end_t = (end.row, end.col)

	if start_t in visited:
		return path

	path += [start_t]
	visited += [start_t]

	grid[start_t[0]][start_t[1]].make_closed()

	if start_t == end_t:
    	
		color_dfs_path(path, grid, draw)
		return

	for edge in grid[start_t[0]][start_t[1]].neighbors:
    		
		edge_t = (edge.row, edge.col)

		if edge_t not in visited:		
			grid[edge_t[0]][edge_t[1]].make_open()	
			draw()
			return dfs(draw, grid, edge, end, path, visited)