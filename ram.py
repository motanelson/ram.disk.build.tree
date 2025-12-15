import os
paths=".//root//"
print("\033c\033[40;37m\ngive me a list file to create tree ? ")
i=input()
f1=open(i,"r")
ff=f1.read()
f1.close()
fff=ff.split(",")
os.mkdir(paths)
for f in fff:
    os.mkdir(paths+f)