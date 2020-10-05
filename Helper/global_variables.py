from Helper.button_helper import Button

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
TEAL = (0, 128, 128)
PURPLE = (128, 0, 128)
ORANGE = (255, 165 ,0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)
LIGHT_BUTTON = (170, 170, 170)
DARK_BUTTON = (100, 100, 100)

astar_string = ["A* Pathfinding Algorithm", "Weighted -> Yes", "Guarantees shortest path -> Yes", "Worst time complexity -> O(b^d)", "Worst space complexity -> O(b^d)"]
bfs_string = ["Breadth First Search", "Weighted -> No", "Guarantees shortest path -> Yes","Worst time complexity -> O(b^d)", "Worst space complexity -> O(b^d)"]
bidirectional_string = ["Bidirectional BFS", "Weighted -> Yes", "Guarantees shortest path -> No", "Time complexity -> O(b^(d/2))", "Spacial complexity -> O(b^(d/2))"]
dijkstra_string = ["Dijkstra Pathfinding Algorithm", "Weighted -> Yes", "Guarantees shortest path -> Yes", "Time complexity -> O(E*logV)", "Spacial complexity -> O(E*logV)"]
dfs_string = ["Depth First Search", "Weighted -> No", "Guarantees shortest path -> No", "Time complexity -> O(b^d)", "Spacial complexity -> O(b*d)"]
best_first_search_string = ["Best First Search", "Weighted -> No", "Guarantees shortest path -> No", "Time complexity -> O(b^d)", "Spacial complexity -> Polynomial"]
time_string = [""]

WIDTH = 1200
HEIGHT = 750
ROWS = 50
GAP = 15

button_start = Button(825, 400, 150, 50, WHITE, DARK_BUTTON, "START")
button_reset = Button(975, 400, 150, 50, WHITE, DARK_BUTTON, "RESET GRID")
button_astar = Button(825, 550, 150, 50, WHITE, DARK_BUTTON, "A*")
button_bfs = Button(975, 550, 150, 50, WHITE, DARK_BUTTON, "BFS")
button_bidirectional = Button(825, 600, 150, 50, WHITE, DARK_BUTTON, "BIDIRECTIONAL")
button_dijkstra = Button(975, 600, 150, 50, WHITE, DARK_BUTTON, "DIJKSTRA")
button_dfs = Button(825, 650, 150, 50, WHITE, DARK_BUTTON, "DFS")
button_best_first_search = Button(975, 650, 150, 50, WHITE, DARK_BUTTON, "BEST FIRST SEARCH")
legend_start = Button(775, 275, 15, 15, BLACK, ORANGE, "S")
legend_end = Button(900, 275, 15, 15, BLACK, TURQUOISE, "E")
legend_obstacle = Button(1025, 275, 15, 15, WHITE, BLACK, "X")