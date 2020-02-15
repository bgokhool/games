

class ProblemState:
    """
    An interface class for search problem domains.
    """
    def __str__(self):
        """
        Returns a string representing the state.
        """
        abstract()

    def applyOperators(self):
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
        
