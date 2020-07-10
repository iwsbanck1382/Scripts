import os
words={}
os.system("COLOR 1")
while True:
    INPUT=input("Say to me a simple :>>> ")
    try:
        print(words[INPUT])
        continue
    except:
        what=input("What 's the mean?>>> ")
        words[INPUT]=what
        print(what)
        os.system("cls")
        continue

