n=int(input("no.of terms"))
n1,n2=0,1
count=0
if n<=0:
    print("invalid input")
elif n==1:
    print(n1)
else:
    print("fibonacci series is")
    while count<n :
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count+=1
