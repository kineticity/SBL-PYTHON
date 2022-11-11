from pprint import pprint
t=()
l=[]
def menu():
    print('''MENU
    1.Create and display tuple
    2.Display Details of student Python
    3.Sort the nested tuple
    4.Exit
    ''')
    return int(input("Enter choice:"))
def read():
    global t
    global n
    n=int(input("Enter no. of students:"))
    for i in range(n):
        print("Enter details of student",i+1,":")
        name=input("Enter name:")
        roll=input("Enter roll no.:")
        print("Enter marks of 3 subjects:")
        marks=[int(x) for x in input().split()]
        t1=(roll,name,marks)
        l.append(t1)
    t=tuple(l)
    print("Student Details:")
    for j in range(n):
        print("Roll no.:",t[j][0])
        print("Name:", t[j][1])
        print("Marks:", t[j][2])
        print("---------------")
    return n
def find(n):
    flag=0
    for i in t:
        if i[1]=="Python":
            print("Python present")
            pprint(i)
            flag=1
            break
    if flag==0:
        print("Python absent")
def sort():
    sortedt=sorted(t,key=lambda x:x[1])
    print("The sorted tuple is given:")
    pprint(sortedt)
c=0
while(c!=4):
    c=menu()
    if c==1:
        read()
    elif c==2:
        find(n)
    elif c==3:
        sort()
    elif c==4:
        print("Exiting...")
        break
    else:
        print("Invalid option")


