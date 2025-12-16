import os
paths=".//root//"
r="/"
def copys(s1:str,s2:str):
    s=b""
    f1=open(s1,"rb")
    f2=open(s2,"wb")
    s=f1.read()
    f2.write(s)
    f1.close()
    f2.close()
print("\033c\033[40;37m\ngive me a list file to create tree ? ")
i=input()
f1=open(i,"r")
ff=f1.read()
f1.close()
fff=ff.split(",")
os.mkdir(paths)
for f in fff:
    f=f.strip()
    if f[0:1]=="!":
        ff=f[1:]
        copys(r+ff,paths+ff)
        os.chmod(paths+ff,0o777)
    else:
        os.mkdir(paths+f)