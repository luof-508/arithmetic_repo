import sys


def cal(seq, n):
    tmp = len(seq)
    if tmp < 2*n:
        return -1
    return sum(seq[:n]) + sum(seq[:-n-1:-1])


while True:
    try:
        M = int(sys.stdin.readline().strip())
        lst = sorted(set(map(int, sys.stdin.readline().strip().split())))
        N = int(sys.stdin.readline().strip())
        re = cal(lst, N)
        if re == -1:
            print(-1)
        else:
            print(re)
    except:
        break
