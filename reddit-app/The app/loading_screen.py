
import time
import curses
from curses import curs_set, wrapper
from curses.textpad import Textbox, rectangle


def main(stdscr):
    curs_set(0)

    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_MAGENTA, curses.COLOR_BLUE)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_RED)
    pair1 = curses.color_pair(1)
    pair2 = curses.color_pair(2)
    pair3 = curses.color_pair(3)


# region
    # # stdscr.attron(pair1)
    # # stdscr.box(500, 95)
    # # stdscr.attroff(pair1)

    # win = curses.newwin(20, 50, 2, 5)
    # win.addstr(5, 5, "Hello, world!", pair2)

    # win.attron(pair1)
    # win.border()
    # win.attroff(pair1)

    # rectangle(win, 1, 1, 8, 30)
    # win.hline(2, 5, 0, 100)
    # win.bkgd(pair3)
# endregion
# region

    # # example of setting window background
    # win1 = curses.newwin(10, 10, 10, 10)
    # win1.box('|', '-')
    # win1.bkgd(pair3)
# endregion

    # win.getch()
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
# region
# LOADING ANIMATION

    # Get length of sides
    lenx = 30
    leny = 5

    # Get dimensions of terminal and set relative position of rectangle
    height, width = stdscr.getmaxyx()
    relx = (width//2) - (lenx//2)
    rely = (height//2) - (leny//2)

    # Initiate rectangle pad and add border
    bodypad = curses.newpad(leny, lenx)
    stdscr.refresh()
    bodypad.bkgd(pair1)
    bodypad.attron(pair1)
    bodypad.border()

    # Insert the message and center it in the box
    message = "Loading..."
    stringy = leny//2
    stringx = lenx//2 - (len(message)//2)
    bodypad.addstr(stringy, stringx, message)
    bodypad.attroff(pair1)

    stdscr.bkgd(pair1)
    stdscr.refresh()
    # #refresh location of pad
    # bodypad.refresh(0, 0, rely, relx, rely + leny, relx + lenx)

    # create the pad which animates around bodypad's perimeter
    animepad = curses.newpad(leny, lenx)
    animepad.bkgd(pair1)

    # Initialize array which holds direction values
    direction = [leny, lenx, leny * -1, lenx * -1]

    # Temporary loop
    for i in range(100):
        stdscr.clear()
        stdscr.refresh()
        y = rely
        x = relx
        # Loop through the four directions
        for k in range(0, 4):

            # The two positive directions
            if k < 2:
                for j in range(direction[k]):
                    # Get height and width of terminal, and the relative position of box
                    height, width = stdscr.getmaxyx()
                    relx = (width//2) - (lenx//2)
                    rely = (height//2) - (leny//2)
                    stdscr.clear()
                    stdscr.refresh()
                    if direction[k] == leny:
                        x = relx
                        y = rely - 1 + j
                        bodypad.refresh(0, 0, rely, relx,
                                        rely + leny, relx + lenx)
                        animepad.refresh(0, 0, y, x, y + 1, x + 1)
                    elif direction[k] == lenx:
                        x = relx + j
                        y = rely - 1 + leny
                        bodypad.refresh(0, 0, rely, relx,
                                        rely + leny, relx + lenx)
                        animepad.refresh(0, 0, y, x, y + 1, x + 4)
                    time.sleep(0.05)

            # The two negative directions
            elif k >= 2:
                for j in range(0, direction[k] + 1, -1):
                    height, width = stdscr.getmaxyx()
                    relx = (width//2) - (lenx//2)
                    rely = (height//2) - (leny//2)
                    stdscr.clear()
                    stdscr.refresh()
                    if direction[k] == leny * -1:
                        x = relx - 1 + lenx
                        y = rely - 2 + leny + j
                        bodypad.refresh(0, 0, rely, relx,
                                        rely + leny, relx + lenx)
                        animepad.refresh(0, 0, y, x, y + 1, x + 1)
                    elif direction[k] == lenx * -1:
                        x = relx - 1 + lenx + j
                        y = rely - 1
                        bodypad.refresh(0, 0, rely, relx,
                                        rely + leny, relx + lenx)
                        animepad.refresh(0, 0, y, x, y + 1, x + 4)
                    time.sleep(0.05)

# endregion
    stdscr.refresh()
    stdscr.getch()


wrapper(main)
