import random
print("random number (1-10):",random.randint(1,10))
colors=["red","blue","green","yellow"]
print("random choice from list:",random.choice(colors))
random.shuffle(colors)
print("shuffled list:",colors)