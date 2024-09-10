# Heads or Tail

# Create a coin flipping program using all I know about randomisation in Python.
# It should randomly print "Heads" or "Tails" everytime it runs.

import random

heads = 0
tails = 1

coin = random.randint(0,1)

if coin == heads :
    print("Heads")
else:
    print("Tails")

# Different solution less lines

random_heads_tails = random.randint(0,1)

if random_heads_tails == 0:
    print("Heads")
else:
    print("Tails")