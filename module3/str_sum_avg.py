s=list(map(str,input().split(" ")))
print("sum "+str(sum([int(i) for i in s if i.isnumeric()]))+" percentage "+str(sum([int(i) for i in s if i.isnumeric()])/len([int(i) for i in s if i.isnumeric()])))