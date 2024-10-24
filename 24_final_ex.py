import random
import copy

#program which pretends to play tic-tac-toe with the user

#the computer (i.e., your program) should play the game using 'X's;
#the user (e.g., you) should play the game using 'O's;

#the first move belongs to the computer − it always puts its first 'X' in the middle of the board;

#all the squares are numbered row by row starting with 1

#the user inputs their move by entering the number of the square they choose. 
    #NUMBER MUST BE VALID! (intenger + 1-10)
    #it cannot point to a field which is already occupied

#the program checks if the game is over − there are four possible verdicts: the game should continue, the game ends with a tie, you win, or the computer wins;
#the computer responds with its move and the check is repeated;


board = [[1,2,3],[4,5,6],[7,8,9]]

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    row = '+---------+---------+---------+'
    col =  '|         |         |         |'

    for line in board:
        print(row)
        print(col)
        print('|    ' + str(line[0]) + '    |    ' + str(line[1]) + '    |    ' +str(line[2])+ '    |')
        print(col)
        print(row)


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    while True:
        try:
            new_mov = int(input('New move: '))
        
            if new_mov == 000:
                print('Bye!')
                break

            elif new_mov not in range(1, 11):
                print('Enter a right cell value!')

            else:
                for line in board:
                    for cell in line:
                        if cell == new_mov:
                            index = line.index(cell)
                            line[index] = 'X'
                            break
                display_board(board)
                break

        except ValueError:          
            print('Wrong type of data!')


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_board = copy.deepcopy(board)
    combined_free = []
    for line in free_board:
        for cell in line:
            if cell == 'X':
                line.remove('X')
            if cell == 'O':
                line.remove('O')

        combined_free += line

    return combined_free


def draw_move(board):
    # The function draws the computer's move and updates the board.
    combined_free = make_list_of_free_fields(board)
    random_mov = random.choice(combined_free)
    for line in board:
        for cell in line:
            if cell == random_mov:
                index = line.index(cell)
                line[index] = 'O'
                break
    print("Computer's move: "+str(random_mov))
    display_board(board)


print('/********************************************************************************\\')
print('/************************** Welcome to the Tic-Tac-Toe **************************\\')
print('/********************************************************************************\\')
display_board(board)
while len(make_list_of_free_fields(board)) > 4:
    enter_move(board)
    make_list_of_free_fields(board)
    draw_move(board)
    make_list_of_free_fields(board)
print('End! Who wins?')