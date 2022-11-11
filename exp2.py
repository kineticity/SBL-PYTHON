num=int(input("Enter a number:"))
temp=num
rev=0
while(num!=0):
    dig=num%10
    rev=rev*10+dig
    num=num//10
if(temp==rev):
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")

str=input(("Enter a string:"))
if(str==str[::-1]):
      print("The string is a palindrome")
else:
      print("The string is not a palindrome")

def fact(x):
    if((x==1)or(x==0)):
        return 1
    else:
        return (x*fact(x-1))

x= int(input("Enter a number:"))
print("Factorial is: ",fact(x))
