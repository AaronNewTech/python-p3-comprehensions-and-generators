#!/usr/bin/env python3

def return_evens(num_list):
    # this way is more verbose than the one below and is easier to understand

    # new_list = list()
    # for i in num_list:
    #     if i % 2 == 0:
    #         new_list.append(num_list[i])
    # return new_list
        
    # this way is less verbose than the one above but needs to be explained like this. The first num is declaring the num we desire to add to our new list that passes the conditons in the for loop
    new_list = [num for num in num_list if num % 2 == 0]
    return new_list

        
    pass

def make_exclamation(sentence_list):

    # this way is more verbose than the one below and is easier to understand
    # new_list = list()
    # for sentence in sentence_list:
    #     new_list.append(sentence + '!')
    # return new_list

    # this way is less verbose than the one above but needs to be explained like this. The first sentence is declaring the sentence we desire to add to our new list that passes the conditons in the for loop
    new_list = [sentence + '!' for sentence in sentence_list]
    return new_list
    pass