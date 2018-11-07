import os

count = 0
with open("a.txt",'a+') as f:
    f.write("A")
    data = f.readlines()
    for line in data:
        count = count + len(line.strip())

os.system("git commit -am The %s times commit" %count )
os.system("git push")
