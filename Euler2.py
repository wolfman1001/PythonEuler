#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
fib = 2
prev = 1
sum = 0
while fib < 4000000:
    if fib % 2 == 0:
        sum = sum + fib
    fib = fib + prev
    prev = fib - prev
print(sum)