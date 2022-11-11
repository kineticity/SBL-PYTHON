l = []
l1 = []
l2 = []
def menu():
    print("MENU: "
          "\n1. Even and odd "
          "\n2. Merge and sort "
          "\n3. Update and delete "
          "\n4. Max and min "
          "\n5. Add name to list "
          "\n6. Exit")
    return int(input("Enter your choice: "))
def even_odd():
    for i in l:
        if i%2 == 0:
            l1.append(i)
        else:
            l2.append(i)
    print("The list with even elements is: ",l1)
    print("The list with odd elements is: ",l2)
def merge():
    l3=l1+l2
    print("The merged list is: ",l3)
    l3.sort()
    print("The list in ascending order: ",l3)
    print("The list in descending order: ",l3[::-1])
def update():
    x = int(input("Enter x: "))
    l[0]=x
    print("The updated list: ",l)
    l.pop(n//2)
    print("List after deleting middle element: ",l)
def max_min():
    print("Max element: ",max(l))
    print("Min element: ",min(l))
def add():
    n1 = int(input("Enter the number of strings: "))
    for j in range (0,n1):
        s = input()
        l.append(s)
    print("The updated list is: ",l)
    if 'Python' in l:
        print("Python is present in the list.")
    else:
        print("Python is not present in the list.")
n = int(input("Enter no. of elements in the list: "))
for i in range(n):
    e=int(input("Enter element:"))
    l.append(e)
print("The list: ",l)
c = 0
while (c!=6):
    c = menu()
    if c ==1:
        even_odd()
    elif c==2:
        merge()
    elif c==3:
        update()
    elif c==4:
        max_min()
    elif c==5:
        add()
    elif c!=6:
        print("Invalid choice!")
        break
