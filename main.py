from TrenchPuzzle import State
from TrenchPuzzle import modify_queue
from TrenchPuzzle import Astar_modify_queue
from TrenchPuzzle import print_state
from TrenchPuzzle import manhattan_distance_heuristic_cost
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

def a_star_manhattan(initial_state):
    # Implement the A* search algorithm with Manhattan distance heuristic here

    # Keep track of states that have been visited
    visited = set()
    priority_queue = []
    heapq.heapify(priority_queue)
    heapq.heappush(priority_queue, (0, 0, initial_state))  # (cost, state)
    # iteration = 0
    start_time = time.time()    # Adding a start time to measure the time it takes to run the algorithm
    max_queue_size = 0  # Keep track of the maximum size of the queue

    while priority_queue:
        # Pop the state with the lowest cost from the priority queue and save priority
        current_state = heapq.heappop(priority_queue)[2]
        # Check if the current state has already been visited
        if tuple(current_state.state) in visited:
            # print("State already visited, skipping...")
            continue
        visited.add(tuple(current_state.state))

        # Print size of visited set for debugging
        # if iteration % 500000 == 0:
        #     print(f"Queue size: {len(priority_queue)}, Visited size: {len(visited)}")
        #     iteration = 0

        # For debugging purposes, limit the number of iterations to 10
        # if iteration == 10:
        #     print("Iteration limit reached, stopping...")
        #     break

        # iteration += 1

        # Print current node being expanded and its cost
        print("Expanding node with cost g(n) =", manhattan_distance_heuristic_cost(current_state))
        print_state(current_state.state)


        # Check if the current state is the goal state
        if current_state.state == [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0]:
            print("Goal state reached!")
            # Calculate the time taken to run the algorithm
            end_time = time.time()
            time_taken = end_time - start_time
            print(f"Time taken: {time_taken:.2f} seconds")
            # Print the visited states for debugging
            print("Number of visited states:", len(visited))
            print("Queue size:", max_queue_size)
            print("Depth:", current_state.depth)
            return

        # Generate successors (children) of the current state
        priority_queue = Astar_modify_queue(priority_queue, current_state, visited)
        # Update max queue size if current size is larger
        if len(priority_queue) > max_queue_size:
            max_queue_size = len(priority_queue)


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
        print("Queue size:", max_queue_size)

        return
    
    print("No solution found.")
    
    return

# def a_star_euclidean(initial_state):
#     # Implement the A* search algorithm with Euclidean distance heuristic here
#     pass

def main():
    # The Main Problem initial state
    # initial_state = State([0, 2, 3, 4, 5, 6, 7, 8, 9, 1, 0, 0, 0], [0, 10, 11, 12])

    # Implement custom input for the initial state

    initial_puzzle = input("Enter the initial state (13 numbers separated by spaces): ").split()
    initial_puzzle = [int(x) for x in initial_puzzle]  # Convert to integers
    if len(initial_puzzle) != 13:
        print("Invalid input. Please enter exactly 13 numbers.")
        return
    
    blank_positions = []
    for i in range(len(initial_puzzle)):
        if initial_puzzle[i] == 0:
            blank_positions.append(i)
    initial_state = State(initial_puzzle, blank_positions)
    if len(blank_positions) != 4:
        print("Invalid input. Please enter exactly 4 blank positions.")
        return

    print_state(initial_state.state)  # Print the initial state for debugging
    print("Blank positions:", initial_state.blank_positions)  # Print the blank positions for debugging

    # Call the A* function with Manhattan distance heuristic
    print("Using A* Search with Manhattan Distance")
    print("====================================")

    # Call the A* function with Manhattan distance heuristic
    a_star_manhattan(initial_state)

    return


if __name__ == "__main__":
    main()


# This was a uniform cost search function that was initially implemented to test functions related to problem space.
# The function was commented out once A* search was implemented.
# Kept for reference and proof of progress. Was not fully tested due to how long it took to run.

# def ucs(initial_state):
#     # Implement the Uniform Cost Search algorithm 
#     # print("Uniform Cost Search not implemented yet.")

#     nodes = []
#     # Keep track of states that have been visited
#     visited = set()
#     queue = []
#     queue.append((initial_state))  # (state, cost)
#     # visited.add(tuple(initial_state))
#     iteration = 0
#     # Adding a start time to measure the time it takes to run the algorithm
#     start_time = time.time()
#     max_queue_size = 0  # Keep track of the maximum size of the queue
#     depth = 0  # Keep track of the depth of the current state

#     while queue:
#         current_state = queue.pop(0)
#         # Check if the current state has already been visited
#         if tuple(current_state.state) in visited:
#             # print("State already visited, skipping...")
#             continue
#         visited.add(tuple(current_state.state))
#         # Print size of visited set for debugging
#         if iteration % 500000 == 0:
#             print(f"Queue size: {len(queue)}, Visited size: {len(visited)}")
#             iteration = 0

#         iteration += 1


#         # Check if the current state is the goal state
#         if current_state.state == [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0]:
#             print("Goal state reached!")
#             # Calculate the time taken to run the algorithm
#             end_time = time.time()
#             time_taken = end_time - start_time
#             print(f"Time taken: {time_taken:.2f} seconds")
#             # Print the visited states for debugging
#             print("Number of visited states:", len(visited))
#             print("Queue size:", max_queue_size)
#             print("Depth:", current_state.depth)
#             return

#         # Generate successors (children) of the current state
#         # print("Generating successors...")
#         queue = modify_queue(queue, current_state, visited)
#         # Update max queue size if current size is larger
#         if len(queue) > max_queue_size:
#             max_queue_size = len(queue)


#     if len(queue) == 0:
#         print("No solution found.")

#         # Print the visited states for debugging
#         # print("Visited states:")
#         # for state in visited:
#         #     print(state)
#         end_time = time.time()
#         time_taken = end_time - start_time
#         print(f"Time taken: {time_taken:.2f} seconds")
#         print("Number of visited states:", len(visited))

#         return
    
#     print("No solution found.")

#     return