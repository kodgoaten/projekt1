import random 
import pygame
import time

def delayed_print_green(text, delay=0.1):
    for char in text:
        print('\033[92m' + char + '\033[0m', end='', flush=True)
        time.sleep(delay)

# Set your desired delay (in seconds) between each character
delay = 0.0002

# The text to be printed with delays
text_to_print = """ 

         _____                    _____                    _____                    _____            _____                    _____          
         /\    \                  /\    \                  /\    \                  /\    \          /\    \                  /\    \         
        /::\    \                /::\    \                /::\    \                /::\____\        /::\    \                /::\    \        
       /::::\    \              /::::\    \              /::::\    \              /:::/    /        \:::\    \              /::::\    \       
      /::::::\    \            /::::::\    \            /::::::\    \            /:::/    /          \:::\    \            /::::::\    \      
     /:::/\:::\    \          /:::/\:::\    \          /:::/\:::\    \          /:::/    /            \:::\    \          /:::/\:::\    \     
    /:::/  \:::\    \        /:::/__\:::\    \        /:::/__\:::\    \        /:::/    /              \:::\    \        /:::/  \:::\    \    
   /:::/    \:::\    \      /::::\   \:::\    \      /::::\   \:::\    \      /:::/    /               /::::\    \      /:::/    \:::\    \   
  /:::/    / \:::\    \    /::::::\   \:::\    \    /::::::\   \:::\    \    /:::/    /       ____    /::::::\    \    /:::/    / \:::\    \  
 /:::/    /   \:::\    \  /:::/\:::\   \:::\    \  /:::/\:::\   \:::\    \  /:::/    /       /\   \  /:::/\:::\    \  /:::/    /   \:::\ ___\ 
/:::/____/     \:::\____\/:::/  \:::\   \:::\____\/:::/__\:::\   \:::\____\/:::/____/       /::\   \/:::/  \:::\____\/:::/____/     \:::|    |
\:::\    \      \::/    /\::/    \:::\  /:::/    /\:::\   \:::\   \::/    /\:::\    \       \:::\  /:::/    \::/    /\:::\    \     /:::|____|
 \:::\    \      \/____/  \/____/ \:::\/:::/    /  \:::\   \:::\   \/____/  \:::\    \       \:::\/:::/    / \/____/  \:::\    \   /:::/    / 
  \:::\    \                       \::::::/    /    \:::\   \:::\    \       \:::\    \       \::::::/    /            \:::\    \ /:::/    /  
   \:::\    \                       \::::/    /      \:::\   \:::\____\       \:::\    \       \::::/____/              \:::\    /:::/    /   
    \:::\    \                      /:::/    /        \:::\   \::/    /        \:::\    \       \:::\    \               \:::\  /:::/    /    
     \:::\    \                    /:::/    /          \:::\   \/____/          \:::\    \       \:::\    \               \:::\/:::/    /     
      \:::\    \                  /:::/    /            \:::\    \               \:::\    \       \:::\    \               \::::::/    /      
       \:::\____\                /:::/    /              \:::\____\               \:::\____\       \:::\____\               \::::/    /       
        \::/    /                \::/    /                \::/    /                \::/    /        \::/    /                \::/____/        
         \/____/                  \/____/                  \/____/                  \/____/          \/____/                  ~~       
                                                                        

"""

# Call the delayed_print_green function with the specified text and delay
delayed_print_green(text_to_print, delay)

#Åvanför är koden för själva "Welcome to Caelid" intron

def delayed_print2_green(text, delay=0.1):
    for char in text:
        print('\033[92m' + char + '\033[0m', end='', flush=True)
        time.sleep(delay)

# Set your desired delay (in seconds) between each character
delay = 0.0015

