import sys
list = ['d', 0,10]
for entry in list:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        list=list+"hehe"#type error
        break
    except:
        print("Oops!", sys.exc_info()[0], "occurred.")
        print("Next entry.")
print("The reciprocal of", entry, "is", r)
