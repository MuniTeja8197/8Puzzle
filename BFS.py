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

#Random Search

def random_search(board):
    loop_cnt = 0
    while board != goal_board:
        action = random.choice(get_possible_actions(board))
        update_board(board, action)
        #show_board(board)
        loop_cnt += 1
    show_board(board)
    print("Done in {} steps".format(loop_cnt))


# Breadth First Search

def BFS(board): 
    # node is (cost, board, parent)
    visited_states = set()
    root_node = (0,board,None)
    frontier = [root_node]
    loop_cnt = 0
    num_created_successors = 0
    while frontier != []:
        loop_cnt += 1
        node = frontier.pop(0)
        if node[1] == goal_board:
            show_solution(node)
            print(loop_cnt, num_created_successors, len(visited_states))
            return
        # generate next states (successors)
        successors = expand(node[1])
        num_created_successors += len(successors)
        # for each successors, turn it to a node and add it to frontier
        for suc in successors:
            if tuple(suc) not in visited_states:
                visited_states.add(tuple(suc))
                new_node = (node[0]+1,suc,node)
                frontier.append(new_node)

def show_solution(node):
    path = [node[1]]
    while node[2] != None:
        node = node[2]
        path.append(node[1])
    path.reverse()
    print("Solution sequences...")
    if len(path) < 100:
        for b in path:
            show_board(b)
    print("Solution in {} steps".format(len(path)-1))


def expand(board):
    # Given a board, return a list of next states
    # eg) expand([1,2,3,4,5,6," ",7,8]) returns
    #   [ [1,2,3," ",5,6,4,7,8], [1,2,3,4,5,6,7," ",8] ]
    successors = []
    actions = get_possible_actions(board)
    for act in actions:
        new_board = board[:]
        update_board(new_board,act)
        successors.append(new_board)
    return successors


show_board(board)
show_board(goal_board)
print(get_possible_actions(board))
random_shuffle(board,100)
print('----After Shuffling----')
show_board(board)
print("----Breadth First Search----- \n")
BFS(board)