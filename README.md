# Sudoku
An interface to watch a sudoku get solved 

# Preview
![Alt text](sudoku_img.png?raw=True "Title")

# Goal
Fill in the grid such that each row, column and 3x3 box contains the digits from 1 to 9. Black digits are given at the beginning of the puzzle and can not be changed.

# Procedures
Currently, you can only add a sudoku to the test directory and then run the code with that input. To slow down the speed of the solver, increase the SPEED global, which will only reprint the screen every SPEED iterations, speeding up the process. I recommend changing SPEED in powers of 10 to see noticable change. 

# Reason for Creation
This is my most recent project, and I intend to extend the solver's capabilities to handle variant sudoku such as anti-knight or anti-king, sandwich sudoku or thermo sudoku. Sudoku has always been an interest of mine, with new types of logic still being discovered to this day, and so I wanted to combine my two passions of coding and sudoku into one. The solver runs a depth first search for a valid solution to the puzzle, however it does not guaruntee that the solution is unique. 
