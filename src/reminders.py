import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../include"))

import tGame
import KEY, CONTROLS
from Menu import *
from Entity import Creature
import Calendar

import time


class QuarterToApp:

    def __init__(self):
        tGame.hideCursor()
        tGame.disableLineWrap()

        tGame.setTitle("Quarter-To ToDo")
        tGame.screenClear()

        tGame.renderCopy()

    def run(self):
        pass
        

class Grid:
    pass



def main():

# Start
    try:
        tGame.init()
        key_input = tGame.KeyboardInput()

        tGame.render("\033]0;Quarter-To TO-DO\x07")
        tGame.screenClear()
        tGame.renderCopy()

# Start main loop
        todo_app = QuarterToApp()
        exit_status = todo_app.run_loop(key_input)

        tGame.screenClear()
        
        if exit_status != KEY.QUIT:
            tGame.render("\033[1;1H" + str(exit_status))
        
        tGame.renderCopy()

    finally:
        if tGame.POSIX:
            import tty, termios
            termios.tcsetattr(tGame.fd,termios.TCSADRAIN, tGame.old_settings)

if __name__ == "__main__":
    try:
        tGame.init()
        App = QuarterToApp()
    finally:
        if tGame.POSIX:
            tGame.end()
    
    tGame.render("\033[1;1H")
    tGame.screenClear()
    tGame.renderCopy()
