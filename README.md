# Search Algorithms Implementation for Pacman

This README provides an overview of the implementation of search algorithms for the Pacman AI project. The implementation is divided into two files: `search.py` and `explored.py`, each serving a specific purpose as described below.

## Introduction

This project focuses on teaching Pacman how to plan for a goal using various search algorithms. Pacman will navigate through maze-like environments without being chased by ghosts. The implementation involves graph search algorithms and heuristic functions to guide Pacman towards its goal efficiently.

## Usage

To use the implemented search algorithms, follow these steps:

1. **Invoke Pacman Game**: Run the Pacman game using the following command:

   ```
   python pacman.py --layout mazename --pacman SearchAgent --agentArgs search_fn=search_type
   ```

   - `mazename`: Specify the layout of the maze (e.g., `smallMaze`, `mediumMaze`, `bigMaze`).
   - `search_type`: Specify the search algorithm to be used (e.g., `breadthFirstSearch`, `depthFirstSearch`, `aStarSearch`).

2. **View Results**: Observe Pacman's exploration of the maze, with shaded positions indicating the order of exploration. The darker shades represent older positions explored.

## Files

### `search.py`

This file contains implementations of the following search algorithms:

- `BreadthFirstSearch`
- `DepthFirstSearch`
- `AStarSearch`

Each algorithm class provides the following class methods:

- `g(cls, node)`: Returns the cost to reach a `SearchNode` instance according to the search algorithm being implemented.
- `h(cls, node, problem)`: Returns the cost to reach the goal as defined by the search algorithm. The `problem` argument provides information about the problem, such as goal states.
- `search(cls, problem)`: Executes a graph search using the class methods `g` and `h`. Returns a solution path or `None` if no solution is found.

### `explored.py`

This file contains the implementation of the `Explored` class, which manages an explored set during graph search. The class provides functionality to add and check for explored states.

## Instructions

- Ensure that the provided command-line arguments are used to specify the layout and search algorithm.
- Use the function calls provided for each search algorithm (`breadthFirstSearch`, `depthFirstSearch`, `aStarSearch`) as the `search_fn` argument.