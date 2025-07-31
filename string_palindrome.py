#Check if a string is a palindrome

str = input("Enter the string: ")
rev = (str[::-1])

if(str == rev):
       print("This string is a Palindrome")

else:
       print("This string is not a Palindrome")


#using loop (can also refer to my reverse_string file):

str = input("Enter the string: ")

rev = ''

for i in range(1, len(str)+1):
  rev = rev + str[(len(str)) - i]

if(str == rev):
       print("This string is a Palindrome")

else:
       print("This string is not a Palindrome")


