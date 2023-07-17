'''
a function called string_range that takes a single 
number and returns a string of its range.
'''

def string_range(number):
    new_string = ''
    for num in range(number):
        if num == 0:
          new_string += f'{num}'
        else:
           new_string += f'.{num}'
    
    return new_string

print(string_range(6))
