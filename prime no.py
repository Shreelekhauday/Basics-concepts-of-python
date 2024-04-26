#prime no
num=2
if num==1:
    print(num,"is not prime no")
elif num>1:
    for i in range(2,num):
        if(num%1)==0:
            print(num,"is not prime no")
            print(1,"times",num//1,"is",num)
            break
    else:
        print(num,"is prime no")

