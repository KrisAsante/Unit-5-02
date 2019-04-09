# Created by: Chris Asante
# Created on: 9-April-2019
# Created for: ICS3U
# Unit 5-02
# This program makes an array of 10 random numbers from 1 to 10 and then finds the largest value of these 
# numbers

import random

def find_max_value(array):
    max_value = max(array)   
    return max_value 

counter = 0
random_numbers = []

while counter < 6:
    single_number = random.randint(1, 6 + 1)
    print(single_number)
    random_numbers.append(single_number)
    counter = counter + 1

largest_value = find_max_value(random_numbers)

print("\nThe largest value in the array is " + str(largest_value) + ".")

