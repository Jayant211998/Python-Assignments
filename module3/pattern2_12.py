Ques1:
n=9
l=[]
for i in range(n):
    if i<=n//2:
        print("*"*((n//2+1)-i),end=" ")
    else:
        print("*"*((i-(n//2)+1)),end=" ")
    print()
        
Ques 2:
n=13
l=[]
for i in range(n):
    if i==n//2:    
        print("*"*n,end=(" "))
    elif i!=n//2:
        print(" "*(n//2),end=(""))
        print("*",end=(" "))
        print(" "*(n//2),end=(""))
    print()     

Ques3:
n=7
for i in range(n):
    if i==n//2:
        print("*"*(n),end=" ")
    else:
        print(" "*(abs((n//2)-i)),end="")
        print("*"*(n-2*(abs((n//2)-i))),end=" ")
    print()
Ques4:
n=9
for i in range(n):
    if i==0:
        print(" "*(n+1),end="")
        print("*")
    elif i==n-1:
        print(" ",end="")
        print("*"*(2*n+1),end=" ")
    else:
        print(" "*(abs(n-i)),end="")
        print("*",end=" ")
        print(" "*(i*2),end="")
        print("*")
print()
        
        