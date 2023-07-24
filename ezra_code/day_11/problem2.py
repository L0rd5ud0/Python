def swap_values(list):
    x = list.pop(len(list) - 1) #
    y = list.pop(0)
    list.insert(0, x)
    list.append(y)

    return list

print(swap_values( [2, 4, 67, 7]))