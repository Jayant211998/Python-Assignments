outfile=open("read.txt",'w')
outfile.write("Jayant Gawali\n")
outfile.write("Himanshu Lade\n")
outfile.write("Mihir Soni")
outfile.close()
infile=open("read.txt","r")
f=infile.readlines()
for i in f:
    print(i.rstrip('\n'))

