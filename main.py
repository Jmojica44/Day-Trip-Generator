# Day Trip Generator

destinations = ["Rome", "Venice", "Florence", "Amalfi Coast"]
restaurants = ["Chic-fil-a", "Portillos", "Panda Express", "Chipotle"]
transportations = ["Ripstick", "Longboard", "Tank", "Chopper"]
entertainments = ["Movie", "Shopping", "Soccer Game", "Casino"]

import random

# function for random destination

def dest_calc(destination):
        destination = random.choice(destinations)
        return destination

destination = dest_calc(destinations)
print(f'Destination: {destination}')

if_no_like_dest = destinations.index(destination)

def rest_calc(restaurant):
        restaurant = random.choice(restaurants)
        return restaurant

restaurant = rest_calc(restaurants)
print(f'Restaurant: {restaurant}')

if_no_like_rest = restaurants.index(restaurant)

def transp_calc(transportation):
        transportation = random.choice(transportation)
        return transportation
transportation = transp_calc(transportations)

print(f'Transportation: {transportation}')

def entertainment_calc(entertainment):
        entertainment = random.choice(entertainments)
        return entertainment
entertainment = entertainment_calc(entertainments)

print(f'Entertainment: {entertainment}')

satisfaction = input("Are you satisfied with your trip? Y or N ")

if satisfaction == "Y":
        print(f'Here is your final trip!')
        print(f'Destination: {destination}')
        print(f'Restaurant: {restaurant}')
        print(f'Transportation: {transportation}')
        print(f'Entertainment: {entertainment}')

        








# destination_position = destinations[i]

# print(f" Destination: {destination} Position: {i}")

# restaurant = random.choice(restaurants)
# j = randrange(len(restaurants))
# restaurant_position = restaurants[j]

# print(f' Restaurant: {restaurant} Position: {j}')

# transportation = random.choice(transportations)
# k = randrange(len(transportations))
# transportation_position = transportations[k]

# print(f' Transportation: {transportation} Position: {k}')

# entertainment = random.choice(entertainments)
# l = randrange()



      
      

# function for random restaurant

# function for random transportation

# function for random entertainment



