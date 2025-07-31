#Count character occurrences in a string

str = input("Enter the string: ")
char = input("Enter the character from string: ")

count = 0
for i in range(0, len(str)):
  if(str[i] == char):
   count+=1
  
print(count)
