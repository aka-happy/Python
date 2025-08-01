# Find the prime numbers in a given range of number

n = int(input("Enter the range"))
a = 1

while(n > 0):
    x = int(input())
    n-=1

    if(x == 1):
        print(x, "is not a prime number")
    
    else:
        for i in range(2, x):
            if(x%i == 0):
                print(x, "is not a prime number")
                break
        else:
            print(x, "is a prime number")
