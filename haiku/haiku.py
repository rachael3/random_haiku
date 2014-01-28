import random

haiku1 = random.choice(
    open("haiku1.txt").readlines()
)
haiku2 = random.choice(
    open("haiku2.txt").readlines()
)
haiku3 = random.choice(
    open("haiku3.txt").readlines()
)

print haiku1, haiku2, haiku3
