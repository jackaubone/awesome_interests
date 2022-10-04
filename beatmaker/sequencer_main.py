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
    curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_GREEN)

    pair1 = curses.color_pair(1)
    pair2 = curses.color_pair(2)
    pair3 = curses.color_pair(3)
    pair4 = curses.color_pair(4)

    # Get dimensions of terminal
    height, width = stdscr.getmaxyx()
    # Set length of sides
    lenx = 100
    leny = 1
    # margin for any ui stuff to add
    ui_y_margin = 5
    # Set relative position of rectangle
    relx = (width//2) - (lenx//2)
    rely = (height//4) - (leny//2) - ui_y_margin

    menu_rely = rely + 3
    menu_relx = relx


# region
# creates a pad per step of range, need to find a way to store each pad individually instead of overwriting pad1 so the time signature can be changed. pads.append adds each pad's instance id to pads array

    # Beat properties
    time_signature = 4
    by_eight = time_signature * 2

    tempo = 120
    counter = (60000 // tempo) / 1000

    #channels = 4

    # cursor location and size of movement spaces
    cursx, cursy = 0, 0
    stepsize = (lenx//by_eight)
    real_len = lenx - stepsize

    bodywindow = curses.newwin(leny, real_len)
    bodywindow.bkgd(pair1)
    bodywindow.refresh()

    init_time = time()
    trigger_list = [0] * by_eight
    while True:

        for j in range(by_eight):
            wave_obj = sa.WaveObject.from_wave_file("808_cowbell.wav")

            if trigger_list[j] == 1:
                play_obj = wave_obj.play()

            pads = list()
            location_list = list()
            # Visuals

            while True:
                metronome_win = curses.newwin(1, 2)
                bodywindow.clear()
                curses.doupdate()
                item = lenx//by_eight + stepsize
                y = rely + leny//2
                x = relx + item

                if time() >= init_time + counter:

                    init_time = time()
                    for k in range(by_eight):

                        item = (lenx//by_eight) * k
                        y = rely + leny//2
                        x = relx + item

                        pad_location = (y, x)
                        location_list.append(pad_location)

                        if k == j:
                            metronome_win.bkgd(pair3)
                            metronome_win.mvwin(y, x)
                            metronome_win.noutrefresh()
                        elif trigger_list[k] == 1:
                            metronome_win.bkgd(pair4)
                            metronome_win.mvwin(y, x)
                            metronome_win.noutrefresh()

                        else:
                            metronome_win.bkgd(pair2)
                            metronome_win.mvwin(y, x)
                            metronome_win.noutrefresh()
                        curses.doupdate()

                    break

                try:
                    key = stdscr.getkey()
                except:
                    key = None

                if key == "KEY_LEFT":
                    if cursx <= 0:
                        cursx = real_len - 4
                    else:
                        cursx -= stepsize
                elif key == "KEY_RIGHT":
                    if cursx >= real_len - stepsize:
                        cursx = 0
                    else:
                        cursx += stepsize
                elif key == "KEY_UP":
                    trigger_list[j] = 1

                testpad = curses.newwin(1, 100)
                testpad.bkgd(pair1)
                testpad.addstr(0, 0, str(init_time))
                testpad.addstr(0, 20, str(time()))
                testpad.addstr(0, 40, str(cursx))
                testpad.addstr(0, 60, str(trigger_list[j]))

                bodywindow.mvwin(menu_rely-1, menu_relx)
                bodywindow.addstr(0, cursx, "$")

                testpad.noutrefresh()
                bodywindow.noutrefresh()
                metronome_win.noutrefresh()

                curses.doupdate


# endregion
wrapper(main)
