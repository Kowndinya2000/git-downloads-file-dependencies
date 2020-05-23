f = open("csharp.txt","r")
for x in f:
    fp = open("csharp.sh","a")
    fp.write("git clone https://github.com/"+x) 
    fp.close()
f.close()   