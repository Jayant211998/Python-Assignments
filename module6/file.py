outfile=open("read.txt",'w')
outfile.write("Jayant Gawali")
outfile.write("Himanshu Lade")
outfile.write("Mihir Soni")
outfile.close()
infile=open("read.txt","r")
f=infile.read()
print(f.rstrip("\n"))

