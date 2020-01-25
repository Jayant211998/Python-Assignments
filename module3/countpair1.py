s=int(input("Enter sum"))
a=list(map(int,input().split(" ")))
count=0
for i in a:
    if (s-i) in a:
        print("yes")
        break