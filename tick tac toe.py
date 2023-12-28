import tkinter as tk
from tkinter import messagebox

class TicTacToeGUI:
    def __init__(self):
    # Welcome to the Tic Tac Toe GUI implementation in Python using tkinter!

        # We start by creating the main window for our game.
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")

        # We initialize the current player; it starts with 'X'.
        self.current_player = 'X'

        # Now, let's create a 3x3 grid of buttons using a nested list.
        self.buttons = [[None, None, None] for _ in range(3)]

        # Time to create and place buttons in the grid.
        for i in range(3):
            for j in range(3):
                # Each button is a tkinter Button widget.
                # The lambda function ensures that the correct row and column are passed to on_button_click.
                self.buttons[i][j] = tk.Button(self.window, text='', font=('normal', 20), width=5, height=2,
                                               command=lambda row=i, col=j: self.on_button_click(row, col))
                # We use the grid method to place buttons in the respective rows and columns.
                self.buttons[i][j].grid(row=i, column=j)

    def on_button_click(self, row, col):
        # This method is triggered when a button is clicked.

        # Check if the clicked button is empty and the game is still ongoing.
        if self.buttons[row][col]['text'] == '' and not self.check_winner() and not self.is_board_full():
            # Set the text of the clicked button to the current player ('X' or 'O').
            self.buttons[row][col]['text'] = self.current_player

            # Check for a winner after the move.
            if self.check_winner():
                self.show_winner_message()

            # Check for a tie after the move.
            elif self.is_board_full():
                self.show_tie_message()

            else:
                # Switch to the other player for the next turn.
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self):
        # This function checks for a winner by examining rows, columns, and diagonals.

        for i in range(3):
            # Check rows and columns for a win.
            if all(self.buttons[i][j]['text'] == self.current_player for j in range(3)) or \
                    all(self.buttons[j][i]['text'] == self.current_player for j in range(3)):
                return True

        # Check diagonals for a win.
        if all(self.buttons[i][i]['text'] == self.current_player for i in range(3)) or \
                all(self.buttons[i][2 - i]['text'] == self.current_player for i in range(3)):
            return True

        # No winner found.
        return False

    def is_board_full(self):
        # Check if the board is full (a tie) by checking all buttons.
        return all(self.buttons[i][j]['text'] != '' for i in range(3) for j in range(3))

    def show_winner_message(self):
        # Display a message box indicating the winner.
        messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} wins!")

    def show_tie_message(self):
        # Display a message box indicating a tie.
        messagebox.showinfo("Tic Tac Toe", "It's a tie!")

    def run(self):
        # Run the main loop of the GUI.
        self.window.mainloop()

# If this script is executed, create an instance of the TicTacToeGUI class and run the game.
if __name__ == "__main__":
    game = TicTacToeGUI()
    game.run()
