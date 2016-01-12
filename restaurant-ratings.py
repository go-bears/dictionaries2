# your code goes here
import sys

#filename = "scores.txt" sys.argv[1]

def convert_text_to_dict(filename):
    """converting scores.txt into restaurant rating 
    dictionary
    """

    restaurant_rating = {}

    for scores_data in open(filename):
        scores_data = scores_data.rstrip().split(":")
        restaurant, rating = scores_data
        # print restaurant, rating
        
        if restaurant not in restaurant_rating:
            restaurant_rating[restaurant] = int(scores_data[1])
           
    return restaurant_rating

restaurant_rating = convert_text_to_dict("scores.txt")

def sort_restaurant_dict(restaurant_rating):
    """doc string here"""

    restaurant_list = sorted(restaurant_rating.items())
    
    for restaurant, rating in restaurant_list:
        print " %s is rated at %d" % (restaurant,rating)

sort_restaurant_dict(restaurant_rating)