# The text to be printed with delays
text_to_print2 = """
                    
⢰⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼
⠀⢿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⠴⠶⠖⠒⠛⣿⣽⡟⠛⠓⠒⠶⠶⢤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠴⣯⠏
⠀⠀⢿⣯⣿⠷⣶⣤⡴⣶⣶⣤⠤⠤⣤⣄⡀⠀⣀⡤⠶⠛⠉⠀⠀⠀⠀⠀⠀⠴⠿⣼⠿⠦⠀⠀⠀⠀⠀⠀⠉⠛⠲⢦⣄⣀⣤⣴⠒⣻⣿⣿⢻⣿⣿⣿⠋⣩⣴⠋⠀
⠀⠀⠀⠙⠿⣦⣼⣟⢷⣷⢹⣿⣌⣿⡟⢺⣿⠛⠻⣄⠀⠀⠀⠀⢀⣠⣤⠤⠖⠒⠒⠛⠒⠒⠒⠦⠤⣤⣀⠀⠀⢀⣤⠖⠛⢿⣇⠐⡾⣷⣿⡟⢚⣿⣷⣿⠶⠋⠁⠀⠀
⠀⠀⠀⠀⠀⠈⠙⠛⠛⠻⠾⢿⣾⣮⣗⣸⣿⣆⠄⠀⠙⣦⡖⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢉⣷⡟⠀⡀⢨⣽⣿⣽⣶⢿⡿⠛⠛⠉⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠛⠉⠙⠻⢿⣷⣶⡂⣸⡟⠓⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠛⣧⣄⣿⣾⣿⡋⠉⠀⠀⠙⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠟⠁⠀⠀⠀⣠⠾⣿⣿⣿⣿⡁⠀⠈⢳⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠋⠀⠀⣿⣿⣿⣫⣶⠟⢦⡀⠀⠀⣀⠹⣆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⡼⢿⡷⣾⠀⢀⡞⠁⠀⠹⡄⢻⣿⣿⡆⠀⠘⣿⣦⣤⣀⣀⠀⠀⣀⣀⣤⣶⣿⡯⠀⢀⣾⣿⡿⠋⢀⡞⠀⠀⠙⢆⣀⣿⣻⣯⣷⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⡾⠷⠛⢳⡞⣻⠋⠀⠀⠀⠀⢳⡀⢻⣿⣿⣦⣠⣿⡯⣷⡉⣽⠿⠿⠟⠉⣹⡯⣿⣷⣤⣾⣿⣿⠁⠀⣼⠃⠀⠀⠀⠈⠻⡍⠏⠁⠉⢷⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⡾⠁⠀⠀⠈⡱⠁⠀⠀⠀⠀⠀⠈⢷⠈⣿⣿⣿⠟⣿⣇⡝⣮⡈⠀⠀⠀⣴⡟⠀⢿⡟⢿⣻⣿⣇⠀⣰⠇⠀⠀⠀⠀⠀⠀⠙⡄⠀⠀⠀⢿⡀⠀⠀⠀
⠀⠀⠀⠀⠀⣼⠇⠀⠀⠀⡼⠃⠀⠀⠀⣀⣀⣠⣤⣼⠿⣿⢿⠃⣰⠋⠈⠁⢻⡙⢶⣴⠟⣹⠃⠀⠀⠱⡄⢹⣿⣟⠲⢿⠤⠤⣤⣤⣀⡀⠀⠀⠸⡆⠀⠀⠈⣧⠀⠀⠀
⠀⠀⠀⠀⢠⡏⠀⠀⠀⣰⣃⣤⠖⠋⣉⡡⢆⣠⠟⠁⣼⣿⡿⢸⣇⠶⠊⠀⢸⣷⠛⠉⢳⣿⠀⠀⠐⢶⠹⡌⣿⡿⣆⠈⠱⢦⡐⠦⣄⣉⣙⣶⣄⣹⡀⠀⠀⢸⡇⠀⠀
⠀⠀⠀⠀⣾⠀⠀⢰⣶⣿⣿⣿⡿⢿⣥⣶⣟⣁⣠⣞⣽⠟⡇⢸⣿⡀⣀⡴⠋⢹⡄⠀⣸⣉⣻⣦⣄⣸⣰⡇⣿⢹⣮⣷⣤⣤⣿⠿⠞⣛⣿⣿⣿⣿⡿⠂⠀⠀⢿⠀⠀
⠀⠀⠀⠀⡟⠀⠀⠀⢹⠋⠳⢿⣿⣷⡶⠦⢭⣽⣾⣿⡟⠰⢷⣘⣿⠁⠿⠋⠉⠙⣿⠉⡿⠉⠉⠉⠏⢩⣿⢠⣟⣐⣿⣿⢷⣾⣷⣒⣩⣿⠿⠟⠉⠀⢱⠀⠀⠀⢸⠀⠀
⠀⠀⠀⢠⡇⠀⠀⠀⢸⠀⠀⠀⠈⠙⠻⠿⢿⣿⣿⣿⡟⣠⣾⣳⣽⣷⣦⢠⠄⣖⢹⣿⠃⠃⠠⠂⣰⣿⣿⢿⣧⣄⣻⣿⣿⣛⠟⠛⠋⠀⠀⠀⠀⠀⢸⡄⠀⠀⢸⡇⠀
⠀⠀⠀⢸⡇⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⢀⣸⠿⠋⢻⣿⣿⣿⣿⡽⣽⣾⣿⣦⣬⠞⠏⠀⢤⣼⣿⣿⣿⢱⣿⣿⣿⣿⡆⠈⠙⠲⣤⡀⠀⠀⠀⠀⠀⢸⡇⠀⠀⢸⡇⠀
⠀⠀⠀⠀⡇⢰⣄⣤⣾⠀⠀⠀⢀⣠⠶⠋⠁⠀⢀⣾⣿⢿⣿⣾⣇⢹⡏⣻⣿⠞⠀⠀⠀⠰⣿⣏⣸⡇⣾⣿⣿⣿⣿⣿⠀⠀⠀⠀⠙⠳⢦⣀⠀⠀⢸⢳⣦⡞⢸⡇⠀
⠀⠀⠀⠀⣷⡼⣯⡽⢿⣆⣤⣞⣋⣀⣀⣀⣀⣀⣸⣿⣿⣧⠬⠹⣯⣬⣿⠉⠹⣄⠀⠀⠀⣰⠏⠉⣿⢤⣿⠟⠲⣾⣿⣻⣧⣤⣤⣤⡤⠤⠤⠽⠿⢦⡼⠛⣷⠛⢿⠀⠀
⠀⠀⠀⠀⢻⡄⠘⠃⠀⢿⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣷⣄⠀⢻⣿⠏⢦⠀⠈⠐⠀⠸⡁⠀⡟⠙⣿⠟⠀⣠⣾⣿⣾⠃⠀⠀⠀⠀⠀⠀⠀⠀⢠⡇⠀⠙⢀⡿⠀⠀
⠀⠀⠀⠀⠘⣇⠀⠀⠀⠈⡇⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣷⣄⠿⣄⠈⢿⡆⠀⠀⠀⢴⡿⠀⣠⠟⣠⣾⣿⢿⡽⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⡞⠀⠀⠀⣸⠇⠀⠀
⠀⠀⠀⠀⠀⢹⡆⠀⠀⠀⠘⣆⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⢿⣶⡈⢦⢸⡇⠀⢠⠀⢸⡇⠐⢁⣼⣿⢿⣯⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⠁⠀⠀⢠⡏⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢻⡄⠀⠀⠀⠘⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢶⣿⣿⣳⠀⠀⡇⠀⣼⠀⢸⡇⠀⣜⣿⣹⠶⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡼⠁⠀⠀⢀⡿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢻⡄⠀⠀⠀⠈⢣⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⣯⡃⢸⡇⠀⢹⠂⠈⡇⠀⣿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠞⠀⠀⠀⢠⡞⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠹⣆⠀⠀⠀⠀⠙⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣽⠷⣼⠃⠀⠀⠀⠀⢷⡰⢹⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠔⠁⠀⠀⠀⣠⠟⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢷⣄⠀⠀⠀⠀⠙⢦⣀⠀⠀⠀⠀⠀⠀⠀⢿⣴⣿⣦⣀⣠⣀⣤⣿⣧⢾⠆⠀⠀⠀⠀⠀⠀⠀⣠⠶⠃⠀⠀⠀⢀⡼⠋⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢦⡀⠀⠀⠀⣆⣉⣷⢦⣀⠀⠀⠀⠀⢸⡜⠿⣷⣿⣿⠿⣽⡿⠛⡞⠀⠀⠀⠀⢀⣠⣴⢊⣁⠀⠀⠀⢀⣴⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠦⣄⣠⢿⣩⡷⡄⠈⠙⠓⠤⢤⣀⣙⣦⣈⣻⣦⣾⣁⣠⣞⣁⣀⠤⠴⠚⠋⣀⣿⣻⣧⡀⣀⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠦⣟⡀⠀⠀⠀⠀⠀⠀⠀⠉⠉⢿⡿⠷⣿⢿⡯⠉⠉⠀⠀⠀⠀⠀⠉⠉⣿⡾⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠓⠶⣄⣀⡀⠀⠀⠀⠀⠀⠙⣶⡿⢸⠇⠀⠀⠀⠀⣀⣠⠴⠞⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠛⠒⠒⠲⢾⣟⡥⠿⠒⠒⠛⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠇⠀
             _____                 ____              
             / ___/__ ___ _  ___   / __ \_  _____ ____
            / (_ / _ `/  ' \/ -_) / /_/ / |/ / -_) __/
            \___/\_,_/_/_/_/\__/  \____/|___/\__/_/  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

"""

