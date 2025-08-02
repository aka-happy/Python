# Create two lists by taking inputs and then merge the two lists

n1 = int(input("Enter the range: "))

my_list1 = []
my_list2 = []
while(n1>0):
    x = int(input())
    my_list1.append(x)
    print(my_list1)
    n1-=1

n2 = int(input("Enter the range: "))

while(n2>0):
    y = int(input())
    my_list2.append(y)
    print(my_list2)
    n2-=1

my_list1.extend(my_list2)
print(my_list1)
