"""
price = [2,5], special = [[3,0,5],[1,2,10]], needs = [3,2]
1、需要的商品种类n，给出没种商品的单价和需要购买的数量。
2、给出大礼包组合，组合构成为：n种商品一定数量的组合，所需要的价格。

求解：
搜索算法：从special中下标idx=0开始搜索，当前n项special[idx]的其中一种商品数量和大于等于需要的数量时，停止搜索，并将数量不够的商品，按单价购买，算出总的价格。
1、深度搜索-->获取到目标值，返回上一层再广度搜索，与前值对比，保留总价最小的。
2、滑动索引，继续步骤1
"""

class Solution:
    def __init__(self):
        self.team = {}

    def shopping_offers(self, price: list, special: list, needs: list) -> int:
        idx = 0
        return self.bfs_search(price, special, needs, idx)

    def bfs_search(self, price, special, needs, idx):
        cur_package = special[idx]
        for i, need in enumerate(needs):
            if special[i] > need:
                break
        self.team[idx] = special[idx]
        return self.bfs_search(price, special, needs, idx+1)


class Solution:
    def shopping_offer(self, price, special, needs) -> int:
        # ----check当前这个礼品，是否合理（不能超，不能多买）
        def check(spe: list, cur_need: list) -> bool:
            for sp, cur in zip(spe, cur_need):
                if sp > cur:
                    return False
            return True

        def dfs(cur_need: list, cur_cost: int) -> None:
            nonlocal res
            if cur_cost >= res:
                return
            if sum(cur_need) == 0:
                res = min(res, cur_cost)
                return

            match = False
            # ----尝试每个大礼包
            for spe in special:
                if check(spe, cur_need) == True:
                    match = True
                    # ----对应的物品，需求数量减少
                    for j in range(len(cur_need)):
                        cur_need[j] -= spe[j]
                    dfs(cur_need, cur_cost + spe[-1])
                    for j in range(len(cur_need)):
                        cur_need[j] += spe[j]
            # ----如果不能使用大礼包，只能单独买了
            if match == False:
                for i in range(len(price)):
                    cur_cost += price[i] * cur_need[i]
                res = min(res, cur_cost)

        n = len(price)
        res = float('inf')

        # ----合理的大礼包，往前挪。不合理的不要了
        k = 0
        for i in range(len(special)):
            # ----买这个大礼包不会买多东西
            if check(special[i], needs) == True:
                tmp_cost = 0
                for j in range(n):
                    tmp_cost += price[j] * special[i][j]
                if special[i][-1] < tmp_cost:
                    special[k] = special[i]
                    k += 1

        special = special[:k]

        dfs(needs, 0)
        return res

