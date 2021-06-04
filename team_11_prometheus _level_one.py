# Project Prometheus: Level One
# Team Eleven Cape Town

# We imported the random module 
import random

# We stored the island map in this one dimensional array
island_map = ["top-left","top-center","top-right","centre-left","middle-centre","centre-right","bottom-left","bottom-centre", "bottom-right"]

# We instantiated the hero's position on the map to the "middle-centre" value in the island map 
# Gave the "wolf" and "fire" variables thier random values from the island map 
hero = island_map[4]
wolf = random.choice(island_map)
fire = random.choice(island_map)

# Gave the "hero xp" variables its value and printed it as a string
hero_xp = 50
print("Hero XP: "+ str(hero_xp))

# We made a While Loop that will only run if the "hero", "wolf" and "fire" variables are not equal to one another or do not have the same values 
# We also made a conditional statement that it will only print 
# if the "hero", "wolf" and "fire" variables are not equal to one another and added a break statement to break the While Loop
while wolf != fire != hero:
    if(wolf != fire != hero):
        print("Hero Location: "+ hero,  "\nWolf Location: "+ wolf, "\nFire Location: "+ fire)
        break
  


