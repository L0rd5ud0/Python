'''
- a function called zeros_last.
- This function takes a list as argument.
- If a list has zeros (0), it will move them to the front of the list and maintain the order of the other numbers in the list.
- If there are no Zeros in the list, the function should returns the original list sorted in ascending order.
'''


def zeros_list(list):
    for index in range(0, len(list)):
        #checks if at that index the value is 0
        if list[index] == 0:
            #removes it from the list
            x = list.pop(index)
            #appends it to the end of the list
            list.append(x)

    return list


test = [0, 2, 0, 1, 4, 0, 7, 6]
print(zeros_list(test))
