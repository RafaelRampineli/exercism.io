import random   #https://www.pythonforbeginners.com/random/how-to-use-the-random-module-in-python
from datetime import datetime
from string import ascii_uppercase as alph, digits as dig
import time

class Robot(object):

    @classmethod
    def get_name(cls):
        time.sleep(0.1)
        random.seed(datetime.now())
        return ''.join(random.choice(code_name) for code_name in (alph, alph, dig, dig, dig))

    def reset(self):
        self.name = Robot.get_name()
        return self.name

    def __init__(self):
        self.name = self.reset()

