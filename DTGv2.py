import random

destinations = ['Texas', 'Georgia', 'Florida']
resturants = ['Steakhouse', 'Tacogong', 'Waffleking']
travel_mode = ['plane', 'car', 'bus']
for_fun = ['riding bikes', 'visit beach', 'the Zoo']

# def user_manual_trip():
#     destinations = ['Texas', 'Georgia', 'Florida']
#     resturants = ['Steakhouse', 'Tacogong', 'Waffleking']
#     travel_mode = ['plane', 'car', 'bus']
#     for_fun = ['riding bikes', 'visit beach', 'the Zoo']
#     print('From the list below, where would you like you go? ')
#     print(destinations)
#     user_man_choice = int(input('Choose from option above. 0. for Texas, 1. for Georgia, and 2. for Forida?' ))
    
#     while user_man_choice == 0 or 1 or 2:
#         if user_man_choice is 0:
#             return('Texas')
#         break

# no
def user_random_trip():

    rand_destination = random.choice(destinations)
    rand_resturants = random.choice(resturants)
    rand_for_fun = random.choice(for_fun)
    rand_travel_mode = random.choice(travel_mode)
    yes_i_like = 'yes'
    no_i_dont = 'no'
    print(f'Your random trip choice is {rand_for_fun}, {rand_resturants} for food, traveling by {rand_travel_mode} in {rand_destination}.')
    user_chose = input('Did you like this choice? YES or NO?' )
    if user_chose == 'no':
        confirmed = False
        while confirmed == False:
            user_choice = int(input('press 1 for a new destination, press 2 for a new resturant, press 3 for a new activity, press 4 for a new mode of transportation or 5 to confirm your options?'))
            if user_choice == 1:
                rand_destination = random.choice(destinations)
                print(f'Your new destination will be {rand_destination}.')
            elif user_choice == 2:
               rand_resturants = random.choice(resturants)
               print(f'Your new resturant will be {rand_resturants}.')
            elif user_choice == 3:
               rand_resturants = random.choice(resturants)
               print(f'Your new activity will be {rand_for_fun}.')
            elif user_choice == 4:
               rand_resturants = random.choice(resturants)
               print(f'Your new travel will be {rand_travel_mode}.')
            elif user_choice == 5:
                print(f'Thank you for confirming your trip! Enjoy your trip! Your random trip choice is {rand_for_fun}, {rand_resturants} for food, traveling by {rand_travel_mode} in {rand_destination}.')
                confirmed = True
    elif user_chose == 'yes':
        print(f'Enjoy your trip! Your random trip choice is {rand_for_fun}, {rand_resturants} for food, traveling by {rand_travel_mode} in {rand_destination}.')
    
user_random_trip()
# input('Would you like to manully select your trip next year?' )
# user_manual_trip()
print('Come back next year!')
# print(user_choose)
#
# (15 points): As a user, I want to be able to randomly re-select a destination, 
# restaurant, mode of transportation, and/or form of entertainment if I don’t 
# like one or more of those things. 
# (10 points): As a user, I want to be able to confirm that my day trip is 
# “complete” once I like all of the random selections. 
# (10 points): As a user, I want to display my completed trip in the console. 
# (5 points): As a developer, I want all of my functions to have a Single 
# Responsibility. Remember, each function should do just one thing!

# dest_input = input('Add custom destination? YES Or NO?' )
#         if dest_input == 'yes':
#             new_loction = input('New Location?')
#             destinations.append(new_loction)
#             user_random_trip()
#         rest_input = input('Add custom destination? YES Or NO?' )
#         if rest_input == 'yes':
#             new_food = input('New Resturant')
#             resturants.append(new_food)
#             user_random_trip()