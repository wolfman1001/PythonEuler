#What is the largest prime factor of the number 600851475143 ?
import math
def isprime(num):
    if num == 2:
        return True
    elif num % 2 == 0:
        return False
    for i in range(3,num):
        if num % i == 0:
            return False
    return True

num = 600851475143
max = 0
for i in range(1, int(math.sqrt(num))):
    if num % i ==0:
        if isprime(i):
            max = i

print(max)
