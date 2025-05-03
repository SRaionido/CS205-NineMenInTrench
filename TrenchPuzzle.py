class State:
    def __init__(self, curr_state, blank_positions):
        self.state = curr_state
        self.blank_positions = blank_positions  # List of indices of blank positions

def modify_queue(queue, current_state, visited):
    # Generate successors (children) of the current state
    # For each blank position, try to move it in all four directions
    # print("Modifying queue...")
    for index in current_state.blank_positions:
        # Check if moving down is possible
        # The blank can move down if the index value is 10, 11, or 12
        if index == 10:
            # Move blank down to index 3
            queue = blank_down(current_state, 3, index, queue, visited)
        elif index == 11:
            # Move blank down to index 5
            queue = blank_down(current_state, 5, index, queue, visited)
        elif index == 12:
            # Move blank down to index 7
            queue = blank_down(current_state, 7, index, queue, visited)

        # Check if moving up is possible
        # The blank can move up if the index value is 3, 5, or 7
        if index == 3:
            # Move blank up to index 10
            queue = blank_up(current_state, 10, index, queue, visited)
        elif index == 5:
            # Move blank up to index 11
            queue = blank_up(current_state, 11, index, queue, visited)
        elif index == 7:
            # Move blank up to index 12
            queue = blank_up(current_state, 12, index, queue, visited)

        # Check if moving left is possible
        # The blank can move left if the index value is not 0 and no other blank is next to the left of it
        if index > 0 & index < 10:
            neighbor_present = False
            for neighbor_check_index in current_state.blank_positions:
                if neighbor_check_index == index - 1:
                    neighbor_present = True
                    # print (f"Blank at index {index} cannot move left because another blank is at index {neighbor_check_index}.")
                    break
            if not neighbor_present:
                # Move blank left to index - 1
                queue = blank_left(current_state, index - 1, index, queue, visited)


        # Check if moving right is possible
        # The blank can move right if the index value is not 9 and no other blank is next to the right of it
        if index < 9 & index >= 0:
            neighbor_present = False
            for neighbor_check_index in current_state.blank_positions:
                if neighbor_check_index == index + 1:
                    neighbor_present = True
                    # print (f"Blank at index {index} cannot move right because another blank is at index {neighbor_check_index}.")
                    break
            if not neighbor_present:
                # Move blank right to index + 1
                queue = blank_right(current_state, index + 1, index, queue, visited)
        

    return queue

def Astar_modify_queue(prio_queue, current_state, visited):
    # Implement the A* algorithm to modify the priority queue

    # TO BE IMPLEMENTED
    print("A* algorithm not implemented yet.")
    return prio_queue



def manhattan_distance_heuristic_cost(state):
    # Find the index of the 1 value in the state
    index_of_1 = state.state.index(1)
    # Calculate the Manhattan distance from the index of the sergant (1) to the goal position (index = 1)
    heuristic = abs(index_of_1 - 1)
    return heuristic + 1
    

def blank_down(state, newIndex, currIndex, queue, visited):
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
    queue.append(State(new_state, new_blank_positions))

    return queue

def blank_up(state, newIndex, currIndex, queue, visited):
    # Move the blank up to new index
    new_state = state.state.copy()
    new_state[currIndex] = new_state[newIndex]
    new_state[newIndex] = 0
    # Replace the blank position with new index value
    new_blank_positions = state.blank_positions.copy()
    new_blank_positions.remove(currIndex)
    new_blank_positions.append(newIndex)
    # print(f"Moving blank up to index {newIndex}")
    # Check if the new state has already been visited
    # if tuple(new_state) in visited:
    #     # print("State already visited, skipping...")
    #     return queue
    queue.append(State(new_state, new_blank_positions))

    return queue

def blank_left(state, newIndex, currIndex, queue, visited):
    # Move the blank left if possible
    new_state = state.state.copy()
    new_state[currIndex] = new_state[newIndex]
    new_state[newIndex] = 0
    # Replace the blank position with new index value
    new_blank_positions = state.blank_positions.copy()
    new_blank_positions.remove(currIndex)
    new_blank_positions.append(newIndex)
    # print(f"Moving blank left to index {newIndex}")
    # Check if the new state has already been visited
    # if tuple(new_state) in visited:
    #     # print("State already visited, skipping...")
    #     return queue
    queue.append(State(new_state, new_blank_positions))

    return queue

def blank_right(state, newIndex, currIndex, queue, visited):
    # Move the blank right if possible
    new_state = state.state.copy()
    new_state[currIndex] = new_state[newIndex]
    new_state[newIndex] = 0
    # Replace the blank position with new index value
    new_blank_positions = state.blank_positions.copy()
    new_blank_positions.remove(currIndex)
    new_blank_positions.append(newIndex)
    # print(f"Moving blank right to index {newIndex}")
    # Check if the new state has already been visited
    # if tuple(new_state) in visited:
    #     # print("State already visited, skipping...")
    #     return queue
    queue.append(State(new_state, new_blank_positions))

    return queue

