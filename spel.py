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
delay = 0.001

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
        print(f"Du hitta ett {vapen}")
    
    def heal(self, heals):
        self.hp += heals
        if self.hp >= 100:
            self.hp = 100

class Rum:
    def __init__(self):
        self.random = random.randint(1,13)
        if self.random <= 6:
            self.chestvapen = None
            self.chestheals = None
            self.monster = random.choice(["Troll", "Robot", "Kloakråttor", "Zombie Jesper"]) 

        elif self.random <= 9:
            self.monster = None
            self.chestvapen = None
            self.chestheals = random.choice(["Mini shield(15HP)", "Big pot(30HP)", "Chug Jug(60HP)"])
        else:
            self.monster = None
            self.chestheals = None
            self.chestvapen = random.choice(["Zweihander", "Greatsword", "Curved Blade", "Machete"])


def main():
    spelare = Spelare()
    monsters_döda = 0
    fix = 0
    
    print("Välj ett rum")

    while spelare.död() == False and monsters_döda <= random.randint(10,15):
        

        
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
                val = input(f"Du har träffat på monstret {r.monster}. Vill du försöka 1. springa bort eller 2. slåss -->")
                if val == "springa bort" or val == "1":
                    antal_skada = random.randint(10,20)
                    spelare.skada(antal_skada)
                    if (spelare.död()):
                            print(f"Du dog av monstret{r.monster} efter att du tog {antal_skada} skada och hade inget hp kvar")
                            print(f"{text_to_print2}")
                    else:
                        print(f"Du hann springa bort men har tagit {antal_skada} skada")
                        print(f"Du har nu {spelare.hp} hp!")
                elif val == "slåss" or val == "2": 
                    if spelare.vapen != None:
                        antal_skada = random.randint(0,30)
                        spelare.skada(antal_skada)
                        if (spelare.död()):
                            print(f"Du dog av monstret{r.monster} efter att du tog {antal_skada} skada och hade inget hp kvar")
                            delayed_print2_green(text_to_print2, delay)
                        elif antal_skada == 0:
                            print(f"Bra jobbat du lyckades besegra {r.monster} utan att ta någon skada")
                        else:
                            print(f"Bra jobbat du lyckades besegra {r.monster}, men du tog {antal_skada} skada")
                            print(f"Du har nu {spelare.hp} hp!")
                        
                            
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

                
            

            elif r.chestvapen != None and r.chestvapen != spelare.vapen:
                if spelare.vapen == None:
                    print(f"Grattis! Du har hittat vapnet {r.chestvapen}")
                    spelare.vapen = r.chestvapen
                elif spelare.vapen != None:
                    vapen_val = input(f"Du har hittat vapnet {r.chestvapen}, vill du byta ut ditt vapen, {spelare.vapen}, för ett nytt vapen? ja eller nej-->")
                    if vapen_val == "ja":
                        spelare.vapen = r.chestvapen
                        print(f"du har nu vapnet {spelare.vapen}")
                    elif vapen_val == "nej":
                        print(f"Du har kvar vapnet {spelare.vapen}")
                    




                
            elif r.chestheals != None and spelare.hp < 100:
                if r.chestheals == "Mini shield(15HP)":
                    antal_heals = 15
                    spelare.heal(antal_heals)
                elif r.chestheals == "Big pot(30HP)":
                    antal_heals = 30
                    spelare.heal(antal_heals)
                else:
                    antal_heals = 60
                    spelare.heal(antal_heals)
                print(f"Grattis! Du har hittat en {r.chestheals} och har nu {spelare.hp} hp")
            
            else: 
                 print("Rummet hade ingenting i sig, men det finns tre till dörrar som du kan välja mellan för att gå in i ett nytt rum, vilket rum väljer du?")
                 fix += 1

        if spelare.död() == False and fix == 0:  
            print("Det finns inget mer i det här rummet, men det finns tre till dörrar som du kan välja mellan för att gå in i ett nytt rum, vilket rum väljer du?")

                

                    
                    

                    
main()


