print('Please enter 5 number,use\',\' to split:')
num = input('>>>').strip().lstrip(' 0')
inputlst = num.split(',')
intinput=[]
if len(inputlst) == 5:
    for i in inputlst:
        i = int(i)
        intinput.append(i)
else:
    print('You must enter 5 number.')
intinput.sort()
print(intinput)


#方法二
lst=[]
for i in range(5):
    lst.append(int(input('{}:').format(i)))
lst.sort()
print(lst)
