#Write code to reverse a string.

#using loop:
str = (input("Enter the string"))

rev = ''
i = 0
for i in range(1, len(str)+1):
  rev = rev + str[len(str)-i] 

print(rev)



#using string
str = input("Enter your string")
print(str[::-1])
  
