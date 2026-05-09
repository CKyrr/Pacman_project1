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


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]



def depthFirstSearch(problem: SearchProblem): 
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

    from util import Stack 

    frontier=Stack() #Stoiva(LIFO) gia na diaxirizomai tis katastasis gia exerevnisi 
    arxi=problem.getStartState() 
    frontier.push((arxi, [])) 
    #kathe stoixio tis stivas einai tuple(state,path) 
    #state=trexousa katastasi 
    #path=i diadromi apo tin arxi mexri eki(ton stoxo) 

    explored=set() #sinolo-set gia tis katastasis pou exoun idi episkefthi

    #loop mexri na adiasi i stoiva/vrethi lisi 
    while not frontier.isEmpty(): 
        state,path=frontier.pop()

        #an exi idi episkefthi, tin agnoo 
        if state in explored: 
            continue 
        explored.add(state) 
    
       #elegxos an einai to goal i katastasi pou vriskome 
        if problem.isGoalState(state): 
            return path 
    
        #psaxno gia kathe successor tis katastasis 
        for successor,action,stepCost in problem.getSuccessors(state): 
            if successor not in explored: 
                newpath=path+[action] #nea diadromi pou exi mesa to neo vima pou kani 
                frontier.push((successor,newpath)) #vazo stin stoiva tin nea katastasi kai tin diadromi mexri na tin vri 
            
    #epistrefo keni lista an den iparxi lisi 
    return [] 
    #util.raiseNotDefined() 


def breadthFirstSearch(problem: SearchProblem): 
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    from util import Queue 
    frontier=Queue() #Oura(FIFO) gia tis katastasis pou tha exerevniso 
    arxi=problem.getStartState() 
    frontier.push((arxi, [])) #kathe stoixio tis stivas einai tuple(state,path) 
    #state=trexousa katastasi 
    #path=i diadromi apo tin arxi mexri eki(ton stoxo) 

    explored=set() #sinolo-set gia tis katastasis pou exoun idi episkefthi 
    
    #loop mexri na adiasi i oura/vrethi lisi 
    while not frontier.isEmpty(): 
        state,path=frontier.pop() 
        
        #an exi idi episkefthi, tin agnoo 
        if state in explored: 
            continue 
        explored.add(state) 
        
        #elegxos an einai to goal i katastasi pou vriskome 
        if problem.isGoalState(state): 
            return path 
        
        #psaxno gia kathe successor tis katastasis 
        for successor,action,stepCost in problem.getSuccessors(state): 
            if successor not in explored: 
                newpath=path+[action] #nea diadromi pou exi mesa to neo vima pou kani 
                frontier.push((successor,newpath)) #vazo stin stoiva tin nea katastasi kai tin diadromi mexri na tin vri 
                
    #epistrefo keni lista an den iparxi lisi 
    return [] 
    #util.raiseNotDefined() 
    

def uniformCostSearch(problem: SearchProblem): 
    """Search the node of least total cost first.""" 
    "*** YOUR CODE HERE ***" 
    
    from util import PriorityQueue 
    frontier=PriorityQueue() #Priority Queue gia tis katastasis pou tha exerevniso 
    arxi=problem.getStartState() 
    frontier.push((arxi, [],0),0) #kathe stoixio tis ouras proteraiotitas einai tuple(state,path,cost) 
    
    explored=set() #krata to mikrotero kostos g gia kathe state 
    
    #loop mexri na adiasi i oura/vrethi lisi 
    while not frontier.isEmpty(): 
        state,path,cost=frontier.pop() 
        
        if state in explored: 
            continue 
        explored.add(state) 
        
        #elegxos an einai to goal i katastasi pou vriskome 
        if problem.isGoalState(state): 
            return path 
        
        for successor,action,stepCost in problem.getSuccessors(state):
            if successor not in explored:
                newcost=cost+stepCost #neo kostos 
                newpath=path+[action] #nea diadromi pou exi mesa to neo vima pou kani 
                frontier.push((successor,newpath,newcost),newcost) #vazo sto queue tin nea katastasi,tin diadromi mexri na tin vri kai to neo kostos 
            
    #epistrefo keni lista an den iparxi lisi 
    return [] 
    #util.raiseNotDefined() 
    

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic): 
    """Search the node that has the lowest combined cost and heuristic first.""" 
    "*** YOUR CODE HERE ***" 
    
    from util import PriorityQueue 
    frontier=PriorityQueue() #gia na diaxirizomai tis katastasis gia exerevnisi 
    arxi=problem.getStartState() 
    #to kostos=0 mexri tora,& i protereotita einai mono i heuristic timi 
    frontier.push((arxi, [],0),heuristic(arxi,problem)) 
    #prostheto tin arxiki katastasi: path=[], cost=0

    explored = set()

    #loop mexri na adiasi i oura/vrethi lisi 
    #vgazo ton komvo me tin mikroteri protereotita 
    while not frontier.isEmpty(): 
        state,path,cost=frontier.pop() 
        
        #an exo idi mikrotero cost, ton agnoo
        if state in explored: 
            continue 
        explored.add(state) 
        
        #elegxos an einai to goal i katastasi pou vriskome 
        if problem.isGoalState(state): 
            return path 
        
        #psaxno gia kathe successor tis katastasis 
        for successor,action,stepCost in problem.getSuccessors(state): 
            if successor not in explored: 
                newpath=path+[action] 
                newcost=cost+stepCost 
                protereotita= newcost+heuristic(successor,problem) 
                frontier.push((successor,newpath,newcost),protereotita) 
                
    #epistrefo keni lista an den iparxi lisi 
    return []
    #util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
