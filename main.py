# Day Trip Generator

destinations = ["Rome", "Venice", "Florence", "Amalfi Coast"]
restaurants = ["Chic-fil-a", "Portillos", "Panda Express", "Chipotle"]
transportations = ["Ripstick", "Longboard", "Tank", "Chopper"]
entertainments = ["Movie", "Shopping", "Soccer Game", "Casino"]

import random

def get_random_item(items):
        return random.choice(items)

def dest_calc():
        result_of_random = random.choice(destinations)
        return result_of_random

def rest_calc():
        restaurant = random.choice(restaurants)
        return restaurant

def transp_calc():
        transportation = random.choice(transportations)
        return transportation

def entertainment_calc():
        entertainment = random.choice(entertainments)
        return entertainment

def unsatisfied_res():
        unsatisfied = input("What would you like to change? ")
        return(unsatisfied)

def satisfaction_res_change(destination, restaurant, transportation, entertainment):
        unsatisfied = unsatisfied_res()
        if unsatisfied == "destination" or unsatisfied == "Destination":
                destinations.remove(destination)
                destination = get_random_item(destinations)
                print(f'New Destination: {destination}')
                satisfaction_check(destination, restaurant, transportation, entertainment)
        elif unsatisfied == "restaurant" or unsatisfied == "Restaurant":
                restaurants.remove(restaurant)
                restaurant = get_random_item(restaurants)
                print(f'New Restaurant: {restaurant}')
                satisfaction_check(destination, restaurant, transportation, entertainment)
        elif unsatisfied == "transportation" or unsatisfied == "Transportation":
                transportations.remove(transportation)
                transportation = get_random_item(transportations)
                print(f'New Transportation: {transportation}')
                satisfaction_check(destination, restaurant, transportation, entertainment)
        elif unsatisfied == "entertainment" or unsatisfied =="Entertainment":
                entertainments.remove(entertainment)
                entertainment = get_random_item(entertainments)
                print(f'New Entertainment: {entertainment}')
                satisfaction_check(destination, restaurant, transportation, entertainment)
        else:
                print("Please check your spelling.")

def satisfaction_check(destination, restaurant, transportation, entertainment):
        satisfaction = input("Are you satisfied with your trip? Y or N ")
        
        if satisfaction == "Y" or satisfaction == "y":
                print(f'Here is your final trip!')
                print(f'Destination: {destination}')
                print(f'Restaurant: {restaurant}')
                print(f'Transportation: {transportation}')
                print(f'Entertainment: {entertainment}')
        else:
                satisfaction_res_change(destination, restaurant, transportation, entertainment)

def run_day_trip():
        destination = get_random_item(destinations)
        restaurant = get_random_item(restaurants)
        transportation = get_random_item(transportations)
        entertainment = get_random_item(entertainments)

        print(f'Destination: {destination}')
        print(f'Restaurant: {restaurant}')
        print(f'Transportation: {transportation}')
        print(f'Entertainment: {entertainment}')

        satisfaction_check(destination, restaurant, transportation, entertainment)

run_day_trip()




















                          











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