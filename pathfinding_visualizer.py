import pygame
import math
import sys
sys.path.append(".")
import time
from Helper.global_variables import *
from Helper.button_helper import Button
from Helper.text_helper import drawText, drawTextcenter
from Grid.node import Node
from Grid.grid import make_grid, draw_grid, draw, get_clicked_pos
from Algorithms.bfs import bfs
from Algorithms.dfs import dfs
from Algorithms.dijkstra import dijkstra
from Algorithms.bidirectional_bfs import bidirectional_bfs
from Algorithms.best_first_search import best_first_search
from Algorithms.a_star import astar

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pathfinding Algorithm Visualizer")
pygame.init()

def main(win, width):
	
	grid = make_grid(ROWS, width)
	all_fonts = pygame.font.get_fonts()

	start = None
	end = None
	ALG_ID = 0
	start_time = 0
	elapsed_time = 0
	number_of_visited_nodes = 0

	run = True
	while run:
		
		#print(ALG_ID)
		
		draw(win, grid, ROWS, width, ALG_ID, elapsed_time)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

			if button_astar.check() == True and ALG_ID != 0:
				button_astar.background_color = LIGHT_BUTTON
			else:
				button_astar.background_color = DARK_BUTTON

			if button_bfs.check() == True and ALG_ID != 1:
				button_bfs.background_color = LIGHT_BUTTON
			else:
				button_bfs.background_color = DARK_BUTTON

			if button_bidirectional.check() == True and ALG_ID != 2:
				button_bidirectional.background_color = LIGHT_BUTTON
			else:
				button_bidirectional.background_color = DARK_BUTTON
	
			if button_dijkstra.check() == True and ALG_ID != 3:
				button_dijkstra.background_color = LIGHT_BUTTON
			else:
				button_dijkstra.background_color = DARK_BUTTON

			if button_dfs.check() == True and ALG_ID != 4:
				button_dfs.background_color = LIGHT_BUTTON
			else:
				button_dfs.background_color = DARK_BUTTON

			if button_best_first_search.check() == True and ALG_ID != 5:
				button_best_first_search.background_color = LIGHT_BUTTON
			else:
				button_best_first_search.background_color = DARK_BUTTON

			if button_reset.check() == True:
				button_reset.background_color = LIGHT_BUTTON
			else:
				button_reset.background_color = DARK_BUTTON

			if pygame.mouse.get_pressed()[0]: # LEFT
				pos = pygame.mouse.get_pos()
				row, col = get_clicked_pos(pos, ROWS, width)
				if row < ROWS and col < ROWS:
					spot = grid[row][col]
					if not start and spot != end:
						start = spot
						start.isStart = 1
						start.make_start()

					elif not end and spot != start:
						end = spot
						end.isEnd = 1
						end.make_end()

					elif spot != end and spot != start:
						spot.make_barrier()
				elif button_reset.check() == True:
					start = None
					end = None
					grid = make_grid(ROWS, width)
					start_time = 0
					elapsed_time = 0
					number_of_visited_nodes = 0

				if button_start.check() == True and start and end:
    					
					for row in grid:
						for spot in row:
							spot.update_neighbors(grid)

					temp_start = start
					temp_end = end
					#start_time = 0
					#elapsed_time = 0
					if(ALG_ID == 0):
						start_time = time.time()
						astar(lambda: draw(win, grid, ROWS, width, ALG_ID, 0), grid, start, end)
						elapsed_time = time.time() - start_time
					if(ALG_ID == 1):
						start_time = time.time()
						bfs(lambda: draw(win, grid, ROWS, width, ALG_ID, 0), grid, start, end)
						elapsed_time = time.time() - start_time
					if(ALG_ID == 2):
						start_time = time.time()
						bidirectional_bfs(lambda: draw(win, grid, ROWS, width, ALG_ID, 0), grid, start, end)
						elapsed_time = time.time() - start_time
					if(ALG_ID == 3):
						start_time = time.time()
						dijkstra(lambda: draw(win, grid, ROWS, width, ALG_ID, 0), grid, start, end)
						elapsed_time = time.time() - start_time
					if(ALG_ID == 4):
						start_time = time.time()
						path = []
						visited = []
						dfs(lambda: draw(win, grid, ROWS, width, ALG_ID, 0), grid, start, end, path, visited)
						elapsed_time = time.time() - start_time
					if(ALG_ID == 5):
						start_time = time.time()
						best_first_search(lambda: draw(win, grid, ROWS, width, ALG_ID, 0), grid, start, end)
						elapsed_time = time.time() - start_time

					temp_start.make_start()
					temp_end.make_end()
					#draw(win, grid, ROWS, WIDTH, ALG_ID, elapsed_time)

				if button_astar.check() == True:
					button_astar.background_color = TEAL
					ALG_ID = 0
				else:
					button_astar.background_color = DARK_BUTTON

				if button_bfs.check() == True:
					button_bfs.background_color = TEAL
					ALG_ID = 1
				else:
					button_bfs.background_color = DARK_BUTTON

				if button_bidirectional.check() == True:
					button_bidirectional.background_color = TEAL
					ALG_ID = 2
				else:
					button_bidirectional.background_color = DARK_BUTTON
	
				if button_dijkstra.check() == True:
					button_dijkstra.background_color = TEAL
					ALG_ID = 3
				else:
					button_dijkstra.background_color = DARK_BUTTON

				if button_dfs.check() == True:
					button_dfs.background_color = TEAL
					ALG_ID = 4
				else:
					button_dfs.background_color = DARK_BUTTON

				if button_best_first_search.check() == True:
					button_best_first_search.background_color = TEAL
					ALG_ID = 5
				else:
					button_best_first_search.background_color = DARK_BUTTON

			elif pygame.mouse.get_pressed()[2]: # RIGHT
				pos = pygame.mouse.get_pos()
				row, col = get_clicked_pos(pos, ROWS, width)
				if row < ROWS and col < ROWS:
					spot = grid[row][col]
					spot.reset()
					if spot == start:
						spot.isStart = -1
						start = None
					elif spot == end:
						spot.isEnd = -1
						end = None

			if event.type == pygame.KEYDOWN:

				if event.key == pygame.K_ESCAPE:
					pygame.quit()
	#pygame.quit()

main(WIN, WIDTH)