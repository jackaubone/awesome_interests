import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle
import time


def main(stdscr):
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_MAGENTA)
    curses.init_pair(2, curses.COLOR_MAGENTA, curses.COLOR_RED)
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_MAGENTA)
    pair1 = curses.color_pair(1)
    pair2 = curses.color_pair(2)
    pair3 = curses.color_pair(3)

    win = curses.newwin(3, 18, 2, 2)
    box = Textbox(win)

    rectangle(stdscr, 1, 1, 5, 20)
    stdscr.refresh()

    # ctrl-G to exit edit
    box.edit()
    text = box.gather().strip().replace("\n", "")

    stdscr.addstr(10, 40, text)

    stdscr.getch()


wrapper(main)
