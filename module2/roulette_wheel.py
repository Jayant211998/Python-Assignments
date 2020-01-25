n=int(input(""))
if n==0:
    print("color is green")
elif (n>=1 and n<=10 and n%2==1) or (n>=11 and n<=18 and n%2==0) or (n>=19 and n<=28 and n%2==1) or (n>=29 and n<=36 and n%2==0):
    print("color is red")
elif(n>=1 and n<=10 and n%2==0) or (n>=11 and n<=18 and n%2==1) or (n>=19 and n<=28 and n%2==0) or (n>=29 and n<=36 and n%2==1):
    print("color is black")
else:
    print("Error: Enter valid number(between 0 and 36)")