# Call the delayed_print_green function with the specified text and delay



class Spelare:
    def __init__(self):
        self.hp = 100
        self.vapen = None
        

    def skada(self, antal_skada):
        self.hp -= antal_skada
        
    def död(self):
        if self.hp <= 0:
            return True
        else:
            return False
    
    def ta_upp_vapen(self, vapen):
        self.vapen = vapen
    
    def heal(self, heals):
        self.hp += heals
        if self.hp >= 100:
            self.hp = 100

    def vapen_information(self, vapen):
        self.vapen = vapen
        if self.vapen == "Zweihander":
            print("Zweihander ökar chansen att döda monster utan att ta någon skada")
        elif self.vapen == "Greatsword":
            print("Greatsword ger dig +3 HP efter varje rum du besöker")
        elif self.vapen == "Machete":
            print("Machete gör dig snabbare och därför tar mindre skada när du springer bort från monster")
        elif self.vapen == "Curved Blade":
            print("Curved Blade är bra på att döda draken")

class Rum:
    def __init__(self):
        self.random = random.randint(1,10)
        if self.random <= 5:
            self.chestvapen = None
            self.chestheals = None
            self.monster = random.choice(["Troll", "Robot", "Kloakråttor", "Zombie Jesper"]) 

        elif self.random <= 8:
            self.monster = None
            self.chestvapen = None
            self.chestheals = random.choice(["Mini shield(15HP)", "Big pot(25HP)", "Chug Jug(35HP)"])
        else:
            self.monster = None
            self.chestheals = None
            self.chestvapen = random.choice(["Zweihander", "Greatsword", "Curved Blade", "Machete"])
        
    def vapen_information2(self, chestvapen):
        if chestvapen == "Zweihander":
            print("Zweihander ökar chansen att döda monster utan att ta någon skada")
        elif chestvapen == "Greatsword":
            print("Greatsword ger dig +3 HP efter varje rum du besöker")
        elif chestvapen == "Machete":
            print("Machete gör dig snabbare och därför tar mindre skada när du springer bort från monster")
        elif chestvapen == "Curved Blade":
            print("Curved Blade är bra på att döda draken")
    
