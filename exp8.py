import os


def menu():
    print('''MENU
    1.To read content of file and write to another file
    2.To append data at the end of existing file
    3.To count no. of lines,words,characters in file
    4.To display files in a directory
    5.Exit
    ''')
    return int(input("Enter your choice:"))


c = 0
while c != 5:
    c = menu()
    if c == 1:
        fname1 = input("Enter first file name:")
        fname2 = input("Enter second file name:")
        f1 = open(fname1 + ".txt", "r")
        f2 = open(fname2 + ".txt", "w+")
        s = f1.read()
        f2.write(s)
        f1.close()
        f2.seek(0, 0)
        s = f2.read()
        print("The content of second file is :")
        print(s)
        f2.close()
    elif c == 2:
        fname = input("Enter file name:")
        f = open(fname + ".txt", "a+")
        s = input("Enter data to append:")
        f.write(s)
        f.seek(0, 0)
        s = f.read()
        print("The file after appending data is: ")
        print(s)
        f.close()
    elif c == 3:
        fname = input("Enter file name:")
        f = open(fname + ".txt", "r")


        a=f.read()
        char=0
        words=0
        lines=0
        for ch in a:
            char+=1
        print("Number of characters",char)
        for word in a.split():
            words+=1
        print("No. of words=",words)
        f.seek(0)
        for line in f:
            lines+=1
        print("No. of lines=", lines)

        '''lines = f.readlines()
        nlines = len(lines)
        nwords = 0
        ncharacters = 0
        print("No. of lines=", nlines)
        f.seek(0, 0)
        for i in lines:
            for j in i.split(" "):
                nwords += 1

        print("No. of words=", nwords)
        f.seek(0, 0)
        ncharacters = len(f.read())
        print("No. of characters(including end of line characters)=", ncharacters)'''
        f.close()
    elif c == 4:
        files = os.listdir('.')
        print("The files in current directory are: ")
        for i in files:
            print(i)
