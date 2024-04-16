import random
import tkinter as tk
#number puzzel.
# Function to create a shuffled game board
def create_board():
    numbers = list(range(1, 9))
    numbers.append(0)
    random.shuffle(numbers)
    board = [numbers[i:i+3] for i in range(0, 9, 3)]
    return board

# Function to handle move button click
def move_number(i, j):
    global board
    empty_i, empty_j = find_empty_slot(board)
    if (i == empty_i and abs(j - empty_j) == 1) or (j == empty_j and abs(i - empty_i) == 1):
        board[empty_i][empty_j], board[i][j] = board[i][j], board[empty_i][empty_j]
        update_board()


# Function to find the position of the empty slot (0)
def find_empty_slot(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return i, j

# Function to update the GUI with the current game board
def update_board():
    global buttons, board
    for i in range(3):
        for j in range(3):
            if board[i][j] != 0:
                buttons[i][j].config(text=str(board[i][j]), state=tk.NORMAL,
                                     command=lambda i=i, j=j: move_number(i, j))
            else:
                buttons[i][j].config(text="", state=tk.DISABLED)

# Main function to run the game
def main():
    global buttons, board
    board = create_board()

    root = tk.Tk()
    root.title("Number Puzzle Game")

    buttons = [[None]*3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            if board[i][j] != 0:
                buttons[i][j] = tk.Button(root, text=str(board[i][j]), width=5, height=2,
                                           command=lambda i=i, j=j: move_number(i, j))
            else:
                buttons[i][j] = tk.Button(root, text="", state=tk.DISABLED, width=5, height=2)
            buttons[i][j].grid(row=i, column=j)

    root.mainloop()

if __name__ == "__main__":
    main()
