from threading import *
from time import sleep

class Taofeek(Thread):
    def name(self):
        for i in range(5):
            print("Taofeek")
            sleep(1)

class Olusola(Thread):
        def name(self):
            for i in range(5):
                print("Olusola")
                sleep(1)

t = Taofeek()
o = Olusola()

t.name()
sleep(0.2)
o.name()
t.join()
o.join()

print("bye")
