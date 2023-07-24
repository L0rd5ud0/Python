'''
- a function called biggest_odd that takes a string of 
numbers and returns the biggest odd number in the list.
'''

def biggest_odd(string):
    #list comprehensions operate just like a for loop with a conditional attached
    '''
      What the code below is saying is:
        for x in string:
            if not int(x) % 2 == 0:
                odd_nums.append(x)
    '''
    odd_nums = [x for x in string if not int(x) % 2 == 0]
    max_odd = max(odd_nums)
    return max_odd
        
print(biggest_odd('23569'))