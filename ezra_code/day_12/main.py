'''
- Function called count_dots. 
- This function takes a string separated by dots as a parameter and counts how many 
dots are in the string.
'''

def count_dots(string):
    count = 0
    for dot in string:
        if dot == '.':
            count += 1
    
    return count

user_input = input('Write down a word, with each letter seperated by a dot: ').lower()

print(count_dots(user_input))