count=0
sum=0

while True:
    num=input('Enter a number,if you want to stop,just enter q>>>')
    if num == 'q':
        break
    num=int(num)
    sum+=num
    count+=1
    ave=sum/count
    print('average:',ave)
