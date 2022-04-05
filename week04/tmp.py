import sys
file = open('../huawei/test.txt', encoding='utf-8')

strings = sys.stdin.readline()
new_strings = strings.strip(' .\n')
sep_str = new_strings.split(' ')
print(len(sep_str[-1]))
