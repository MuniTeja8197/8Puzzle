goal_board = [1,2,3,4,5,6,7,8," "]
board = [7,2,4,5," ",6,8,3,1]

#To show the board in required format

def show_board(board):
    for i in range(len(board)):
        print(board[i],end=" ")
        if i % 3 == 2:
            print()
    print()

#To get the actions to move the queen

def get_possible_actions(board):
    # return a list of possible actions
    # actions are "Left", "Right", "Up", "Down"
    # eg) ["Left","Up"]
    actions = []
    empty_index = board.index(" ")
    r = empty_index // 3
    c = empty_index % 3
    if r < 2:
        actions.append("Down")
    if r > 0:
        actions.append("Up")
    if c < 2:
        actions.append("Right")
    if c > 0:
        actions.append("Left")
    return actions

#Updates the board after ceratin move has done

def update_board(board,action):
    # make change to the board after taking the given action
    # if action == "Up", then swap empty slot with Up guy.
    # if action == "Left", then swap empty with Left guy.
    empty_index = board.index(" ")
    if action == "Up":
        switch_index = empty_index - 3
    elif action == "Down":
        switch_index = empty_index + 3
    elif action == "Left":
        switch_index = empty_index - 1
    else: # action == "Right"
        switch_index = empty_index + 1
    # swap between the two positions
    board[empty_index], board[switch_index] = board[switch_index], board[empty_index]

#Shuffles the board randomly(to complicate)

import random
def random_shuffle(board, move_cnt):
    for i in range(move_cnt):
        update_board(board, random.choice(get_possible_actions(board)))


show_board(board)
show_board(goal_board)
print(get_possible_actions(board))
random_shuffle(board,100)
print('----After Shuffling----')
show_board(board)