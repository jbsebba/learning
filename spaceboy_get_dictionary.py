import random
import math

print("I have information for the following planets:\n")

print("   1. Venus   2. Mars    3. Jupiter")
print("   4. Saturn  5. Uranus  6. Neptune\n")

weight = 185
rand_int = random.randint(1,8)

planets = ['Venus', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
gravity = [0.91, 0.38, 2.43, 1.06, 0.92, 1.19]

print ('Dear lord, we have recieved word that there are two more planets we need to consider!!!\nNamely Tellus and Pluto, please add them to the list.\n')

#Adding more planets
outsiders = ['Tellus', 'Pluto']
planets = planets + outsiders
#Adding gravity for new planets
outsider_gravity = [1, 0.5]
gravity = gravity + outsider_gravity

#So what planet will it be?!!!
chosen_planet = random.choice(planets)

#just making a empty dictionary
planets_and_gravity_dictionary = {}
pagd = planets_and_gravity_dictionary
#making our two lists into one dictionary
pagd = dict(zip(planets, gravity))

print('The list is now\n' + str(planets))

#.Getting the chosen planets matching gravity from dictionary
planet_gravity = pagd.get(chosen_planet)
relative_weight = planet_gravity * weight


print('\nThe planet you have arrived on is:\n' + chosen_planet)
print('The planet has a gravity of:\n' + str(planet_gravity))
print(' Compared to earth, your weight is now:\n' + str(math.ceil(relative_weight)) + ' kg')
