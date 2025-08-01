# Find the max number from the given range of numbers

n = int(input("Enter the range: "))
max = 0
while(n > 0):
    x = int(input())
    n-=1
    
    if(max>x):
       a = max
    else:
       a = x
    max = a
    
print("Max is",a)
