num=int(input('Enter a number:'))
fac=1
sum=0
for i in range(1,num+1):
    fac*=i
    sum+=fac
else:
    print('The sum of factorial is:',sum)
