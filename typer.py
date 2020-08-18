from time import *
from os import remove 
from random import choice

import os
import pyautogui

def tab(): pyautogui.hotkey('ctrl', 'tab')
def write(sent, endsleep): 
    pyautogui.write(sent, interval=0.03)
    pyautogui.press('enter')
    sleep(endsleep)

# ggwp4: general events
# ggwp3: pls hunt
# ggwp2: pls search
# ggwp : pls fish

# Event detections
ITERATION = 0
def generalEventDetection(n):
    if os.path.exists('ggwp4.txt'):
        with open('ggwp4.txt', 'r', encoding='utf-8') as f:
            typeEvent = f.readline()
            if len(typeEvent) > 0:
                for _ in range(n): 
                    write(typeEvent, 0.7); tab()
    
        remove('ggwp4.txt')

def pmDetection(n, tc):
    for _ in range(n):
        if ITERATION > 0 and ITERATION % 10 == 0:
            for text in ['pls with 1500', 'pls buy laptop', 'pls pm', choice(list('nerd'))]:
                write(text, 0.25)
        else:
            for text in ['pls pm', choice(list('nerd'))]:
                write(text, 1)
        
        if _ == 0: tc()
        tab()

def huntDetection(n, tc): 
    for _ in range(n):
        write('pls hunt', 1.5)
        if os.path.exists('ggwp3.txt'):
            with open('ggwp3.txt', 'r', encoding='utf-8') as f:
                typingWarning = f.readline()
                if len(typingWarning):
                    write(typingWarning, 0.7)
                
            remove('ggwp3.txt')
        if _ == 0: tc()
        tab()

def fishDetection(n, tc):
    for _ in range(n):
        write('pls fish', 2)
        if os.path.exists('ggwp.txt'):
            with open('ggwp.txt', 'r', encoding='utf-8') as f:
                typingWarning = f.readline()
                if len(typingWarning):
                    write(typingWarning, 0.7)
                
            remove('ggwp.txt')
        if _ == 0: tc()
        tab()

def searchDetection(n, tc):
    for _ in range(n):
        write('pls search', 2)
        with open('ggwp2.txt', 'r', encoding='utf-8') as f:
            searchOption = f.readline()
            write(searchOption, 1)
        if _ == 0: tc()
        tab()
    
 
def deposit(n, tc):
    for _ in range(n):
        write('pls dep all', 1); tab()
        if _ == 0: tc()

def beg(n, tc):
    for _ in range(n):
        write('pls beg', 1); tab()
        if _ == 0: tc()

# Command Timing Class
class CommandExecutor:
    def __init__(self, command, accounts: int, timer: int):
        """
        :type func: command, function to execute which will type the command
        :type int: timer, how long to wait until the command can be typed again
        :type int: current_lag_time, time between current time and time until we can execute the command again
        :type int: accounts, number of accounts ( will be required to know how many times to tab )
        """

        self.command          = command
        self.timer            = timer
        self.accounts         = accounts

        self.time_completed   = 0        
        self.current_lag_time = 0
    
    def set_time_completed(self):
        self.time_completed = time()

    def execute(self):
        sleep(self.current_lag_time)
        generalEventDetection(self.accounts)
        
        self.command(self.accounts, self.set_time_completed)
        
        generalEventDetection(self.accounts)
    
    def update(self):
        ct = time()
        self.current_lag_time = (0, self.time_completed + self.timer - ct)[self.time_completed + self.timer - ct >= 0]
        print(self.current_lag_time, self.command.__name__)

# MAIN
accounts = 3
lfuncs = {
    beg: 25,
    pmDetection: 58,    
    huntDetection: 59,
    fishDetection: 43,
    deposit: 0,
    searchDetection: 28
}

mapped = [CommandExecutor(func, accounts, time) for func, time in lfuncs.items()]

sleep(5)
while True:
    for class_ in mapped:
        class_.update(); class_.execute()
    
    ITERATION += 1
