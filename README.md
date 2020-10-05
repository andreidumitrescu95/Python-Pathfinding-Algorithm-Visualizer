# Python Pathfinding Algorithm Visualizer

I built this application for two main reasons: to get much more accomodated with python and to 

## The project

The project is implemented in Python using Pygame. We create a grid, we draw it to the screen and depending on the algorithm the user will be able to visualize several pathfinding algorithms in action and analyze the results (time elapsed, nodes visited, time and space complexity).

## Algorithms

**A* Search** - the best pathfinding algorithm as it always finds the shortest path and does it much faster than Dijkstra by using a heuristic function that aproximates the distance between the currently probed node and the end node.

**Best First Search** - also uses a heuristic function to determine the approximate distance between nodes, but does not guarantee neither the shortest path, nor finding the actual end node.

**Breadth First Search** - is a search algorithm most commonly used to traverse graphs, but can also be used to find the path between two nodes. It does guarantee the shortest path and it will always find the end node, but at a much slower rate than others.

**Depth First Search** - also a search algorithm for graph traversal and is arguably the worst contender for pathfinding as it searches in depth through neighbors and in doing so can search the entire grid space before finding the end node.

**Bidirectional Breadth First Search** - a combination of two breadth first searches, one starting at the start node and one at the end node. The path is computed through the intersection point of the two searches. It does not guarantee the shortest path.

**Dijkstra's Algorithm** - the founding father of search algorithms, that guarantees the shortest path, albeit it being relatively slower than A*.

## The application 

The application allows the user to place start, end and obstacle nodes on a grid. After placing the aforementioned nodes the user is able to select a pathfinding algorithm of his choice and start the visualization process. Once the algorithm is done, the application will display the time elapsed since the start of the algorithm and the total nodes visited in order to find the goal node. The user can now either reset the grid in order to test out another algorithm or exit completely out of the application.
