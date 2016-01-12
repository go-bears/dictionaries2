# your code goes here
import sys
import random

def welcome():
    """takes in and returns user name"""
    user = raw_input("Hi! What's your name? ")
    return user

def convert_text_to_dict(filename):
    """converting scores.txt into restaurant_rating dictionary """

    #create empty dictionary
    restaurant_rating = {}

    #open file and loop through data to clean and split data
    for scores_data in open(filename):
        scores_data = scores_data.rstrip().split(":")
        restaurant, rating = scores_data
        
        #checks dictionary for entry, adds restaurant and rating if not already in
        #dictionary

        if restaurant not in restaurant_rating:
            restaurant_rating[restaurant] = int(rating)
           
    return restaurant_rating

def user_updates_rating(restaurant_rating):
    """takes in restaurant_rating dictionary and asks user to update current restaurants"""

    user_updates_ratings = restaurant_rating
    restaurant_list = restaurant_rating.keys()
    user_update = None

    print "Welcome %s! Help us keep our restaurant ratings up-to-date! " % user
    
    #updates current restaurants until user quits   
    while user_update != "q" or user_update != 'Q' or user_update != 'quit':
        random_restaurant = random.choice(restaurant_list)
        print "%s is currently rated %d" % (random_restaurant, int(restaurant_rating[random_restaurant]))
        user_update = raw_input("how would you rate %s between 1-5, with 5 being best: " % random_restaurant)    

        if user_update == 'q': break

        try:
            int(user_update) >0  and int(user_update) < 5            
            user_updates_ratings[random_restaurant] = user_update      
        
        except ValueError:
            print "?!? That wasn't a valid entry"
            print "You can quit anytime by entering the letter q."

    return user_updates_ratings


def user_adds_restaurant(user_updated_ratings):
    """takes in user restaurant and adds it to restaurant_rating dict"""

    updated_restaurants = user_updates_ratings
    user_restaurant = raw_input("Now Let's add your favorite restaurant!\
                                What restaurant do you want to add? ")
    user_rating = raw_input("Rate your restaurant between 1-5, 5 being the best: ")    
    
    if user_restaurant not in updated_restaurants:
        updated_restaurants[user_restaurant] = int(user_rating)

    print "Thanks! These are our current ratings: "


    return sort_restaurant_dict(updated_restaurants) 



def sort_restaurant_dict(updated_ratings):
    """sorts restaurant_rating dict and outputs in alphabetized by restaurant string"""

    #create list of tuples of restaurant and rating, returns sorted list by restaurant name
    restaurant_list = sorted(updated_ratings.items())
    
    #loops through sorted restaurant_list to print string
    for restaurant, rating in restaurant_list:
        print " {} is rated at {}.".format(restaurant,rating)


user = welcome()    
restaurant_rating = convert_text_to_dict("scores.txt")
user_updates_ratings = user_updates_rating(restaurant_rating)
restaurant_rating = user_updates_rating(user_updates_ratings)
user_adds_restaurant(restaurant_rating)
