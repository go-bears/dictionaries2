# your code goes here
import sys

def convert_text_to_dict(filename):
    """converting scores.txt into restaurant rating 
    dictionary
    """
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


def sort_restaurant_dict(restaurant_rating):
    """sorts restaurant_rating dict and outputs in alphabetized by restaurant string"""

    #create list of tuples of restaurant and rating
    #and returns sorted list by restaurant name
    restaurant_list = sorted(restaurant_rating.items())
    
    #loops through sorted restaurant_list to print string
    for restaurant, rating in restaurant_list:
        print " %s is rated at %d." % (restaurant,rating)

restaurant_rating = convert_text_to_dict("scores.txt")
sort_restaurant_dict(restaurant_rating)