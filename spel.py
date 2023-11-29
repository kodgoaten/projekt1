import random 

class Spelare:
    def __init__(self):
        self.hp = 100
        self.vapen = None

    def Skada(self, Antal_skada):
        self.hp -= Antal_skada
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
        self.random = random.randint(1,11)
        if self.random <= 5:
            self.chest = None
            self.monster = random.choice(["Troll", "Robot", "Kloakråttor", "Zombie Jesper"]) 

        else:
            self.monster = None
            self.chest = random.choice(["Mini shield(25HP)", "Big pot(50HP)", "Chug Jug(100HP)", "Zweihander", "Greatsword", "Scavenger's Curved Sword"])

def main():
        spelare = Spelare()
        times_died = 0



        while times_died < 1:
            
            current_room = Rum()

            print("Välj ett rum")
            print("Rum 1")
            print("Rum 2")
            print("Rum 3")

            Deras_val = input("")
            if Deras_val == "1":
                r = Rum()
                print(r.chest)
                print(r.monster)








        
        
            # Kod för rum, kistor, fights
main()
    




    
    
    







#______________________________________________________________________________________________________________
 #Här under är chat gpt generad kod som vi kanske skulle kunna kolla igenom för att LÄRA oss av
#import random

#class Player:
    #def __init__(self, name):
        #self.name = name
        #self.health = 100
        #self.stamina = 100
        #self.weapon_damage = 20  # Du kan ändra detta värde beroende på vapnets styrka

    #def take_damage(self, damage):
        #self.health -= damage
        #if self.health <= 0:
            #print(f"Game Over! {self.name}, du har förlorat all hälsa.")

    #def print_status(self):
        #print(f"{self.name}'s Status:")
        #print(f"Health: {self.health}")
        #print(f"Stamina: {self.stamina}")

    #def choose_door(self, level):
        #things_behind_doors = {
            #1: [Monster(), Weapon(), Money()],
            #2: [Monster(), Weapon(), Money()],
            #3: [Monster(), Weapon(), Money()]

        #print(f"\nNivå {level}: Välj en dörr (1, 2 eller 3):")
        #door_choice = int(input())
        
        #if 1 <= door_choice <= 3:
            #thing_found = random.choice(things_behind_doors[level])
            #print(f"Bakom dörr {door_choice} hittade du: {thing_found}")
            #if isinstance(thing_found, Monster):
                #self.take_damage(thing_found.damage)
            #elif isinstance(thing_found, Weapon):
                #self.weapon_damage += thing_found.damage_bonus
            #elif isinstance(thing_found, Money):
                #print(f"Du hittade {thing_found.amount} guld!")

        #else:
            #print("Ogiltigt val. Välj en dörr mellan 1, 2 eller 3.")

#class Monster:
    #def __init__(self):
        #self.name = "Monster"
        #self.damage = random.randint(10, 20)
        #self.health = random.randint(50, 100)

    #def __str__(self):
        #return f"{self.name} med {self.health} liv och {self.damage} skada"

#class Weapon:
    #def __init__(self):
#       self.damage_bonus = random.randint(5, 10)
#
 #   def __str__(self):
  #      return f"{self.name} med {self.damage_bonus} bonus skada"
#
#class Money:
 #   def __init__(self):
  #      self.name = "Pengar"
   #     self.amount = random.randint(1, 100)
#
 #   def __str__(self):
  #      return f"{self.name}: {self.amount} guld"
#
## Början av spelet
#player_name = input("Vad är ditt namn? ")
#player = Player(player_name)

# Visa spelarens status i början av spelet
#player.print_status()

# Spela nivå 1
#player.choose_door(1)

# Fortsätt med resten av spelet och implementera logiken för andra nivåer om det behövs.