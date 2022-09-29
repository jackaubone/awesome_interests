import time
from time import time
import curses
from curses import curs_set, wrapper
from curses.textpad import Textbox, rectangle

import simpleaudio as sa

from pip import main


def main(stdscr):
    curs_set(0)
    stdscr.nodelay(True)

    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_RED)
    curses.init_pair(2, curses.COLOR_MAGENTA, curses.COLOR_YELLOW)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLUE)

    pair1 = curses.color_pair(1)
    pair2 = curses.color_pair(2)
    pair3 = curses.color_pair(3)

    # Get dimensions of terminal
    height, width = stdscr.getmaxyx()
    # Set length of sides
    lenx = 100
    leny = 5
    # margin for any ui stuff to add
    ui_y_margin = 5
    # Set relative position of rectangle
    relx = (width//2) - (lenx//2)
    rely = (height//4) - (leny//2) - ui_y_margin

    # Create background pad
    bodywindow = curses.newwin(leny, lenx)
    bodywindow.bkgd(pair1)
    bodywindow.refresh()


# region
# creates a pad per step of range, need to find a way to store each pad individually instead of overwriting pad1 so the time signature can be changed. pads.append adds each pad's instance id to pads array

    # Beat properties
    time_signature = 4
    by_eight = time_signature * 2

    tempo = 120
    counter = (60000 // tempo) / 1000

    # set padding margin on background
    margin = (lenx//by_eight)//2

    cursx, cursy = 0, 0
    init_time = time()
    while True:

        for j in range(by_eight):
            # wave_obj = sa.WaveObject.from_wave_file("808_cowbell.wav")
            # play_obj = wave_obj.play()
            pads = list()
            location_list = list()
            # Visuals

            while True:
                bodywindow.clear()
                curses.doupdate()

                if time() >= init_time + counter:
                    init_time = time()
                    for k in range(by_eight):
                        item = (lenx//by_eight) * k + margin
                        y = rely + leny//2
                        x = relx + item
                        pad1 = curses.newpad(100, 100)
                        pad_location = (0, 0, y, x, y+1, x+1)
                        location_list.append(pad_location)

                        if k == j:
                            pad1.bkgd(pair3)
                            pad1.refresh(0, 0, y, x, y+1, x+1)

                        else:
                            pad1.bkgd(pair2)
                            pad1.refresh(0, 0, y, x, y+1, x+1)

                    break
                  # delay(counter)

                else:

                    try:
                        key = stdscr.getkey()
                    except:
                        key = None

                    if key == "KEY_LEFT":
                        cursx -= 1
                    elif key == "KEY_RIGHT":
                        cursx += 1
                    elif key == "KEY_UP":
                        cursy -= 1
                    elif key == "KEY_DOWN":
                        cursy += 1
                    # bodywindow.addstr(cursy, cursx, "^")

                for h, item, in enumerate(pads):
                    pad1.refresh(item[0], item[1], item[2],
                                 item[3], item[4], item[6])
                testpad = curses.newwin(1000, 1000)
                testpad.bkgd(pair1)
                testpad.addstr(cursy, cursx, "^")
                testpad.addstr(0, 0, str(init_time))
                testpad.addstr(0, 20, str(time()))

                testpad.refresh()

            # y = rely + leny//2
            # x = relx + loc_x[k - 1]

            # pads[k].bkgd(pair1)
            # pads[k].refresh(0, 0, y, x, y+1, x+1)


# endregion

    bodypad.getch()

    # Set four beats


def delay(secs):
    init_time = time()
    while time() < init_time+secs:
        pass


wrapper(main)

# print(pads)
