from TrenchPuzzle import State
from TrenchPuzzle import modify_queue
from TrenchPuzzle import Astar_modify_queue
import heapq
import time


#  Things to need for 9 men in trench problem

# Uniform cost search

# How to represent the state of the problem
# A state is a list of 13 numbers
# All 0s are blank spaces
# Numbers for men are 1-9
# Places 10-12 are where the spaces are for the trench to move out of the line:  index 3 under 10, 5 under 11, 7 under 12 


# The initial state list:
# 0 2 3 4 5 6 7 8 9 1 0 0 0

# Represents pictorally like this:
#       0   0   0
# 0 2 3 4 5 6 7 8 9 1

# The goal state list:
# 1 2 3 4 5 6 7 8 9 0 0 0 0

# Represents pictorally like this:
#       0   0   0
# 1 2 3 4 5 6 7 8 9 0

# Operators Move one of four blanks up, down, left, right (depending on the position of the blank)

# The cost of each operator - 1

def ucs(initial_state):
    # Implement the Uniform Cost Search algorithm 
    # print("Uniform Cost Search not implemented yet.")

    nodes = []
    # Keep track of states that have been visited
    visited = set()
    queue = []
    queue.append((initial_state))  # (state, cost)
    # visited.add(tuple(initial_state))
    iteration = 0
    # Adding a start time to measure the time it takes to run the algorithm
    start_time = time.time()

    while queue:
        current_state = queue.pop(0)
        # Check if the current state has already been visited
        if tuple(current_state.state) in visited:
            # print("State already visited, skipping...")
            continue
        visited.add(tuple(current_state.state))
        # Print size of visited set for debugging
        if iteration % 100000 == 0:
            print(f"Queue size: {len(queue)}, Visited size: {len(visited)}")
            iteration = 0

        iteration += 1


        # Check if the current state is the goal state
        if current_state.state == [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0]:
            print("Goal state reached!")
            # Calculate the time taken to run the algorithm
            end_time = time.time()
            time_taken = end_time - start_time
            print(f"Time taken: {time_taken:.2f} seconds")
            # Print the visited states for debugging
            print("Number of visited states:", len(visited))
            return

        # Generate successors (children) of the current state
        queue = modify_queue(queue, current_state, visited)


    if len(queue) == 0:
        print("No solution found.")

        # Print the visited states for debugging
        # print("Visited states:")
        # for state in visited:
        #     print(state)
        end_time = time.time()
        time_taken = end_time - start_time
        print(f"Time taken: {time_taken:.2f} seconds")
        print("Number of visited states:", len(visited))

        return

    pass

def a_star_manhattan(initial_state):
    # Implement the A* search algorithm with Manhattan distance heuristic here
    #  WORK IN PROGRESS, NOT FINISHED OR FUNCTIONAL YET

    # Keep track of states that have been visited
    visited = set()
    priority_queue = []
    heapq.heapify(priority_queue)
    heapq.heappush(priority_queue, (0, 0, initial_state))  # (cost, state)
    # visited.add(tuple(initial_state))
    iteration = 0
    # Adding a start time to measure the time it takes to run the algorithm
    start_time = time.time()

    while priority_queue:
        current_state = heapq.heappop(priority_queue)[2]
        # Check if the current state has already been visited
        if tuple(current_state.state) in visited:
            # print("State already visited, skipping...")
            continue
        visited.add(tuple(current_state.state))
        # Print size of visited set for debugging
        if iteration % 100000 == 0:
            print(f"Queue size: {len(priority_queue)}, Visited size: {len(visited)}")
            iteration = 0

        iteration += 1


        # Check if the current state is the goal state
        if current_state.state == [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0]:
            print("Goal state reached!")
            # Calculate the time taken to run the algorithm
            end_time = time.time()
            time_taken = end_time - start_time
            print(f"Time taken: {time_taken:.2f} seconds")
            # Print the visited states for debugging
            print("Number of visited states:", len(visited))
            return

        # Generate successors (children) of the current state
        priority_queue = Astar_modify_queue(priority_queue, current_state, visited)


    if len(priority_queue) == 0:
        print("No solution found.")

        # Print the visited states for debugging
        # print("Visited states:")
        # for state in visited:
        #     print(state)

        # Calculate the time taken to run the algorithm
        end_time = time.time()
        time_taken = end_time - start_time
        print(f"Time taken: {time_taken:.2f} seconds")
        # Print the visited states for debugging
        print("Number of visited states:", len(visited))

        return
    
    pass

# def a_star_euclidean(initial_state):
#     # Implement the A* search algorithm with Euclidean distance heuristic here
#     pass

def main():
    # The initial 
    initial_state = State([0, 2, 3, 4, 5, 6, 7, 8, 9, 1, 0, 0, 0], [0, 10, 11, 12])

    # Implement custom input for the initial state

    # Select what type search algorithm to use (UCS , A* w/Manhattan, A* w/Euclidean?)
    # Execute which ever search algorithm is selected and print success or failure

    print("Select search algorithm:")
    print("1. Uniform Cost Search")
    print("2. A* Search with Manhattan Distance")

    alg = input("Enter your choice (1 or 2): ")
    if alg == '1':
        print("Using Uniform Cost Search")
        # Call the UCS function
        ucs(initial_state)
    elif alg == '2':
        print("Using A* Search with Manhattan Distance")
        # Call the A* function with Manhattan distance heuristic
        a_star_manhattan(initial_state)
    else:
        print("Invalid choice. Please select 1 or 2.")


if __name__ == "__main__":
    main()
