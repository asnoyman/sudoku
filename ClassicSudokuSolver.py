# A program that solves a classic sudoku
# Adam Snoyman, adamsnoyman@gmail.com, September 2021
import pygame
from copy import deepcopy

pygame.display.set_caption("Classic Sudoku!")

# Colours used
WHITE = (230, 230, 230)
BLUE = (28, 98, 255)
BLACK = (0,0,0)

EMPTY = 0

GRID_SIZE = 9
CELL_SIZE = 75

FPS = 60
SPEED = 1

counter = 0

class Board:
    def __init__(self, cells):
        self.cells = cells
        self.rows = [set() for _ in range(9)]
        self.cols = [set() for _ in range(9)]
        self.boxes = [set() for _ in range(9)]

class Cell:
    def __init__(self, value, given, row, col):
        self.value = value
        self.given = given
        self.row = row
        self.col = col
        self.box = 3 * (row // 3) + col // 3


def board_create(file):
    file = open(file, "r")
    cells = []
    for i in range(GRID_SIZE):
        a = []
        for j in range(GRID_SIZE):
            value = int(file.read(1))
            if value != EMPTY:
                cell = Cell(value, True, i, j)
            else:
                cell = Cell(value, False, i, j)
            a.append(cell)
        cells.append(a)
        file.read(1)

    board = Board(cells)
    for row in board.cells:
        for cell in row:
            if cell.given:
                board.rows[cell.row].add(cell.value)
                board.cols[cell.col].add(cell.value)
                board.boxes[cell.box].add(cell.value)
    return board


def draw_background(window):
    window.fill(WHITE)
    for i in range(1, GRID_SIZE):
        hor_line = pygame.Rect(0, i * CELL_SIZE, GRID_SIZE * CELL_SIZE, 1)
        vert_line = pygame.Rect(i * CELL_SIZE, 0, 1, GRID_SIZE * CELL_SIZE)
        if i % 3 == 0:
            pygame.draw.rect(window, BLACK, pygame.Rect.inflate(hor_line, 1, 3))
            pygame.draw.rect(window, BLACK, pygame.Rect.inflate(vert_line, 3, 1))
        else:
            pygame.draw.rect(window, BLACK, hor_line)
            pygame.draw.rect(window, BLACK, vert_line)

def draw_board(window, board):
    draw_background(window)
    for row in board.cells:
        for cell in row:
            if cell.value != EMPTY:
                font = pygame.font.Font('freesansbold.ttf', CELL_SIZE)
                if cell.given:
                    text = font.render(str(cell.value), True, BLACK)
                else:
                    text = font.render(str(cell.value), True, BLUE)

                window.blit(text, (cell.col * CELL_SIZE + 18, cell.row * CELL_SIZE + 5))
    pygame.display.flip()
    pygame.event.pump()

def check_solved(board):
    if any([len(row) != GRID_SIZE for row in board.rows]):
        return False
    if any([len(col) != GRID_SIZE for col in board.cols]):
        return False
    if any([len(box) != GRID_SIZE for box in board.boxes]):
        return False
    return True

def valid_move(board, cell, num):
    # Checks if position already filled (0 corresponds to empty cell)
    if cell.given:
        return False

    # Checks if num already in row
    if num in board.rows[cell.row]:
        return False

    # Checks if num is already in col
    if num in board.cols[cell.col]:
        return False

    # Checks if num is already in the of 3 x 3 box which cell is in
    if num in board.boxes[cell.box]:
        return False

    return True

def solve_sudoku(window, board):
    if check_solved(board):
        draw_board(window, board)
        return

    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if board.cells[i][j].value == EMPTY:
                for num in range(1, 10):
                    if valid_move(board, board.cells[i][j], num):
                        global counter
                        counter += 1
                        try:
                            board.cells[i][j].value = num
                            board.rows[i].add(num)
                            board.cols[j].add(num)
                            board.boxes[3 * (i // 3) + (j // 3)].add(num)
                            if counter == SPEED:
                                counter = 0
                                draw_board(window, board)
                            return solve_sudoku(window, board)
                        except:
                            board.cells[i][j].value = EMPTY
                            board.rows[i].remove(num)
                            board.cols[j].remove(num)
                            board.boxes[3 * (i // 3) + (j // 3)].remove(num)
                raise ValueError(description=f"No available moves")


def main():
    pygame.init()
    window = pygame.display.set_mode((GRID_SIZE * CELL_SIZE, GRID_SIZE * CELL_SIZE))
    sudoku = "tests/" + input("Provide a sudoku please: ")
    board = board_create(sudoku)
    draw_board(window, board)

    try:
        solve_sudoku(window, board)
        print("Finished! Enjoy the solution :)")
    except:
        print("Unsolvable sudoku :(")


    clock = pygame.time.Clock()

    run = True
    while run:
        for event in pygame.event.get():
            clock.tick(FPS)
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()

if __name__ == "__main__":
    main()
