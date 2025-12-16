import os
import shutil
paths="./root/"
r="/"
def copys(s1:str,s2:str):
    s=b""
    try:
        f1=open(s1,"rb")
        f2=open(s2,"wb")
        s=f1.read()
        f2.write(s)
        f1.close()
        f2.close()
    except:
        print("file error: "+s1)
def dirs(f):
    ff=f.replace("//","/")
    d=ff.split("/")
    aa=d[:len(d)-1]
    a="/".join(aa)
    os.makedirs(a,0o777,True)
   
def ppath(spath,rpath):
    print("------------------------------")
    f1=open("/tmp/out.txt","r")
    s=f1.read()
    f1.close()
    ss=s.split("\n")
    for n in ss:
        n=n.strip()
        if n!="":
            sss=n.split("(")
            if sss[0].find("=>")<0:
                if sss[0].find("/")>-1:
                    nnn=sss[0].strip()
                    
                    dirs(spath+nnn)
                    copys(rpath+nnn,spath+nnn)
                else:
                    nnn=sss[0].strip()
                    print(nnn)
            else:
                nn=sss[0].split("=>")
                nnn=nn[1].strip()
                dirs(spath+nnn)
                copys(rpath+nnn,spath+nnn)
print("\033c\033[40;37m\ngive me a list file to create tree ? ")
i=input()
i=i.strip()
f1=open(i,"r")
ff=f1.read()
f1.close()
print("\033[40;37m\ngive me a binary file to start up ? ")
ii=input()
ii=ii.strip()

fff=ff.split(",")
os.makedirs(paths,0o777,True)
for f in fff:
    f=f.strip()
    if f[0:1]=="!":
        ff=f[1:]
        copys(r+ff,paths+ff)
        os.chmod(paths+ff,0o777)
        os.system("ldd $1 > /tmp/out.txt".replace("$1",paths+ff))
        ppath(paths,r)
    else:
        os.makedirs(paths+f,0o777,True)
ss="genisoimage -o disk.iso -input-charset utf-8 -b $1 -no-emul-boot -boot-load-size 4  -boot-info-table $2 ".replace("$2",paths).replace("$1",ii)
print(ss)
os.system(ss)
