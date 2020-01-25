s=list(map(str,input("").split(",")))
a,b=sum([int(s[1]),int(s[2]),int(s[3]),int(s[4]),int(s[5])]),sum([int(s[6]),int(s[7])])
print(s[0]+" obtained "+str(sum([int(s[1]),int(s[2]),int(s[3]),int(s[4]),int(s[5])]))+"marks out of 500 and "+ str(sum([int(s[6]),int(s[7])])) + "marks out of 40. Aggregate is "+str((sum([a,b])/590)))