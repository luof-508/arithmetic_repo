n=int(input('enter a number:'))
for i in range(0,n,1):
    if i==0 or i==(n-1):
        print("*\t "*n)
    else:
        print("*\t"," \t"*(n-2),"*")
