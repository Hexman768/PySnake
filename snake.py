import curses
import time
import sys
from random import randint


class Snake:
    def __init__(self, x, y):
        self.body = [[y+1,  x], [y, x]]
        self.dir = curses.KEY_DOWN

    def move(self):
        # Pop last item in list
        self.body.pop()

        x = self.body[0][1]
        y = self.body[0][0]

        # Insert new vector at idx 0 based on dir
        if self.dir == curses.KEY_RIGHT:
            self.body.insert(0, [y, x+1])
        elif self.dir == curses.KEY_LEFT:
            self.body.insert(0, [y, x-1])
        elif self.dir == curses.KEY_UP:
            self.body.insert(0, [y-1, x])
        elif self.dir == curses.KEY_DOWN:
            self.body.insert(0, [y+1, x])

    def grow(self):
        x = self.body[len(self.body) - 1][1]
        y = self.body[len(self.body) - 1][0]

        if self.dir == curses.KEY_RIGHT:
            self.body.append([y, x - 1])
        elif self.dir == curses.KEY_LEFT:
            self.body.append([y, x + 1])
        elif self.dir == curses.KEY_UP:
            self.body.append([y + 1, x])
        elif self.dir == curses.KEY_DOWN:
            self.body.append([y - 1, x])

    def check_key(self, key):
        if key == curses.KEY_ENTER or key == 10 or key == 13:
            sys.exit()
        elif key == curses.KEY_LEFT:
            self.dir = curses.KEY_LEFT
        elif key == curses.KEY_RIGHT:
            self.dir = curses.KEY_RIGHT
        elif key == curses.KEY_UP:
            self.dir = curses.KEY_UP
        elif key == curses.KEY_DOWN:
            self.dir = curses.KEY_DOWN

    def check_apple_collision(self, apple):
        if self.body[0][0] == apple.y and self.body[0][1] == apple.x:
            return True
        return False

    def check_wall_collision(self, rows, cols):
        # we gotta put some logic here
        if self.body[0][0] < 0 or self.body[0][0] > rows - 1 or self.body[0][1] < 0 or self.body[0][1] > cols - 1:
            return True
        return False


class Apple:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Board:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.tokens = {0: ' . ', 1: ' # ', 2: ' @ '}
        self.board = [[0 for i in range(self.cols)] for j in range(self.rows)]

    def print_board(self, stdscr, snake, apple):
        self.board = [[0 for i in range(self.cols)] for j in range(self.rows)]

        # set snake in board
        for i, j in snake.body:
            print("LOG: Setting i: {} and j: {} to 1\n".format(i, j))
            if i < 0:
                i = self.rows - 1
            elif i > self.rows - 1:
                i = 0

            if j < 0:
                j = self.cols - 1
            elif j > self.cols - 1:
                j = 0

            self.board[i][j] = 1

        self.board[apple.y][apple.x] = 2

        # print board to stdout
        for i in range(len(self.board)):
            row = ""
            for j in range(len(self.board[i])):
                row += self.tokens[self.board[i][j]]
            stdscr.addstr(i, 0, row)


def main(stdscr):
    curses.noecho()
    a_x = randint(0, 9)
    a_y = randint(0, 9)

    rows = 10
    cols = 10
    board = Board(rows, cols)
    snake = Snake(5, 0)
    apple = Apple(a_x, a_y)

    stdscr.timeout(0)

    while True:
        board.print_board(stdscr, snake, apple)
        key = stdscr.getch()
        snake.check_key(key)
        if snake.check_apple_collision(apple):
            snake.grow()
            apple = Apple(randint(0, 9), randint(0, 9))

        if snake.check_wall_collision(rows, cols):
            sys.exit(0)

        snake.move()

        stdscr.refresh()
        time.sleep(.2)


if __name__ == "__main__":
    curses.wrapper(main)
