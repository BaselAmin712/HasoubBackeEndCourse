from game_of_life import *

running_game = gameOfLife(8)

while True:
    running_game.print_board()
    if input("do you want to populate a cell? yes/no?") == "yes":
        row, col = input("enter row and column separated by space (numbers between 0-8)\n").split()
        row = int(row)
        col = int(col)
        if row >= running_game.board_size or row < 0 or col >= running_game.board_size or col < 0:
            print("cell out of range!")
        else:
            running_game.populate_cell(row=row,col=col)
    else:
        break

rounds = int(input("how many rounds do you want to simulate?\n"))

running_game.play(rounds)

            