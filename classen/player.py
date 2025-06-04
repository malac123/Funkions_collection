import os
from colorama import Fore, Style, init
import time

class Player:
    def __init__(self, name, hp, power, mood):
        self.name = name
        self.hp = hp
        self.power = power
        self.__mood = mood
    @property
    def mood(self):
        return self.__mood
    
    def eat_shit(self):
        print("You just ate shit.")
        self.hp += 25
        self.power += 2
        self.__mood -= 95
        print(f"mood: {self.mood}, power: {self.power}, hp:{self.hp}.")
