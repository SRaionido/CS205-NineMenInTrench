import heapq
import itertools

counter = itertools.count()

class State:
    def __init__(self, curr_state, blank_positions):
        self.state = curr_state
        self.blank_positions = blank_positions  # List of indices of blank positions

    def __lt__(self, other):
        return self.state < other.state  # or any logic that makes sense for your State

def modify_queue(queue, current_state, visited):
    # Generate successors (children) of the current state
    # For each blank position, try to move it in all four directions
    # print("Modifying queue...")
    Mode = 0
    for index in current_state.blank_positions:
        # Check if moving down is possible
        # The blank can move down if the index value is 10, 11, or 12
        if index == 10:
            # Move blank down to index 3
            queue = swap(current_state, 3, index, queue, visited, Mode)
        elif index == 11:
            # Move blank down to index 5
            queue = swap(current_state, 5, index, queue, visited, Mode)
        elif index == 12:
            # Move blank down to index 7
            queue = swap(current_state, 7, index, queue, visited, Mode)

        # Check if moving up is possible
        # The blank can move up if the index value is 3, 5, or 7
        if index == 3:
            # Move blank up to index 10
            queue = swap(current_state, 10, index, queue, visited, Mode)
        elif index == 5:
            # Move blank up to index 11
            queue = swap(current_state, 11, index, queue, visited, Mode)
        elif index == 7:
            # Move blank up to index 12
            queue = swap(current_state, 12, index, queue, visited, Mode)

        # Check if moving left is possible
        # The blank can move left if the index value is not 0 and no other blank is next to the left of it
        if (index > 0) & (index < 10):
            neighbor_present = False
            for neighbor_check_index in current_state.blank_positions:
                if neighbor_check_index == index - 1:
                    neighbor_present = True
                    # print (f"Blank at index {index} cannot move left because another blank is at index {neighbor_check_index}.")
                    break
            if not neighbor_present:
                # Move blank left to index - 1
                queue = swap(current_state, index - 1, index, queue, visited, Mode)


        # Check if moving right is possible
        # The blank can move right if the index value is not 9 and no other blank is next to the right of it
        if index < 9:
            neighbor_present = False
            for neighbor_check_index in current_state.blank_positions:
                if neighbor_check_index == index + 1:
                    neighbor_present = True
                    # print (f"Blank at index {index} cannot move right because another blank is at index {neighbor_check_index}.")
                    break
            if not neighbor_present:
                # Move blank right to index + 1
                queue = swap(current_state, index + 1, index, queue, visited, Mode)
        

    return queue

def Astar_modify_queue(prio_queue, current_state, visited):
    # Implement the A* algorithm to modify the priority queue

    # Generate successors (children) of the current state
    # For each blank position, try to move it in all four directions
    Mode = 1
    for index in current_state.blank_positions:
        # Check if moving down is possible
        # The blank can move down if the index value is 10, 11, or 12
        if index == 10:
            # Move blank down to index 3
            prio_queue = swap(current_state, 3, index, prio_queue, visited, Mode)
            # print(f"Moving blank down to index 3")
        elif index == 11:
            # Move blank down to index 5
            prio_queue = swap(current_state, 5, index, prio_queue, visited, Mode)
            # print(f"Moving blank down to index 5")
        elif index == 12:
            # Move blank down to index 7
            prio_queue = swap(current_state, 7, index, prio_queue, visited, Mode)
            # print(f"Moving blank down to index 7")

        # Check if moving up is possible
        # The blank can move up if the index value is 3, 5, or 7
        if index == 3:
            # Move blank up to index 10
            prio_queue = swap(current_state, 10, index, prio_queue, visited, Mode)
            # print(f"Moving blank up to index 10")
        elif index == 5:
            # Move blank up to index 11
            prio_queue = swap(current_state, 11, index, prio_queue, visited, Mode)
            # print(f"Moving blank up to index 11")
        elif index == 7:
            # Move blank up to index 12
            prio_queue = swap(current_state, 12, index, prio_queue, visited, Mode)
            # print(f"Moving blank up to index 12")

        # Check if moving left is possible
        # The blank can move left if the index value is not 0 and no other blank is next to the left of it
        if (index > 0) & (index < 10):
            neighbor_present = False
            for neighbor_check_index in current_state.blank_positions:
                if neighbor_check_index == index - 1:
                    neighbor_present = True
                    break
            if not neighbor_present:
                # Move blank left to index - 1
                prio_queue = swap(current_state, index - 1, index, prio_queue, visited, Mode)
                # print(f"Moving blank left to index {index - 1}")

        # Check if moving right is possible
        # The blank can move right if the index value is not 9 and no other blank is next to the right of it
        if index < 9:
            neighbor_present = False
            for neighbor_check_index in current_state.blank_positions:
                if neighbor_check_index == index + 1:
                    neighbor_present = True
                    break
            if not neighbor_present:
                # Move blank right to index + 1
                prio_queue = swap(current_state, index + 1, index, prio_queue, visited, Mode)
                # print(f"Moving blank right to index {index + 1}")

        # print("Finished expanding a node")

    return prio_queue


def manhattan_distance_heuristic_cost(state):
    # Find the index of the 1 value in the state
    index_of_1 = state.state.index(1)
    # Calculate the Manhattan distance from the index of the sergant (1) to the goal position (index = 0)
    if index_of_1 == 10:
        heuristic = 4
    elif index_of_1 == 11:
        heuristic = 6
    elif index_of_1 == 12:
        heuristic = 8
    heuristic = index_of_1
    return heuristic + 1

def swap(state, newIndex, currIndex, queue, visited, Mode):

    global counter

    # Move the blank down to new index
    new_state = state.state.copy()
    new_state[currIndex] = new_state[newIndex]
    new_state[newIndex] = 0
    # Replace the blank position with new index value
    new_blank_positions = state.blank_positions.copy()
    new_blank_positions.remove(currIndex)
    new_blank_positions.append(newIndex)
    # print(f"Moving blank down to index {newIndex}")
    # Check if the new state has already been visited
    # if tuple(new_state) in visited:
    #     # print("State already visited, skipping...")
    #     return queue

    if Mode == 0:
        queue.append(State(new_state, new_blank_positions))
    elif Mode == 1:
        # Calculate the heuristic cost using Manhattan distance
        heuristic_cost = manhattan_distance_heuristic_cost(State(new_state, new_blank_positions))
        # Add the state to the priority queue with the heuristic cost as the priority
        heapq.heappush(queue, (heuristic_cost, next(counter), State(new_state, new_blank_positions)))
    else:
        raise ValueError("Invalid mode. Mode should be 0 or 1.")

    return queue
