# Roulette with random Names

import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# Option Number 1
print(random.choice(friends))

# Option Number 2
random_index = random.randint(0,4)
print(friends[random_index])