class Drake:
    def __init__(self):
        self.drakhp = 200
    
    def drak_skada(self, drak_skadad):
        self.drakhp -= drak_skadad
    
    def drake_död(self):
        if self.drakhp <= 0:
            return True
        else:
            return False
    
    

def main():
    spelare = Spelare()
    drake = Drake()
    monster_döda = 0
    fix = 0
    

    print("Välkommen till spelet Caelid!")
    print("Du ska gå genom olika rum, rummen kan innehålla monster, vapen eller heals")
    print("Efter att ha dödat många monster spawnar en drake. Döda Draken för att vinna")
    print("Välj ett rum eller kolla dina stats")
    

    while spelare.död() == False and monster_döda <= 1:
        

        print("0. Stats")
        print("1. Rum 1")
        print("2. Rum 2")
        print("3. Rum 3")

        Deras_val = input("-->")
        if Deras_val == "1" or Deras_val == "2" or Deras_val == "3":
            r = Rum()
            (r.chestheals)
            (r.chestvapen)
            (r.monster)
            if r.monster != None:
                val = input(f"Du har träffat på monstret {r.monster}. Vill du försöka 1.springa bort eller 2.slåss -->")
                if val == "springa bort" or val == "1":
                    if spelare.vapen == "Machete":
                        antal_skada = random.randint(1,8)
                    else:
                        antal_skada = random.randint(10,20)
                    spelare.skada(antal_skada)
                    if (spelare.död()):
                            print(f"Du dog av monstret{r.monster} efter att du tog {antal_skada} skada och hade inget hp kvar")
                            print(f"{text_to_print2}")
                    else:
                        print(f"Du hann springa bort men har tagit {antal_skada} skada")
                        print(f"Du har nu {spelare.hp} hp!")

                elif val == "slåss" or val == "2": 
                    
                    if spelare.vapen != None and spelare.vapen != "Zweihander":
                        antal_skada = random.randint(0,40)
                        spelare.skada(antal_skada)
                        if (spelare.död()):
                            print(f"Du dog av monstret{r.monster} efter att du tog {antal_skada} skada och hade inget hp kvar")
                            delayed_print2_green(text_to_print2, delay)
                        elif antal_skada == 0:
                            print(f"Bra jobbat du lyckades besegra {r.monster} utan att ta någon skada")
                            monster_döda += 1
                        else:
                            print(f"Bra jobbat du lyckades besegra {r.monster}, men du tog {antal_skada} skada")
                            print(f"Du har nu {spelare.hp} hp!")
                            monster_döda += 1
                          
                    elif spelare.vapen == None:
                        print(f"Du dog till {r.monster} eftersom att du inte hade något vapen")
                        antal_skada = 100
                        spelare.skada(antal_skada)
                        if (spelare.död()):
                            pygame.init()
                            mp3_file = "nightmare-jumpscare.mp3"
                            pygame.mixer.music.load(mp3_file)
                            pygame.mixer.music.set_volume(1.0)
                            pygame.mixer.music.play()
                            delayed_print2_green(text_to_print2, delay)
                            time.sleep(5)
                            pygame.mixer.quit()

                    elif spelare.vapen == "Zweihander":
                        Zweihander_1shot = random.randint(1,4)
                        if Zweihander_1shot == 1:
                            spelare.skada(0)
                            print(f"Bra jobbat du lyckades besegra {r.monster} utan att ta någon skada, eftersom du har vapnet {spelare.vapen}")
                            monster_döda += 1
                        else: 
                            antal_skada = random.randint(1,40)
                            spelare.skada(antal_skada)
                            if (spelare.död()):
                                print(f"Du dog av monstret{r.monster} efter att du tog {antal_skada} skada och hade inget hp kvar")
                                delayed_print2_green(text_to_print2, delay)
                            else:
                                print(f"Bra jobbat du lyckades besegra {r.monster}, men du tog {antal_skada} skada")
                                print(f"Du har nu {spelare.hp} hp!")
                                monster_döda += 1


                
            

            elif r.chestvapen != None and r.chestvapen != spelare.vapen:
                if spelare.vapen == None:
                    print(f"Grattis! Du har hittat vapnet {r.chestvapen}")
                    spelare.vapen = r.chestvapen
                elif spelare.vapen != None:
                    vapen_val = input(f"Du har hittat vapnet {r.chestvapen}, vill du byta ut ditt vapen, {spelare.vapen}, för ett nytt vapen? 1.ja, 2.nej, eller 3. information om vapnena -->")
                    while vapen_val == "3" and vapen_val != 1 or vapen_val != 2:
                        if vapen_val == "ja" or vapen_val == "1":
                            spelare.vapen = r.chestvapen
                            print(f"Du har nu vapnet {spelare.vapen}")
                            break
                        elif vapen_val == "nej" or vapen_val == "2":
                            print(f"Du har kvar vapnet {spelare.vapen}")
                            break
                        elif vapen_val == "information" or vapen_val == "3":
                            print("Ditt vapen:")
                            spelare.vapen_information(spelare.vapen)
                            print("Vapnet du hitta:")
                            r.vapen_information2(r.chestvapen)
                            print("")
                            vapen_val = input(f"Vill du nu byta ut ditt vapen {spelare.vapen} för det vapnet du hitta {r.chestvapen}? 1.ja, 2.nej, eller 3. information om vapnena -->")
                        




                
            elif r.chestheals != None and spelare.hp < 100:
                if r.chestheals == "Mini shield(15HP)":
                    antal_heals = 15
                    spelare.heal(antal_heals)
                elif r.chestheals == "Big pot(30HP)":
                    antal_heals = 25
                    spelare.heal(antal_heals)
                else:
                    antal_heals = 35
                    spelare.heal(antal_heals)
                print(f"Grattis! Du har hittat en {r.chestheals} och har nu {spelare.hp} hp")
            
            else: 
                 print("Rummet hade ingenting i sig, men det finns tre till dörrar som du kan välja mellan för att gå in i ett nytt rum, vilket rum väljer du?")
                 fix += 1

        elif Deras_val == "0":
            print("")
            print("Stats:")
            print(f"HP: {spelare.hp}")
            print(f"Vapen: {spelare.vapen}")
            print(f"Monster du har dödat: {monster_döda}")
            print("")
            print("Välj ett rum eller kolla dina stats igen")




        if spelare.vapen == "Greatsword" and spelare.hp != 100 and spelare.hp >= 1 and Deras_val != "0":
            antal_heals = 3
            spelare.heal(antal_heals)
            print("Greatsword har gett dig +3 hp")
            print(f"Du har nu {spelare.hp} hp!")






        if spelare.död() == False and fix == 0 and Deras_val != "0" and monster_döda <= 1:  
            print("Det finns inget mer i det här rummet, men det finns tre till dörrar som du kan välja mellan för att gå in i ett nytt rum, vilket rum väljer du?")

                

                    
    
    
    if spelare.död() == False:
        print("DRAKEN HAR SPAWNAT")
        
        while spelare.död() == False and drake.drake_död() == False:
            drak_attack1 = input("Draken går för attack. Du kan välja att 1. försöka undvika hans attack eller 2. försöka attackera draken istället-->")
            if drak_attack1 == "1" and spelare.vapen != "Machete":
                snabb = random.randint(0,1)
                if snabb == 0:
                    antal_skada = 0
                    spelare.skada(antal_skada)
                else:
                    antal_skada = 50
                    spelare.skada(antal_skada)
                
                
                if antal_skada == 0:
                    print(f"Du lyckades undvika drakens attack")
                    drak_skadad = 50
                    drake.drak_skada(drak_skadad)
                    if (drake.drake_död()):
                        print(f"Du attackerade draken tillbaka efter och gjorde {drak_skadad} så att draken fick 0 HP och dog")
                        print("Grattis du har vunnit spelet")
                    else:
                        print(f"Du attackerade draken tillbaka efter och gjorde {drak_skadad} så att draken har nu {drake.drakhp} hp")

                elif antal_skada == 50 and spelare.död() == False:
                    print(f"Du lyckades inte undvika attacken och tog då {antal_skada} och har nu {spelare.hp}")
                elif (spelare.död()):
                    print(f"Du dog av Draken efter att du tog {antal_skada} skada och hade inget hp kvar")
                    delayed_print2_green(text_to_print2, delay)
                

            elif drak_attack1 == "1" and spelare.vapen == "Machete":
                snabb = random.randint(0,2)
                if snabb <= 1:
                    antal_skada = 0
                    spelare.skada(antal_skada)
                else:
                    antal_skada = 50
                    spelare.skada(antal_skada)
                
                if antal_skada == 0:
                    print(f"Du lyckades undvika drakens attack")
                    drak_skadad = 50
                    drake.drak_skada(drak_skadad)
                    if (drake.drake_död()):
                        print(f"Du attackerade draken tillbaka efter och gjorde {drak_skadad} skada så att draken fick 0 HP och dog")
                        print("Grattis du har vunnit spelet")
                    else:
                        print(f"Du attackerade draken tillbaka efter och gjorde {drak_skadad} skada så att draken har nu {drake.drakhp} hp")
            elif drak_attack1 == "2" and spelare.vapen != "Curved Blade":
                antal_skada = random.randint(1,50)
                spelare.skada(antal_skada)
                drak_skadad = random.randint(1,50)
                drake.drak_skada(drak_skadad)
                if (spelare.död()):
                    print(f"Du dog av Draken efter att du tog {antal_skada} skada och hade inget hp kvar")
                    delayed_print2_green(text_to_print2, delay)
                elif (drake.drake_död()):
                    print("Grattis du har vunnit spelet")
                else:
                    print(f"Du tog {antal_skada} och har nu {spelare.hp} hp")
                    print(f"Draken tog {drak_skadad} och har nu {drake.drakhp} hp")
            elif drak_attack1 == "2" and spelare.vapen == "Curved Blade":
                antal_skada = random.randint(1,50)
                spelare.skada(antal_skada)
                drak_skadad = random.randint(50,100)
                drake.drak_skada(drak_skadad)
                if (spelare.död()):
                    print(f"Du dog av Draken efter att du tog {antal_skada} skada och hade inget hp kvar")
                    delayed_print2_green(text_to_print2, delay)
                elif (drake.drake_död()):
                    print(f"Draken tog {drak_skadad} och har därför inget hp kvar")
                    print("Grattis du har vunnit spelet")  
                else:
                    print(f"Du tog {antal_skada} och har nu {spelare.hp} hp")
                    print(f"Draken tog {drak_skadad} och har nu {drake.drakhp} hp")
            

                

                    
             
                    
main()


