import os
from colorama import Fore, Style, init
import time 
from classen.player import Player

leo = Player(
    name ="leo",
    hp = 100,
    power = 50,
    mood = 100
)

def main():
    print(leo.name)

base_collor = Fore.LIGHTGREEN_EX


def input_menu(menu_items: list) -> int:
    """
    You put a list containing as many opitions as you want 
    input_menu([Attack, Use Items])
    
    this method creates a Menu from wich the player chooses one option 
    1.Attac 
    2.Use Items
    Using the Num pad the user Inputs a nuber wich gets returnd
    This Int can be uese to trigger ifttt commands

    action = input_menu(["Attack ","Use Item"])
        if action == 1:
            doese damage to the enemy

    The method also is Protected agains Dumm inputs like "asdghwiupezhaq"
    it will call an error to the use asking hin not to be stupid
    """
    while True:
        for i, item in enumerate(menu_items):
            print(f"{Fore.LIGHTGREEN_EX}{i + 1}. {item}")
        print(Fore.WHITE + "Select your choice...")
        answer_str = input(Fore.WHITE + ">").strip()
        try:
            answer_int = int(answer_str)
            if 1 <= answer_int <= len(menu_items):
                return answer_int
            else:
                p(f"{Fore.LIGHTRED_EX}Invalid Input. Please enter a number from 1 to {len(menu_items)}.{Style.RESET_ALL}")
        except ValueError:
            p(f"{Fore.LIGHTRED_EX}Invalid Input. Please enter a number.{Style.RESET_ALL}")



def wait():
    """
    Uesecase: 
                -Makes Text readable

    It prints the String "Press Emter to Continue"
    and then waits until the user presses Enter
    """
    print("")
    print(Fore.WHITE + "Press Enter to continue")
    input(Fore.WHITE + ">")
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def remove_ansi_codes(text):
    result = ""
    i = 0
    while i < len(text):
        if text[i] == '\x1b':  # ANSI Escape start
            while i < len(text) and text[i] != 'm':
                i += 1
            i += 1
        else:
            result += text[i]
            i += 1
    return result

def box_print(text_farbe, text_lines):
    max_len = max(len(remove_ansi_codes(line)) for line in text_lines)
    breite = max_len + 2

    # Store the actual text lines without initial ANSI codes for proper slicing
    clean_lines = [remove_ansi_codes(line) for line in text_lines]

    for step in range(max_len):
        clear_terminal() # Clear inside the loop for animated effect
        print("┌" + "─" * breite + "┐")
        for i, line in enumerate(clean_lines):
            visible_portion = line[:step+1] if step < len(line) else line
            padding = " " * (max_len - len(visible_portion))
            original_line = text_lines[i]
            print(f"│ {text_farbe}{visible_portion}{Fore.WHITE}{padding} │")
            
        print("└" + "─" * breite + "┘")
        time.sleep(0.001)
    clear_terminal()
    print("┌" + "─" * breite + "┐")  #print last time but with collor
    for i, line in enumerate(clean_lines):
            visible_portion = line[:step+1] if step < len(line) else line
            padding = " " * (max_len - len(visible_portion))
            original_line = text_lines[i]
            print(f"│ {text_farbe}{original_line}{Fore.WHITE}{padding} │")
    print("└" + "─" * breite + "┘")
    wait()

def p(text):
    clean_text = remove_ansi_codes(text)
    sichtbare_laenge = len(clean_text) + 2
    for i in range(len(clean_text)):
        clear_terminal()
        print("┌" + "─" * sichtbare_laenge + "┐")
        revealed_portion = clean_text[0:i+1]
        print(f"│ {base_collor}{revealed_portion}{Fore.WHITE} │")
        print("└" + "─" * sichtbare_laenge + "┘")
        time.sleep(0.001)
    clear_terminal()
    print("┌" + "─" * sichtbare_laenge + "┐") #print last time but with collor
    print(f"│ {base_collor}{text}{Fore.WHITE} │")
    print("└" + "─" * sichtbare_laenge + "┘")
    wait()
