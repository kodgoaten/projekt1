import random 

print("""                                                                                                                                                                      
   █     █▓█████ ██▓    ▄████▄  ▒█████  ███▄ ▄███▓█████    ▄▄▄█████▓▒█████      ▄████▄  ▄▄▄     ▓█████ ██▓    ██▓█████▄ 
  ▓█░ █ ░█▓█   ▀▓██▒   ▒██▀ ▀█ ▒██▒  ██▓██▒▀█▀ ██▓█   ▀    ▓  ██▒ ▓▒██▒  ██▒   ▒██▀ ▀█ ▒████▄   ▓█   ▀▓██▒   ▓██▒██▀ ██▌
  ▒█░ █ ░█▒███  ▒██░   ▒▓█    ▄▒██░  ██▓██    ▓██▒███      ▒ ▓██░ ▒▒██░  ██▒   ▒▓█    ▄▒██  ▀█▄ ▒███  ▒██░   ▒██░██   █▌
  ░█░ █ ░█▒▓█  ▄▒██░   ▒▓▓▄ ▄██▒██   ██▒██    ▒██▒▓█  ▄    ░ ▓██▓ ░▒██   ██░   ▒▓▓▄ ▄██░██▄▄▄▄██▒▓█  ▄▒██░   ░██░▓█▄   ▌
  ░░██▒██▓░▒████░██████▒ ▓███▀ ░ ████▓▒▒██▒   ░██░▒████▒     ▒██▒ ░░ ████▓▒░   ▒ ▓███▀ ░▓█   ▓██░▒████░██████░██░▒████▓ 
  ░ ▓░▒ ▒ ░░ ▒░ ░ ▒░▓  ░ ░▒ ▒  ░ ▒░▒░▒░░ ▒░   ░  ░░ ▒░ ░     ▒ ░░  ░ ▒░▒░▒░    ░ ░▒ ▒  ░▒▒   ▓▒█░░ ▒░ ░ ▒░▓  ░▓  ▒▒▓  ▒ 
    ▒ ░ ░  ░ ░  ░ ░ ▒  ░ ░  ▒    ░ ▒ ▒░░  ░      ░░ ░  ░       ░     ░ ▒ ▒░      ░  ▒    ▒   ▒▒ ░░ ░  ░ ░ ▒  ░▒ ░░ ▒  ▒ 
    ░   ░    ░    ░ ░  ░       ░ ░ ░ ▒ ░      ░     ░        ░     ░ ░ ░ ▒     ░         ░   ▒     ░    ░ ░   ▒ ░░ ░  ░ 
      ░      ░  ░   ░  ░ ░         ░ ░        ░     ░  ░               ░ ░     ░ ░           ░  ░  ░  ░   ░  ░░    ░    
                       ░ """)

class Spelare:
    def __init__(self):
        self.hp = 100
        self.vapen = None

    def skada(self, antal_skada):
        self.hp -= antal_skada
        print(f"Du har nu {self.hp} hp!")
        if self.hp <= 0:
            print(f"Game Over! Du har dött till {self.monster}")
    
    def ta_upp_vapen(self, Vapen):
        self.vapen = Vapen
        print(f"Du hitta ett {Vapen}")
    
    def heal(self, Heals):
        self.hp += Heals
        print(f"Grattis! Du har nu hittat en heal som ger {Heals} hp och har nu {self.hp} HP")

class Rum:
    def __init__(self):
        self.random = random.randint(1,13)
        if self.random <= 4:
            self.chestvapen = None
            self.chestheals = None
            self.monster = random.choice(["Troll", "Robot", "Kloakråttor", "Zombie Jesper"]) 

        elif self.random <= 8:
            self.monster = None
            self.chestvapen = None
            self.chestheals = random.choice(["Mini shield(25HP)", "Big pot(50HP)", "Chug Jug(100HP)"])
        else:
            self.monster = None
            self.chestheals = None
            self.chestvapen = random.choice(["Zweihander", "Greatsword", "Curved Blade", "Machete"])


def main():
    spelare = Spelare()
    times_died = 0



    while times_died < 1:
        

        print("Välj ett rum")
        print("Rum 1")
        print("Rum 2")
        print("Rum 3")

        Deras_val = input("-->")
        if Deras_val == "1":
            r = Rum()
            print(r.chestheals)
            print(r.chestvapen)
            print(r.monster)
            if r.monster != None:
                val = input(f"Du har träffat på monstret {r.monster}. Vill du försöka springa eller slåss -->")
                if val == "springa":
                    antal_skada = random.randint(10,20)
                    print(f"Du hann springa bor men har tagit {antal_skada} skada")
                    spelare.skada
                    print(f"Du har nu {spelare.hp} hp!")
                elif val == "slåss": 
                    if spelare.vapen != None:
                        antal_skada = random.randint(0,20)
                    elif spelare.vapen == None:
                        print("Du har dött och förlorat spelet")
                        times_died = 1
                
            

            elif r.chestvapen != None:
                pass
            elif r.chestheals != None:
                pass
main()
