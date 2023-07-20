'''
- a function called zeros_last.
- This function takes a list as argument.
- If a list has zeros (0), it will move them to the front of the list and maintain the order of the other numbers in the list.
- If there are no Zeros in the list, the function should returns the original list sorted in ascending order.
'''


def zeros_list(list):
    for index in range(0, len(list)):
        for num in list:
            if num == 0:
                if index + 1 < len(list) - 1:
                    print(f"{index} : index")
                    temp = list[index + 1]
                    print(f"This is temp: {temp}")
                    list[index + 1] = list[index]
                    list[index] = temp
                else:
                    temp = list[len(list) - 1]
                    print(f"This is temp: {temp}")
                    list[len(list) - 1] = list[index]
                    list[index] = temp

    return list


test = [0, 2, 0, 1, 4, 0, 7, 6]
print(zeros_list(test))
