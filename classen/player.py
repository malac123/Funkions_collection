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
    @mood.setter
    def mood(self, new_mood):
        if new_mood > 0:
            self.__mood = new_mood
        else:
            raise ValueError("Mood kann nicht negativ sein")
    
    def eat_feces(self):
        print("You just ate shit.")
        self.hp += 25
        self.power += 2
        self.mood -= 95
        print(f"mood: {self.mood}, power: {self.power}, hp:{self.hp}.")
        

