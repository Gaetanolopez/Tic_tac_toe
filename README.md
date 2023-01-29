This is a script that plays a game of tic-tac-toe.

The display_board() function takes a board as an input and prints it out in a 3x3 grid format. 

The player_choose() function prompts the first player to choose either 'X' or 'O' as their marker.

The player1_choose() function assigns the second player the opposite marker of the first player.

The move_1() and move_2() functions prompt each player to select a number on the board to place their marker, and checks to make sure that the spot is not already taken.

The win() function checks if a player has won by getting 3 markers in a row, either horizontally, vertically, or diagonally.

The draw() function checks if the board is full and there is no winner.

The game starts by asking the user if they want to play and continues until the user decides to stop. 

If a player wins or there is a draw, the game ends and the player is prompted to play again.
