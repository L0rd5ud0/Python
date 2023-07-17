'''
a function called odd_even that has one parameter and
takes a list of numbers as an argument. 
The function returns the difference between the largest even number in the list and the 
smallest odd number in the list.
'''

def sort_list(arr):
    #This is insertion sort
    #Used to sort a list/array
	# Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        j = i - 1
        while j >= 0 and arr[j + 1] < arr[j]:
            # arr[j] and arr[j + 1] are out of order so swap them
            #tmp holds a next value temporarily
            tmp = arr[j + 1]
            arr[j + 1] = arr[j]
            #Swaps out the bigger value for the smaller value
            arr[j] = tmp
            j -= 1
    return arr     

def odd_even(list):
    #Two varible to hold the largest even num
    #Smallest odd num
    max_even = 0
    odd_numbers = []
    list = sort_list(list)
    #For loop to extract each number
    for num in list:
        #Extracting even num and odd
        if num % 2 == 0:
            if num > max_even:
                #Compares numbers
                max_even = num
        else:
            odd_numbers.append(num)
    
    return max_even - odd_numbers[0]

test = [2,4,6,23,21,54,124]

print(odd_even(test))
              