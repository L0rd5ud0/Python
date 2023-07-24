'''
- A function called equal_strings
- The function takes two strings as arguments and compares them. 
- If the strings are equal (if they have the same characters and have equal length), it 
should return True,
'''

def equal_strings(string1, string2):
    is_true = False
    if len(string1) == len(string2):
        for letter in string1:
            if letter in string2:
                is_true = True
    
    return is_true

user_input1 = input("What word would you like to compare first: ").lower()
user_input2 = input("What other word would you like to compare: ").lower()

print(equal_strings(user_input1, user_input2))