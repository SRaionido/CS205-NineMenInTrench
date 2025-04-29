from driverTest import testVar
from driverTest import testFunct

#  Things to need for 9 men in trench problem

# Uniform cost search

# How to represent the state of the problem
# A state is vector of 13 numbers
# All 0s are blanks
# Numbers 1-9
# Places 10-12 are where the divets are for the trench to move: 3 and 10, 5 and 11, 7 and 12 


# The initial state 
# 0 2 3 4 5 6 7 8 9 1 0 0 0

# The goal state
# 0 1 2 3 4 5 6 7 8 9 0 0 0

# Operators Move one of four blanks up, down, left, right (depending on the position of the blank)

# The cost of each operator - 1

def ucs(initial_state):
    # Implement the Uniform Cost Search algorithm here
    pass

def a_star_manhattan(initial_state):
    # Implement the A* search algorithm with Manhattan distance heuristic here
    pass

# def a_star_euclidean(initial_state):
#     # Implement the A* search algorithm with Euclidean distance heuristic here
#     # MAYBE WILL DO
#     pass

def main():
    # The initial state
    initial_state = [0, 2, 3, 4, 5, 6, 7, 8, 9, 1, 0, 0, 0]

    # Implement custom input for the initial state

    # Select what type search algorithm to use (UCS , A* w/Manhattan, A* w/Euclidean?)

    # Execute which ever search algorithm is selected and print success or failure

    # Test the initial state and goal state
    testFunct(initial_state)

if __name__ == "__main__":
    main()
