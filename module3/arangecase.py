s=input()
t,l="",""
for i in s:
    if i.islower():
        t+=i
    else:
        l+=i
print(t+l)
    