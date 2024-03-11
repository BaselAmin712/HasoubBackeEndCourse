import copy


class gameOfLife:
    def __init__(self, board_size):
        self.board_size = board_size
        self.board = [[0 for i in range(board_size)] for i in range(board_size)]

    def print_board(self):
        for i in range(self.board_size):
            print(self.board[i])
    
    def populate_cell(self, row, col):
        self.board[row][col] = 1

    def unpopulate_cell(self, row, col):
            self.board[row][col] = 0

    def next_round(self):
        lastBoard = copy.deepcopy(self.board)
        for row in range(self.board_size):
            for col in range(self.board_size):
                neighbors_num = self.get_neighbors_num(lastBoard, col, row)
                if neighbors_num < 2 or neighbors_num > 3:
                    self.unpopulate_cell(row, col)
                elif neighbors_num == 3:
                    self.populate_cell(row=row,col=col)
    
    def is_legal_cell(self,row,col):
        if row >= self.board_size or row < 0 or col >= self.board_size or col < 0:
            return False
        return True

    def get_neighbors_num(self, lastBoard, col, row):
        moves = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        neighbors_num = 0
        for move in moves:
            if self.is_legal_cell(row + move[0], col + move[1]) \
            and lastBoard[row + move[0]][col + move[1]]:
                neighbors_num += 1
        return neighbors_num

    def play(self, rounds):
        for round in range(rounds):
            self.next_round()
            print("\n************************\n")
            self.print_board()