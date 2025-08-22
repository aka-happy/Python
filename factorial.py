# Calculate the factorial of a number

number = int(input("Enter the number: "))

fact = 1
while(number>0):
  fact*= number
  number-= 1

print(fact)


# using for loop

n = int(input("Enter your number: "))

fact = 1
for i in range(1, n+1):
    fact*= i

print(fact)


# using recursion function

def fact(n):
    if(n == 1):
        return 1    
    else:
        return n*fact(n-1)
    
print(fact(5))


