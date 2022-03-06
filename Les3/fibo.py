fib0 = 0
fib1 = 1
fibn = 1
n = int(input("how many? "))

if (n >= 0):
    print(0)
if (n >= 0):
    print(1)

for i in range(0,n - 2):
    fibn = fib0 + fib1
    fib0 = fib1
    fib1 = fibn
    print(fibn)
