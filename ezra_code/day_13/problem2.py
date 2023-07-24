'''
a function called Python_snakes that takes a number
as an argument and creates the following shape
      ⠦
     ⠦ ⠦
    ⠦ ⠦ ⠦
   ⠦ ⠦ ⠦ ⠦
  ⠦ ⠦ ⠦ ⠦ ⠦
 ⠦ ⠦ ⠦ ⠦ ⠦ ⠦

'''

def Python_snakes(num):
    space = num - 1
    count = 1
    for shape in range(num - 1):
        print(' ' * space + ('🤼 ' * count))
        space -= 1
        count += 1

user_num = int(input("Enter a number and watch the magic unfold: "))

Python_snakes(user_num)

