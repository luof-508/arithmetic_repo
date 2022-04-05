def bottom_up_coins(c=None):
    c = c[:]
    c.insert(0, 0)
    n = len(c)
    dp = [None] * (n)
    dp[0] = 0
    dp[1] = c[1]
    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2] + c[i])
    return dp


def trace_back_coins(c, dps):
    i = len(dps)-1
    pick_up_coins = []
    n = 0
    while i+1:
        if dps[i] > dps[i-1]:
            pick_up_coins.append(c[i-1])
            i -= 2
        else:
            i -= 1
    return pick_up_coins


c1 = [5, 1, 2, 10, 6, 2]
dp1 = bottom_up_coins(c1)
pick = trace_back_coins(c1, dp1)
print(dp1)
print(pick)
