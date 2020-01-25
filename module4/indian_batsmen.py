n=int(input("Enter number of players"))
t=input("Enter the type of player")
d1={}
d1[t]={}
d2={}
for plyr in range(n):
    if(plyr!=0):
        tp=input("Enter the type of player")
        if(tp!=t):
            t=tp
            d1[t]={}
    name=input("Name of player")
    d1[t][name]={}
    d1[t][name]['Matches']=int(input("matches "))
    d1[t][name]['Runs']=int(input(" runs"))
    d1[t][name]['Average']=float(input("Average "))
    d1[t][name]['Highest_Score']=int(input("Highest score"))
for types in d1.keys():
    for name in d1[t].keys():
        d2[d1[t][name]['Highest_Score']]=name
print(d2[sorted(d2,reverse=True)[0]])
print(d1)
