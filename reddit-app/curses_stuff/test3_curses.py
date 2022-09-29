import curses
from curses import wrapper
import time


def main(stdscr):
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_MAGENTA)
    curses.init_pair(2, curses.COLOR_MAGENTA, curses.COLOR_RED)
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_MAGENTA)
    pair1 = curses.color_pair(1)
    pair2 = curses.color_pair(2)
    pair3 = curses.color_pair(3)

    stdscr.nodelay(True)

    x, y = 0, 0
    string_x = 0
    while True:
        try:
            key = stdscr.getkey()
        except:
            key = None

        if key == "KEY_LEFT":
            x -= 1
        elif key == "KEY_RIGHT":
            x += 1
        elif key == "KEY_UP":
            y -= 1
        elif key == "KEY_DOWN":
            y += 1

        stdscr.clear()

        string_x += 1
        stdscr.addstr(0, string_x//500, "hello_world")

        stdscr.addstr(y, x, "0")
        stdscr.refresh()
        time.sleep(0.5)


wrapper(main)
