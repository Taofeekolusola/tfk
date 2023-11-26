import random
from math import ceil

class Warrior:
    def __init__(self, name, health, attackMax, blockMax):
        self.name = name
        self.health = health
        self.attackMax = attackMax
        self.blockMax = blockMax

    def attack(self):
        attackAmt = self.attackMax * (random.random() + 0.5)
        return attackAmt

    def block(self):
        blockAmt = self.blockMax * (random.random() + 0.5)
        return blockAmt

class Battle:
    def __init__(self, warrior1, warrior2):
        self.warrior1 = warrior1
        self.warrior2 = warrior2

    def startFight(self):
        while True:
            if self.getAttackResult(self.warrior1, self.warrior2) == "Game Over":
                print("Game Over")
                break

            if self.getAttackResult(self.warrior2, self.warrior1) == "Game Over":
                print("Game Over")
                break

    def getAttackResult(self, warriorA, warriorB):
        warriorAAttkAmt = warriorA.attack()
        warriorBBlockAmt = warriorB.block()

        damage2warriorB = ceil(warriorAAttkAmt - warriorBBlockAmt)
        warriorB.health = warriorB.health - damage2warriorB
        print("{} attacks {} and deals {} damage".format(warriorA.name, warriorB.name, damage2warriorB))
        print("{} is down to {} health".format(warriorB.name, warriorB.health))

        if warriorB.health <= 0:
            print("{} is dead and {} is victorious".format(warriorA.name, warriorB.name))
            return "Game Over"
        else:
            return "Fight Again"

def main():
    DupeFolohun = Warrior("DupeFolohun", 50, 20, 10)
    Taofeek = Warrior("Taofeek", 50, 20, 10)

    battlefield = Battle(DupeFolohun, Taofeek)
    battlefield.startFight()

if __name__ == "__main__":
    main()
