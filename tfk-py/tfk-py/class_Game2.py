import random

class Fighter:
    def __init__(self, name, max_life=100):
        self.name = name
        self.max_life = max_life
        self.current_life = max_life
        self.sword_damage = 10
        self.shield_block = 5

    def attack(self, opponent):
        damage = random.randint(1, self.sword_damage)
        blocked_damage = min(damage, opponent.shield_block)
        actual_damage = damage - blocked_damage

        opponent.current_life -= actual_damage
        print(f"{self.name} attacks {opponent.name} with {actual_damage} damage.")

    def is_alive(self):
        return self.current_life > 0

class Battle:
    def __init__(self, fighter1, fighter2):
        self.fighter1 = fighter1
        self.fighter2 = fighter2

    def start_battle(self):
        print(f"The battle begins between {self.fighter1.name} and {self.fighter2.name}!")

        while self.fighter1.is_alive() and self.fighter2.is_alive():
            self.fighter1.attack(self.fighter2)
            self.fighter2.attack(self.fighter1)

        if self.fighter1.is_alive():
            print(f"{self.fighter1.name} is victorious!")
        else:
            print(f"{self.fighter2.name} is victorious!")

def main():
    fighter1 = Fighter(input("Enter The first fighter's name: "))
    fighter2 = Fighter(input("Enter the second fighter's name: "))

    battle = Battle(fighter1, fighter2)
    battle.start_battle()

if __name__ == "__main__":
    main()
