Ques1:
for i in range(9):
    for j in range(5):
        if i<=4 and i+j<=4:
            print("*",end=" ")
        if i>4 and i-j>=4:
            print("*",end=" ")
    print()
    
Ques2:
n=13
for i in range(n):
    for j in range(n):
        if j==n//2:
            print("*",end=" ")
        elif i==n//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

Ques 3:
for i in range(4):
    for j in range(7):
        if i+j>=3 and j-i<=3:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
for i in range(4,7):
    for j in range(7):
        if i+j<=9 and i-j<=3:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

Ques4:

n=9
for i in range(8):
    if i==5:
        for j in range(10):
            print("*",end=" ")
    else:
        for j in range(10):
            if i+j==4 or j-i==4:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        
    print()