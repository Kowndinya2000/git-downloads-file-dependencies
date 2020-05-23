f = open("python.txt","r")
for x in f:
    fp = open("python.sh","a")
    fp.write("git clone https://github.com/"+x) 
    fp.close()
f.close()   