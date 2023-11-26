import random
import math
class Warrior:
    def __init__(self, warrior, health="0", attackMax="0", blockMax="0"):
        self.warrior = warrior
        self.healthMax = health
        self.attackMax = attackMax
        self.blockMax = blockMax

    def attack(self):
        AttackAmt = self.attackMax * (random.random() + .5)
        return AttackAmt

    def block(self):
        blockhAmt = self.blockMax * (random.random() + .5)
        return blockAmt

class Battle:
    def __init__(self, warrior1, warrior2):

        while True:
            if getAttackResult(warrior1, warrior2) == "Game Over":
                print("Game Over")

        while True:
            if getAttackResult(warrior2, warrior1) == "Game Over":
                print("Game Over")

    @staticmethod
    def getAttackResult(worriorA, worriorB):
        worriorAAttkAmt = worriorA.attack()
        worriorBBlockAmt = worriorB.block()

        damage2worriorB = ceil(worriorAAttkAmt - worriorBBlockAmt)
        worriorB.health = worriorB.health - damage2worriorB
        print("{} attacks {} and deals {} damage".format(worriorA, worriorB, damage2worriorB))
        print("{} is down to {} health".format(worriorB.name, worriorB.health))

        if worriorB.health <= 0:
            print("{} is dead and {} is victorious".format(worriorA.name, worriorB.name))
            return "Game Over"
        else:
            return "Fight Again"

def main():
    DupeFolohun = Warrior(50, 20, 10)
    Taofeek = Warrior(50, 20, 10)

    battlefield = Battle(DupeFolohun, Taofeek)
    battlefield.startFight(DupeFolohun, Taofeek)
main()
if __name__ == "__main__":
    main()
