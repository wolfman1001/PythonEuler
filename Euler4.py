#Find the largest palindrome made from the product of two 3-digit numbers.
max = 0
for i in range(900,999):
    for n in range(900,999):
        if str(i*n) == (str(i*n))[::-1]:
            if (i*n) > max:
                max = i*n
print(max)
