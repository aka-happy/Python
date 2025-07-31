#Swap two numbers without using a temporary variable

#using integers:

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

a = a+b
b = a - b
a = a - b

print("a = ", a)
print("b + ", b)




#using string:

a = str(input("Enter first number: ")) #may avoid writing str as by default the number is stored as string
b = str(input("Enter second number: ")) #may avoid writing str as by default the number is stored as string

a+b
print("a = ", (a+b)[len(a):])
print("b = ", (a+b)[:len(a)])
