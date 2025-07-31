#Find vowels in a string and print it in string and count the number of vowels in a string

str = input("Enter the string: ")

v = "aeiou"
a = ''
count = 0
for i in range(0, len(str)):
    if(str[i] in v):
        print(str[i])
        a = a + str[i]
        count+= 1

print(a)
print(count)
