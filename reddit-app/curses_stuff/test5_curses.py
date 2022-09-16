import curses
import time
stdscr = curses.initscr()
curses.cbreak()
curses.noecho()
stdscr.keypad(1)

try:
# Run your code here
    height,width = stdscr.getmaxyx()
    num = min(height,width)
    for x in range(num):
        stdscr.addch(x,x,'X')
    stdscr.refresh()
    time.sleep(3)
finally:
    curses.nocbreak()
    stdscr.keypad(0)
    curses.echo()
    curses.endwin()