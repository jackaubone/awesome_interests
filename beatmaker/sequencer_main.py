import time
import curses
from curses import curs_set, wrapper
from curses.textpad import Textbox, rectangle

import simpleaudio as sa

from pip import main


def main(stdscr):
    curs_set(0)

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
    # Set relative position of rectangle
    relx = (width//2) - (lenx//2)
    rely = (height//2) - (leny//2)

    # Create background pad
    bodypad = curses.newpad(leny, lenx)
    bodypad.bkgd(pair1)
    bodypad.refresh(0, 0, rely, relx, rely + leny, relx + lenx)


# region
# creates a pad per step of range, need to find a way to store each pad individually instead of overwriting pad1 so the time signature can be changed. pads.append adds each pad's instance id to pads array

    # Beat properties
    time_signature = 3
    by_eight = time_signature * 2

    tempo = 120
    counter = (60000 // tempo) / 1000

    # set padding margin on background
    margin = (lenx//by_eight)//2

    for i in range(10):

        # Visuals
        for j in range(by_eight):

            # wave_obj = sa.WaveObject.from_wave_file("808_cowbell.wav")
            # play_obj = wave_obj.play()

            pads = list()
            for k in range(by_eight):
                item = (lenx//by_eight) * k + margin
                y = rely + leny//2
                x = relx + item
                pad1 = curses.newpad(1, 1)
                pads.append(pad1)

                if k == j:
                    pad1.bkgd(pair3)
                    pad1.refresh(0, 0, y, x, y+1, x+1)
                else:
                    pad1.bkgd(pair2)
                    pad1.refresh(0, 0, y, x, y+1, x+1)

            time.sleep(counter)
            # y = rely + leny//2
            # x = relx + loc_x[k - 1]

            # pads[k].bkgd(pair1)
            # pads[k].refresh(0, 0, y, x, y+1, x+1)


# endregion

    bodypad.getch()

    # Set four beats


wrapper(main)

# print(pads)
