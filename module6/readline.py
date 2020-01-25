outfile=open("read.txt",'w')
outfile.write("Jayant Gawali\n")
outfile.write("Himanshu Lade\n")
outfile.write("Mihir Soni")
outfile.close()
infile=open("read.txt","r")
f=infile.readline()
print(f)

