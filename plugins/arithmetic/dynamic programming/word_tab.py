# 包含父节点的动态规划表
def word_tab(word_lst, width):
    m = len(word_lst)
    word_lst.insert(0, 0)
    dp = []
    n = m + 1
    dp.append([0, -1])
    for i in range(1, n):
        possible = {}
        for j in range(0, i):
            if sum(word_lst[i-1:i+1]) > width:
                possible[word_lst[i]**3] = i-1
                break
            if sum(word_lst[j+1:i+1]) <= width:
                mid = dp[j][0]
                keys = mid + (width-sum(word_lst[j+1:i+1]))**3
                possible[keys] = j
        key = min(possible.keys())
        value = possible[key]
        dp.append([key, value])
    return dp


w = [5, 5, 5, 5, 14]
p = 18
dp_lst = word_tab(w, p)
print(dp_lst)
