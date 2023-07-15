'''
A program that will count how many males and females are in the list.
'''

students = ['Male', 'Female', 'female', 'male', 'male', 'male','female', 'male', 'Female', 'Male', 'Female', 'Male', 'female']

def enrollment(list):
    male_counter = 0
    female_counter = 0
    for sex in list:
        sex = sex.lower()
        if sex == "male":
            male_counter += 1
        elif sex == "female":
            female_counter += 1
    males = tuple(['Male', male_counter])
    females = tuple(['female', female_counter])

    return [males, females]

print(enrollment(students))