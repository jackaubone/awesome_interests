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

# region

    # counter_win = curses.newwin(1, 20, 10, 10)
    # stdscr.addstr(3, 10, "hello buddy")
    # stdscr.refresh()

    # for i in range(100):
    #     counter_win.clear()
    #     color = pair1

    #     if i % 2 == 0:
    #         color = pair2

    #     counter_win.addstr(f"hello world, {i}", color)
    #     counter_win.refresh()
    #     time.sleep(0.1)
# endregion
    pad = curses.newpad(100, 100)
    stdscr.refresh()

    for i in range(100):
        for j in range(26):
            char = chr(67 + j)
            pad.addstr(char, pair3)

    pad.refresh(0, 0, 5, 5, 20, 25)
    time.sleep(0.1)

    stdscr.getch()


wrapper(main)
