class State:
    def __init__(self, curr_state, blank_positions):
        self.state = curr_state
        self.blank_positions = blank_positions  # List of indices of blank positions

def modify_queue(queue, current_state):
    # Generate successors (children) of the current state
    # For each blank position, try to move it in all four directions
    print("Modifying queue...")
    for index in current_state.blank_positions:
        # Check if moving down is possible
        # The blank can move down if the index value is 10, 11, or 12
        if index == 10:
            # Move blank down to index 3
            queue = blank_down(current_state, 3, index, queue)
        elif index == 11:
            # Move blank down to index 5
            queue = blank_down(current_state, 5, index, queue)
        elif index == 12:
            # Move blank down to index 7
            queue = blank_down(current_state, 7, index, queue)

        # Check if moving up is possible
        # The blank can move up if the index value is 3, 5, or 7
        if index == 3:
            # Move blank up to index 10
            queue = blank_up(current_state, 10, index, queue)
        elif index == 5:
            # Move blank up to index 11
            queue = blank_up(current_state, 11, index, queue)
        elif index == 7:
            # Move blank up to index 12
            queue = blank_up(current_state, 12, index, queue)

        # Check if moving left is possible
        # The blank can move left if the index value is not 0 and no other blank is next to the left of it
        

        # Check if moving right is possible
        # The blank can move right if the index value is not 9 and no other blank is next to the right of it
        

    return queue


def blank_down(state, newIndex, currIndex, queue):
    # Move the blank down to new index
    new_state = state.state.copy()
    new_state[currIndex] = new_state[newIndex]
    new_state[newIndex] = 0
    # Replace the blank position with new index value
    new_blank_positions = state.blank_positions.copy()
    new_blank_positions.remove(currIndex)
    new_blank_positions.append(newIndex)
    print(f"Moving blank down to index {newIndex}")
    queue.append(State(new_state, new_blank_positions))

    return queue

def blank_up(state, newIndex, currIndex, queue):
    # Move the blank up to new index
    new_state = state.state.copy()
    new_state[currIndex] = new_state[newIndex]
    new_state[newIndex] = 0
    # Replace the blank position with new index value
    new_blank_positions = state.blank_positions.copy()
    new_blank_positions.remove(currIndex)
    new_blank_positions.append(newIndex)
    print(f"Moving blank up to index {newIndex}")
    queue.append(State(new_state, new_blank_positions))

    return queue

def blank_left(state, index):
    # Move the blank left if possible
    pass

def blank_right(state, index):
    # Move the blank right if possible
    pass

