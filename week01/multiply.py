for i in  range(1,10):
    for j in range(1,i+1):
        print('%d*%d=%d\t' %(i,j,i*j),end='\t')
    print()

for i in range(1,10):
    for j in range(1,i+1):
         print(str(i) + '*' + str(j) + '=' + str(i*j),end=' \t')
#        print('%d*%d=%d\t' %(i,j,i*j),end=' \t')
    print()

for i in range(1,10):
    line=''
    for j in range(1,i+1):
        line+='{0}*{1}={2:<4}'.format(i,j,i*j)
    print(line)

for i in range(1,10):
    for j in range(1,10):
        if i>j:
            line='{} {} {:<4}'.format(' ',' ',' ')
        else:
            line='{0}*{1}={2:<4}'.format(i,j,i*j)
        print(line,end='')
    print()

for i in range(1,10):
    for m in range(i-1):
        line='{0} {1} {2:<4}'.format(' ',' ',' ')
        print(line,end='')
    for j in range(i,10):
        line='{0}*{1}={2:<4}'.format(i,j,i*j)
        print(line,end='')
    print()

for i in range(1,10):
    print(' '*8*(i-1),end='')
    for j in range(i,10):
        line='{0}*{1}={2:<4}'.format(i,j,i*j)
        print(line,end='')
    print()

