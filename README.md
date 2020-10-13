# Python Pathfinding Algorithm Visualizer

I built this application in order to get much more accommodated with Python and Pygame and to have a much better understanding of the nature of various pathfinding algorithms through visualization.

## The Project

The project is implemented in Python using Pygame. The program creates a grid, draws it to the screen and depending on the chosen algorithm the user will be able to visualize it in action and analyze the results (time elapsed, nodes visited, time and space complexity).

## The Algorithms

**A*** **Search** - the best pathfinding algorithm as it always finds the shortest path and does it much faster than Dijkstra by using a heuristic function that approximates the distance between the currently probed node and the end node.

**Best First Search** - also uses a heuristic function to determine the approximate distance between nodes, but does not guarantee neither the shortest path, nor finding the actual end node.

**Breadth First Search** - is a search algorithm most commonly used to traverse graphs, but can also be used to find the path between two nodes. It does guarantee the shortest path and it will always find the end node, but at a much slower rate than others.

**Depth First Search** - also a search algorithm for graph traversal and is arguably the worst contender for pathfinding as it searches in depth through neighbors and in doing so can search the entire grid space before finding the end node.

**Bidirectional Breadth First Search** - a combination of two breadth first searches, one starting at the start node and one at the end node. The path is computed through the intersection point of the two searches. It does not guarantee the shortest path.

**Dijkstra's Algorithm** - the founding father of search algorithms, that guarantees the shortest path, albeit it being relatively slower than A*.

Both the A* and Best First Search heuristic are based on the Manhattan distance between two points.

## The Application 

The application allows the user to place start, end and obstacle nodes on a grid. After placing the aforementioned nodes the user is able to select a pathfinding algorithm of his choice and start the visualization process. Once the algorithm is done, the application will display the time elapsed since the start of the algorithm and the total nodes visited in order to find the goal node. The user can now either reset the grid in order to test out another algorithm or exit completely out of the application.

![](https://github.com/andreidumitrescu95/Python-Pathfinding-Algorithm-Visualizer/blob/master/application.gif)

## WIP features and functionalities

At the current stage all proposed pathfinding algorithms have been implemented and the flow of the application is complete enough so that a user may be able to visualize all algorithms and reset the grid easily.
Further adjustments can be made in the optimization department. I am considering switching from lists and arrays to numpy arrays which should make the app run a bit faster, seeing as numpy data structures are linear and they take less time to swap and compare values.
