# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()

def graph_search(problem, g, h, verbose=False, debug=False):
    from explored import Explored
    
    frontier = util.PriorityQueue()
    frontier.push(Node(problem.getStartState(),None, [], 0), 0)
    explored = Explored() # keep track of nodes we have checked
    explored.add(problem.getStartState())

    while frontier:
        node = frontier.pop() # remove state
        if problem.isGoalState(node.state):
            return node.action
        else:
            # only add novel results from the current node
            successors = problem.getSuccessors(node.state)
            for successor, action, stepCost in successors:
                # if successor not in explored:
                if not explored.exists(successor):
                    newAction = node.action + [action]
                    newNode = Node(successor, node, newAction, problem.getCostOfActions(newAction))
                    new_priority = g(newNode) + h(newNode, problem) # cost/estimate start→n + n→goal
                    explored.add(successor)
                    frontier.push(newNode, new_priority) # merge new nodes in by estimated cost
    return None

def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def genericSearch(problem, g, h):
    state = problem.getStartState()
    goal = problem.goal

from explored import Explored

class DepthFirstSearch:
    @classmethod
    def g(cls, node):
        return 0
    
    @classmethod
    def h(cls, node, problem):
        return -node.depth

    @classmethod
    def search(cls, problem):
        return graph_search(problem, cls.g, cls.h, verbose=False, debug=False)      

class BreadthFirstSearch:
    @classmethod
    def g(cls, node):
        return node.depth
    
    @classmethod
    def h(cls, node, problem):
        return 0

    @classmethod
    def search(cls, problem):
        return graph_search(problem, cls.g, cls.h, verbose=False, debug=False)
    
class AStarSearch:
    @classmethod
    def g(cls, node):
        return node.depth
    
    @classmethod
    def h(cls, node, problem):
        import math
        
        curr_x, curr_y = node.state
        goal_x, goal_y = problem.goal
        return math.sqrt((curr_x - goal_x)**2 + (curr_y - goal_y)**2)

    @classmethod
    def search(cls, problem):
        return graph_search(problem, cls.g, cls.h, verbose=False, debug=False)

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"

    return DepthFirstSearch.search(problem)
    
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    return BreadthFirstSearch.search(problem)
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    return BreadthFirstSearch.search(problem)
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    return AStarSearch.search(problem)
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch


class Node:
    """A node in a search tree. Contains a pointer to the parent (the node
    that this is a successor of) and to the actual state for this node. Note
    that if a state is arrived at by two paths, then there are two nodes with
    the same state. Also includes the action that got us to this state, and
    the total path_cost (also known as g) to reach the node. Other functions
    may add an f and h value; see best_first_graph_search and astar_search for
    an explanation of how the f and h values are handled. You will not need to
    subclass this class."""

    def __init__(self, state, parent=None, action=None, path_cost=0):
        """Create a search tree Node, derived from a parent by an action."""
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1

