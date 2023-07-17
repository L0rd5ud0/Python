# Write a function called longest_value that takes a dictionary as an argument and returns the first longest value of the dictionary. 
# For example, the following dictionary should return – apple as the longest value.
# fruits = {'fruit': 'apple', 'color': 'green'}

fruits = {'fruit': 'apple', 'color': 'green'}
def longest_value(dic):
    word_count = 0
    longest_word = ""
    for i in dic:
        if len(dic[i]) > word_count:
            word_count = len(dic[i])
            longest_word = dic[i]
    return longest_word