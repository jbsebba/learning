import random
import math
import time

planets = ['Venus', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
gravity = [0.91, 0.38, 2.43, 1.06, 0.92, 1.19]
planet_gravity = 1
chosen_planet = 1

print('Welcome to the interplanetary space program\n')
time.sleep(2)

answer = input('Are you ready to begin?\n please answer with: (yes) or (no)\n')

if answer != 'no':
    print('\nALRIGHT, awesome! Before we begin we need some information')

    name = input('First, what is your name?\n')
    weight = input('Secondly, how much do you weigh?\n')
    
    print('Thank you!\n')
    
    time.sleep(2)
    
    print("There are currently 6 available planets in our solar system:\n")
    
    time.sleep(2)
    
    for items in planets:
        print(items)
        time.sleep(0.5)
    
    chosen_planet = int(input('\nWhich planet would you like to travel to?\nANSWER 1, 2, 3, 4, 5 or 6... \n'))
    chosen_planet -= 1
    print('Great, you are going to: ' + str(planets[chosen_planet]))
    
    time.sleep(3)
    
    print('\nHoly shit! Wait a minute!\n')
    time.sleep(3)
    print('Our scientists just discovered a new planet')
    time.sleep(3)
    print('If you go there you can be the one to name it')
    time.sleep(2)
    print('Do you wish to go?\n')
    time.sleep(1)
    answer = input('yes or no\n')
    
    if answer != str('no'):
        new_planet = input('What will be the name of the new planet?\n')
        print('Great, you are going to\n' + new_planet)
        chosen_planet = new_planet
        time.sleep(1)
        
        #Adding more planets to lists
        new_gravity = random.uniform(0,2)
        new_gravity_list_item = new_gravity
        planets = planets + [new_planet]
        gravity = gravity + [new_gravity_list_item]

        planet_gravity = new_gravity
        relative_weight = planet_gravity * int(weight)
        
        print('Launching in\n')
        
        time.sleep(1)
        
        loop = 3
        while loop > 0:
            print (str(loop) + '\n')
            loop -= 1
            time.sleep(1)

        print('\nThe planet you have arrived on is:\n' + chosen_planet)
        time.sleep(2)
        print('The planet has a gravity of:\n' + str(new_gravity))
        time.sleep(2)
        print('You used to weigh ' + weight + ' kg')
        print('Compared to earth, your weight is now:\n' + str(math.ceil(relative_weight)) + ' kg')
        
    else:
        
        print('Alright, you are going to ' + str(planets[chosen_planet]) + ' then!')
        time.sleep(2)
        print('Launching in\n')
        
        time.sleep(1)
        
        loop = 3
        while loop > 0:
            print (str(loop) + '\n')
            loop -= 1
            time.sleep(1)

        #.Getting the chosen planets matching gravity from dictionary
        planet_gravity = gravity[chosen_planet]
        relative_weight = planet_gravity * int(weight)


        print('\nThe planet you have arrived on is:\n' + str(planets[chosen_planet]))
        time.sleep(2)
        print('The planet has a gravity of:\n' + str(gravity[chosen_planet]))
        time.sleep(2)
        print('You used to weigh ' + str(weight) + ' kg')
        print('Compared to earth, your weight is now:\n' + str(math.ceil(relative_weight)) + ' kg')
        
else: print ('too bad, cya')