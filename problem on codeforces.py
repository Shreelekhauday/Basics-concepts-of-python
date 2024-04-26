w=int(input("weight of watermelon"))
if (w%2!=0):
    print("NO")
else:
    x=w/2
    if(x%2==0):
        print("x1=",x,"and" "x2=",x)
    else:
        print("x1=","x-1","and","x2=",x+1)