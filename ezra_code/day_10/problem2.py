def convert_numbers(list):
    converted_nums = []
    # seperate each number
    for num in list:
        #convert number into a string for easy concatenation
        new_num = str(num)
        num_str = ''
        
        #The range skips every 3 numbers inorder to add a comma to every three spaces
        for index in range(0, len(new_num), 3):
            #Checks if the number is divisble by 1000
            #if it has reminders this part adds the commas
            #if the number isn't divisble by 1000, as a reminder is produced then it moves on to the else statement
            if num // 1000 != 0:
                if(num % 1000 > 99):
                  num_str = ',' + str(num % 1000) + num_str  
                elif(num % 1000 <= 99 and num % 1000 > 9):
                    num_str = ',0' + str(num % 1000) + num_str
                elif(num % 1000 >= 0 ):
                    num_str = ',00' + str(num % 1000) + num_str
                num = num // 1000
            else:
                num_str = str(num) + num_str
            
        converted_nums.append(num_str)

    return converted_nums


print(convert_numbers([1000000, 2356989, 2354672, 9878098, 1]))
