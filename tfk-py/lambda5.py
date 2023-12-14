attack = {"quick": (lambda: print("Quick Attack")),
          "power": (lambda: print("Power Attack")),
          "miss": (lambda: print("Missed Attack"))}

attack["quick"]()

import random

attackkey = random.choice(list(attack.keys()))
attack[attackkey]()
