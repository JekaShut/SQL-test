from framework.Base.BaseElement import *
import pyautogui
import os
import time
import random

from random import choice
from string import ascii_lowercase, ascii_uppercase
from string import digits


FILES = jsonGetter.GetJson.getFile(CONFIG, "Files")


class SysOperations:
    @staticmethod
    def upload(file):
        time.sleep(2)
        path = os.getcwd() + FILES + file
        pyautogui.write(path)
        pyautogui.press('enter')

    @staticmethod
    def generate_string(x):
        string = [choice(ascii_uppercase + ascii_lowercase + ascii_lowercase + digits) for i in range(x)]
        random.shuffle(string)
        string = "".join(string)
        return string