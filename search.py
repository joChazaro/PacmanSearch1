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



#TODO: We have a set to save the individual nodes, but we need the set to save the PATH taken to those nodes. 
#That is because the nodes themselves will be entering and leaving the stack pretty consistenly. 
#The nodes themselves won't be unique but their paths will be.
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


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
        Search the deepest nodes in the search tree first.

        Your search algorithm needs to return a list of actions that reaches the
        goal. Make sure to implement a graph search algorithm.

        To get started, you might want to try some of these simple commands to
        understand the search problem that is being passed in:
    """

    explored = set() #where visited nodes will be added make the explored into a list -> easier to deal with? 
    fringeStack =  util.Stack()  # stack is empty
    firstNode = problem.getStartState() #identify first node
    print(firstNode)
    fringeStack.push((firstNode, []))
    search = True
    
    while search is True:  # loop do the do 
        print("tis but the beginning") #test print
        if not fringeStack.isEmpty(): # checking if first node is empty, if empty -> fringe is empty, bad if it is empty
            assert "Failure: fringe do be empty" # raise Exception("Fringe is empty") -> begone thot
        print("we shall continue onward") #test print
        currentNode, path = fringeStack.pop()
        
        if problem.isGoalState(currentNode): #by god's will if it is the first state we done 
            print(currentNode)
            print("Ye got it lad! - (nextState, actionFromCurrStateToNextState, costToGetFromCurrStateToNextState)")
            return(path)
        if currentNode not in explored: #if this node isnt a repeated node thou shall continue 
            explored.add(currentNode)
            for child in (problem.getSuccessors(currentNode)):
                fringeStack.push((child[0], path + [child[1]]))

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    """
        Search the deepest nodes in the search tree first.

        Your search algorithm needs to return a list of actions that reaches the
        goal. Make sure to implement a graph search algorithm.

        To get started, you might want to try some of these simple commands to
        understand the search problem that is being passed in:
    """

    explored = set() #where visited nodes will be added make the explored into a list -> easier to deal with? 
    fringeStack =  util.Queue()  # stack is empty
    firstNode = problem.getStartState() #identify first node
    fringeStack.push((firstNode, []))
    search = True
    
    while search is True:  # loop do the do 
        if not fringeStack.isEmpty(): # checking if first node is empty, if empty -> fringe is empty, bad if it is empty
            assert "Failure: fringe do be empty" # raise Exception("Fringe is empty") -> begone thot
        currentNode, path = fringeStack.pop()
        
        if problem.isGoalState(currentNode): #by god's will if it is the first state we done 
            print(currentNode)
            return(path)
        if currentNode not in explored: #if this node isnt a repeated node thou shall continue 
            explored.add(currentNode)
            for child in (problem.getSuccessors(currentNode)):
                fringeStack.push((child[0], path + [child[1]]))

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
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
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
