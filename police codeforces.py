event=int(input('enter the events'))
unsolved=0
no_of_police=0
if(event==-1):
    if(no_of_police==0):
        unsolved+=1
    else:
        no_of_police-=1
else:
    num_of_police=event+no_of_police