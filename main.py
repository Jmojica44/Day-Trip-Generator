# Day Trip Generator

destinations = ["Rome", "Venice", "Florence", "Amalfi Coast"]
restaurants = ["Chic-fil-a", "Portillos", "Panda Express", "Chipotle"]
transportations = ["Ripstick", "Longboard", "Tank", "Chopper"]
entertainments = ["Movie", "Shopping", "Soccer Game", "Casino"]

import random

def dest_calc(destination):
        destination = random.choice(destinations)
        return destination

destination = dest_calc(destinations)
print(f'Destination: {destination}')

def rest_calc(restaurant):
        restaurant = random.choice(restaurants)
        return restaurant

restaurant = rest_calc(restaurants)
print(f'Restaurant: {restaurant}')

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

def unsatisfied_res():
        unsatisfied = input("What would you like to change? ")
        return(unsatisfied)

def satisfaction_res_change():
        unsatisfied = unsatisfied_res()
        if unsatisfied == "destination" or unsatisfied == "Destination":
                destinations.remove(destination)
                dest_calc(destination)
                print(f'New Destination: {destination}')
                satisfaction_check()
                unsatisfied_res()
        elif unsatisfied == "restaurant" or unsatisfied == "Restaurant":
                restaurants.remove(restaurant)
                rest_calc(restaurant)
                print(f'New Restaurant: {restaurant}')
        elif unsatisfied == "transportation" or unsatisfied == "Transportation":
                transportations.remove(transportation)
                transp_calc(transportation)
                print(f'New Transportation: {transportation}')
        elif unsatisfied == "entertainment" or unsatisfied =="Entertainment":
                entertainments.remove(entertainment)
                entertainment_calc(entertainment)
                print(f'New Entertainment: {entertainment}')
        else:
                print("Please check your spelling.")

def satisfaction_check():
        satisfaction = input("Are you satisfied with your trip? Y or N ")
        if satisfaction == "Y" or satisfaction == "y":
                print(f'Here is your final trip!')
                print(f'Destination: {destination}')
                print(f'Restaurant: {restaurant}')
                print(f'Transportation: {transportation}')
                print(f'Entertainment: {entertainment}')
        else:
                satisfaction_res_change()

satisfaction_check()


















                          











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