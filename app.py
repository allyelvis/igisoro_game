class Igisoro:
    def __init__(self):
        self.board = [[2]*8, [2]*8]
        self.current_player = 0

    def print_board(self):
        for row in self.board:
            print(' '.join(map(str, row)))

    def move(self, row, col):
        stones = self.board[row][col]
        self.board[row][col] = 0
        r, c = row, col

        while stones > 0:
            c = (c + 1) % 8
            if c == 0:
                r = (r + 1) % 2
            if r == row and c == col:
                continue
            self.board[r][c] += 1
            stones -= 1

        if self.board[r][c] in [1, 2, 3] and r != row:
            self.capture(r, c)

    def capture(self, row, col):
        capture_amount = self.board[row][col]
        self.board[row][col] = 0
        r, c = row, col

        while capture_amount > 0:
            c = (c - 1) % 8
            if c == 7:
                r = (r - 1) % 2
            if self.board[r][c] in [1, 2, 3]:
                capture_amount += self.board[r][c]
                self.board[r][c] = 0
            capture_amount -= 1

    def check_winner(self):
        player_0_stones = sum(self.board[0])
        player_1_stones = sum(self.board[1])
        
        if player_0_stones == 0:
            return 1
        elif player_1_stones == 0:
            return 0
        else:
            return None

    def play_game(self):
        while True:
            self.print_board()
            print(f"Player {self.current_player + 1}'s turn")

            row = int(input("Select row (0 or 1): "))
            col = int(input("Select column (0 to 7): "))

            self.move(row, col)
            winner = self.check_winner()
            
            if winner is not None:
                print(f"Player {winner + 1} wins!")
                break
            
            self.current_player = (self.current_player + 1) % 2

if __name__ == "__main__":
    game = Igisoro()
    game.play_game()
