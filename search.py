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
import searchAgents

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

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    # Stack
    s = util.Stack()
    
    # intial -> successor
    push_states = problem.getSuccessors(problem.getStartState())
    print push_states
    for i in range(len(push_states)):
        s.push((push_states[i],-1))
        print push_states[i]
    
    # answer
    answer = []
    
    # visited
    visited = set(problem.getStartState())
    
    
    while not s.isEmpty():
        # top element
        state = s.pop()
        visited.add(state[0][0])
        # if goal then end it
        if problem.isGoalState(state[0][0]):
            answer.append((state[0][1],state[1]))
            break
        
        # or...........
        else:
            answer.append((state[0][1],state[1]))
            push_states = problem.getSuccessors(state[0][0])
            
            for i in range(len(push_states)):
                if not (push_states[i][0] in visited):
                    s.push((push_states[i], len(answer)-1))
                    # visited.add(push_states[i][0])          
    a = answer[len(answer)-1][1]
    indices = []
    while a!=-1:
        indices.append(a)
        a = answer[a][1]
    a = len(indices)-1
    result = []
    while a>=0:
        result.append(answer[indices[a]][0])
        a -=1
    result.append(answer[len(answer)-1][0])
    return result

def breadthFirstSearch(problem):
    # Queue
    s = util.Queue()
    # visited
    visited = set(problem.getStartState())
    # intial -> successor
    push_states = problem.getSuccessors(problem.getStartState())
    for i in range(len(push_states)):
        s.push((push_states[i],-1))
        visited.add(push_states[i][0])
    # answer
    answer = []
    
    while not s.isEmpty():
        # top element
        state = s.pop()
        # if goal then end it
        if problem.isGoalState(state[0][0]):
            answer.append((state[0][1],state[1]))
            break
        
        # or...........
        else:
            answer.append((state[0][1],state[1]))
            push_states = problem.getSuccessors(state[0][0])
            
            for i in range(len(push_states)):
                if not (push_states[i][0] in visited):
                    s.push((push_states[i], len(answer)-1))
                    visited.add(push_states[i][0])          
    a = answer[len(answer)-1][1]
    indices = []
    while a!=-1:
        indices.append(a)
        a = answer[a][1]
    a = len(indices)-1
    result = []
    while a>=0:
        result.append(answer[indices[a]][0])
        a -=1
    result.append(answer[len(answer)-1][0])
    return result

def uniformCostSearch(problem):
    #PriorityQueue
    s = util.PriorityQueue()
    # visited
    visited = set(problem.getStartState())
    # intial -> successor
    push_states = problem.getSuccessors(problem.getStartState())
    for i in range(len(push_states)):
        a = (push_states[i],-1)
        s.push(a,push_states[i][2])
    
    # answer
    answer = []
    while not s.isEmpty():
        # top element
        state = s.pop()
        if state[0][0] in visited:
            continue
        visited.add(state[0][0])
        # if goal then end it
        if problem.isGoalState(state[0][0]):
            answer.append((state[0][1],state[1]))
            break
        
        # or...........
        else:
            answer.append((state[0][1],state[1]))
            push_states = problem.getSuccessors(state[0][0])
            for i in range(len(push_states)):
                if not (push_states[i][0] in visited):
                    a = [(push_states[i][0],push_states[i][1],push_states[i][2]+state[0][2]), len(answer)-1]
                    s.push(a,a[0][2])          
    a = answer[len(answer)-1][1]
    indices = []
    while a!=-1:
        indices.append(a)
        a = answer[a][1]
    a = len(indices)-1
    result = []
    while a>=0:
        result.append(answer[indices[a]][0])
        a -=1
    result.append(answer[len(answer)-1][0])
    return result

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    #PriorityQueue
    s = util.PriorityQueue()
    # visited
    visited = set(problem.getStartState())
    # intial -> successor
    push_states = problem.getSuccessors(problem.getStartState())
    for i in range(len(push_states)):
        a = (push_states[i],-1)
        s.push(a,push_states[i][2]+heuristic(push_states[i][0],problem))
    
    # answer
    answer = []
    while not s.isEmpty():
        # top element
        state = s.pop()
        if state[0][0] in visited:
            continue
        visited.add(state[0][0])
        # if goal then end it
        if problem.isGoalState(state[0][0]):
            answer.append((state[0][1],state[1]))
            break
        
        # or...........
        else:
            answer.append((state[0][1],state[1]))
            push_states = problem.getSuccessors(state[0][0])
            for i in range(len(push_states)):
                if not (push_states[i][0] in visited):
                    a = [(push_states[i][0],push_states[i][1],push_states[i][2]+state[0][2]), len(answer)-1]
                    s.push(a,a[0][2]+heuristic(push_states[i][0],problem))          
    a = answer[len(answer)-1][1]
    indices = []
    while a!=-1:
        indices.append(a)
        a = answer[a][1]
    a = len(indices)-1
    result = []
    while a>=0:
        result.append(answer[indices[a]][0])
        a -=1
    result.append(answer[len(answer)-1][0])
    return result


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
