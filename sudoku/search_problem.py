"""
This module contains ProblemState interface, which is an interface for our
search problem.
The Search Algorithm uses backtracking search to find a solution.
The Search algorithm creates Node instances of the Sudoku Board and searches
the tree for a solution.

"""

class Queue:
    """
    A Queue class to be used in combination with state space
    search. The enqueue method adds new elements to the end. The
    dequeue method removes elements from the front.
    """
    def __init__(self):
        self.queue = []
    def __str__(self):
        result = "Queue contains " + str(len(self.queue)) + " items\n"
        for item in self.queue:
            result += str(item) + "\n"
        return result
    def enqueue(self, node):
        self.queue.append(node)
    def dequeue(self):
        if not self.empty():
            return self.queue.pop(0)
        else:
            raise Exception
    def size(self):
        return len(self.queue)
    def empty(self):
        return len(self.queue) == 0


class Stack:
    """
    A Stack class to be used in combination with state space
    search for backtracking search.
    """
    def __init__(self):
        self.stack = []

    def __str__(self):
        result = "Stack contains " + str(len(self.queue)) + " items\n"
        for item in self.stack:
            result += str(item) + "\n"

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        toReturn = self.stack[-1]
        del self.stack[-1]
        return toReturn

    def top(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def empty(self):
        return self.size() == 0


class Node:
    """
    A Node class to be used in combination with state space search.  A
    node contains a state, a parent node, and the depth of the node in
    the search tree.  The root node should be at depth 0.
    """
    def __init__(self, state, parent, depth):
        self.state = state
        self.parent = parent
        self.depth = depth

    def __str__(self):
        result = "\nState: " +  str(self.state)
        result += "\nDepth: " + str(self.depth)
        if self.parent != None:
            result += "\nParent: " + str(self.parent.state)
        return result

class Search:
    """
    A Search class that can be used for the Sudoku problem domain.
    Given instances of an initial state, this class will return the
    number of possible solutions by using backtracking search.
    The problem domain should be based on the ProblemState
    class.
    """
    total_solns = 0

    def __init__(self, initialState, verbose=False):
        self.uniqueStates = {}
        self.uniqueStates[initialState.dictkey()] = True
        self.q = Stack()
        self.q.push(Node(initialState, None, 0))

        self.verbose = verbose
        solution = self.execute()

    def getNumSolns(self):
        """
        Returns total number of solutions found
        """
        return self.total_solns


    def execute(self):
        while not self.q.empty():
            current = self.q.pop()
            if current.state.isDone():
                self.total_solns += 1
            else:
                successors = current.state.followingStates()
                for nextState in successors:
                    if nextState.dictkey() not in self.uniqueStates.keys():
                        n = Node(nextState, current, current.depth+1)
                        self.q.push(n)
                        self.uniqueStates[nextState.dictkey()] = True
                if self.verbose:
                    print("Expanded:", current)
                    print("Number of successors:", len(successors))
                    print("Queue length:", self.q.size())
                    print( "-------------------------------")


    def showPath(self, node):
        path = self.buildPath(node)
        for current in path:
            print( current.state)
        print("Goal reached in", current.depth, "steps")

    def buildPath(self, node):
        """
        Beginning at the goal node, follow the parent links back
        to the start state.  Create a list of the states traveled
        through during the search from start to finish.
        """
        result = []
        while node != None:
            result.insert(0, node)
            node = node.parent
        return result

class ProblemState:
    """
    An interface class for search problem domains.
    """
    def __str__(self):
        """
        Returns a string representing the state.
        """
        abstract()

    def successors(self):
        """
        Returns a list of valid successors to the current state.
        """
        abstract()

    def equals(self, state):
        """
        Tests whether the state instance equals the given state.
        """
        abstract()

    def dictkey(self):
        """
        Returns a string that can be used as a dictionary key to
        represent unique states.
        """
        abstract()


import sudoku
import generator

if __name__ == "__main__":
    full_board = [
        [ 3, 4, 8, 7, 1, 2, 9, 6, 5],
        [ 2, 5, 6, 9, 4, 8, 7, 1, 3],
        [ 9, 7, 1, 5, 6, 3, 4, 8, 2],
        [ 4, 9, 7, 1, 3, 5, 6, 2, 8],
        [ 5, 6, 3, 8, 2, 7, 1, 9, 4],
        [ 8, 1, 2, 4, 9, 6, 3, 5, 7],
        [ 7, 3, 9, 2, 8, 1, 5, 4, 6],
        [ 6, 2, 4, 3, 5, 9, 8, 7, 1],
        [ 1, 8, 5, 6, 7, 4, 2, 3, 9]
    ]

    for i in range(9):
        full_board[i%3][i] = 0
        full_board[5 - i%3][i] = 0
        full_board[6 + i%3][i] = 0
    game = sudoku.Sudoku(full_board)
    game.printBoard()
    print(Search(game).getNumSolns())
