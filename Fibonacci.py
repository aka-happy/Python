# Print Fibonacci series

n = int(input("Enter the number"))

a = 0
b = 1
print(a)

for i in range(0, n):
    c = a + b
    a = b
    b = c
    print(a)
