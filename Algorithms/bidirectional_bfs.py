import pygame
from Algorithms.bfs import color_bfs_path

def bidirectional_bfs(draw, grid, start, end):
	
	queue1 = []
	queue2 = []
	t1 = (start.row, start.col)
	t2 = (end.row, end.col)
	queue1.append([t1])
	queue2.append([t2])

	while queue1 and queue2:
    		
			path1 = []
			path2 = []
			path1 = queue1.pop(0)
			path2 = queue2.pop(0)
			node1 = path1[-1]
			node2 = path2[-1]

			grid[node1[0]][node1[1]].isVisited[0] = 1
			grid[node1[0]][node1[1]].make_closed()

			grid[node2[0]][node2[1]].isVisited[1] = 1
			grid[node2[0]][node2[1]].make_closed()
			
			aux1 = grid[node1[0]][node1[1]].isVisited[1]
			aux2 = grid[node2[0]][node2[1]].isVisited[0]

			if aux1 == 1 or aux2 == 1 or (node1[0] == node2[0] and node1[1] == node2[1]):
				#x.make_barrier()
				if aux1 == 1:
    									
					while queue2:
						
						path2 = queue2.pop(0)
						node = path2[-1]
						if node[0] == node1[0] and node[1] == node1[1]:
							path2.reverse()
							path = path1 + path2
							color_bfs_path(path, grid, draw)
							return
				
				if aux2 == 1:
    					
					while queue1:

						path1 = queue1.pop(0)
						node = path1[-1]
						if node[0] == node2[0] and node[1] == node2[1]:
							path1.reverse()
							path = path2 + path1
							color_bfs_path(path, grid, draw)	
							return

			for adjacent in grid[node1[0]][node1[1]].neighbors:
    			
				if (grid[adjacent.row][adjacent.col]).isVisited[0] == 0:
						
					adjacent.make_open()
					new_path = list(path1)
					t = (adjacent.row, adjacent.col)
					new_path.append(t)
					queue1.append(new_path)
					grid[adjacent.row][adjacent.col].isVisited[0] = 1
					draw()

			for adjacent in grid[node2[0]][node2[1]].neighbors:
    			
				if (grid[adjacent.row][adjacent.col]).isVisited[1] == 0:
						
					adjacent.make_open()
					new_path = list(path2)
					t = (adjacent.row, adjacent.col)
					new_path.append(t)
					queue2.append(new_path)
					grid[adjacent.row][adjacent.col].isVisited[1] = 1
					draw()