'''
a function called zeroed code that takes a list of numbers 
as an argument. And zeros the first and last arguments in a list
'''

def zeroed(list):
    list[0] = 0
    list[len(list) - 1] = 0
    return list

test = [2, 5, 7, 8, 9]
print(zeroed([2, 5, 7, 8, 9]))