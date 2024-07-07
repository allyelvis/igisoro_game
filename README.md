Here’s a basic implementation of the Igisoro game in Python. This code includes setting up the board, allowing players to make moves, and determining the winner.

```python
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
```

### Explanation:

1. **Class Initialization**:
    - `__init__`: Sets up the board with 2 stones in each of the 16 holes, and starts with player 0.

2. **Board Display**:
    - `print_board`: Prints the current state of the board.

3. **Player Move**:
    - `move`: Executes a player's move by picking up all the stones in the selected hole and distributing them one by one in subsequent holes. If the last stone lands in a hole with 1, 2, or 3 stones and it's in the opponent's row, the player captures those stones.

4. **Capture Mechanism**:
    - `capture`: Handles the logic for capturing stones.

5. **Check for Winner**:
    - `check_winner`: Determines if a player has won by checking if the opponent has no stones left.

6. **Main Game Loop**:
    - `play_game`: Runs the game, alternating between players until one player wins.

You can run this script in a Python environment to play the game. The game logic can be extended and refined further as needed.
