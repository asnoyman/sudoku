# Sudoku
An interface to watch a sudoku get solved 

# Preview
![Alt text](sudoku_img.png?raw=True "Title")

# Goal
Fill in the grid such that each row, column and 3x3 box contains the digits from 1 to 9. Black digits are given at the beginning of the puzzle and can not be changed.

# Procedures
The solver runs an depth first search for a valid solution to the puzzle. Currently, you can only add a sudoku to the test directory and then run the code with that input - rather than building your own sudoku using the GUI. To slow down the speed of the solver, increase the SPEED global, which will only reprint the screen every SPEED iterations, speeding up the process. I recommend changing SPEED in powers of 10 to see noticable change. 
