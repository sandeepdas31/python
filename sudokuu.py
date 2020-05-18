board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]


def solve(board1):
    find = find_empty(board1)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(board1, i, (row, col)):
            board1[row][col] = i

            if solve(board1):
                return True

            board1[row][col] = 0

    return False


def valid(board1, num, pos):

    for i in range(len(board1[0])):
        if board1[pos[0]][i] == num and pos[1] != i:
            return False


    for i in range(len(board1)):
        if board1[i][pos[1]] == num and pos[0] != i:
            return False


    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if board1[i][j] == num and (i,j) != pos:
                return False

    return True


def print_board(board1):
    for i in range(len(board1)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(board1[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board1[i][j])
            else:
                print(str(board1[i][j]) + " ", end="")


def find_empty(board1):
    for i in range(len(board1)):
        for j in range(len(board1[0])):
            if board1[i][j] == 0:
                return (i, j)

    return None

"""
board=[]
for i in range(1,10):
    a=[]
    for j in range(1,10):
        a.append(int(input()))
    board.append(a)
"""

print_board(board)
solve(board)
print("___________________")
print_board(board)
