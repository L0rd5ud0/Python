'''
A function called prime_numbers. 
This function asks a user to enter a number (integer) as an argument and returns a 
list of all the prime numbers within its range
'''

'''
Prime number rules:
- Greater than 1
- cannot be divided by any other positive integers
- only divisble by itself and one
'''

def is_prime(num):
    #Checks if number is prime or not
    prime_num = False
    if num == 2:
        return True
    else:
      for i in range(2, num):
          #this checks if the number is divisible by the iterator
          if num % i == 0:
              prime_num = False
              break
          else:
              prime_num = True
            
    return prime_num

def prime_numbers(int):
    numbers = []
    for i in range(2, int + 1):
        if is_prime(i):
            numbers.append(i)
        
    return numbers

print(prime_numbers(13))