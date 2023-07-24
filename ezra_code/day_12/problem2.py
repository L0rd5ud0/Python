'''
A function called age_in_minutes that tells a user how 
old they are in minutes.
'''
from datetime import date

#Adds commas to the minutes 
def convert_numbers(num):
        new_num = str(num)
        num_str = ''

        # The range skips every 3 numbers inorder to add a comma to every three spaces
        for index in range(0, len(new_num), 3):
            # Checks if the number is divisble by 1000
            # if it has reminders this part adds the commas
            # if the number isn't divisble by 1000, as a reminder is produced then it moves on to the else statement
            if num // 1000 != 0:
                if (num % 1000 > 99):
                  num_str = ',' + str(num % 1000) + num_str
                elif (num % 1000 <= 99 and num % 1000 > 9):
                    num_str = ',0' + str(num % 1000) + num_str
                elif (num % 1000 >= 0):
                    num_str = ',00' + str(num % 1000) + num_str
                num = num // 1000
            else:
                num_str = str(num) + num_str

        return num_str

#takes in the current year and birth year and calculates age in minutes
def age_in_minutes(birth_year, current_year):
    age = current_year - birth_year
    age_in_minutes = age * 525600
    
    print(f"You are {convert_numbers(age_in_minutes)} minutes old")

current_year = date.today().year
user_birth_year = int(input("What year were you born: ") )

#Checks if a user has input a valid year
while user_birth_year < 1930 or user_birth_year > current_year:
        user_birth_year = int(input(f"You have entered an that's off, please enter a year between 1930 and {current_year} : "))

age_in_minutes(user_birth_year, current_year)

