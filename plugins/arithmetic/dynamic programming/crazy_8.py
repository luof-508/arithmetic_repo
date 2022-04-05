import numpy as np


def join_able(ci, cj):
    if ci[0] == '8' or cj[0] == '8':
        return True
    elif ci[1] == cj[1]:
        return True
    elif ci[0] == cj[0]:
        return True
    return False


def max_seq_card(lst):
    trick = {}
    parent = {}
    trick[0] = 1
    parent[0] = None
    for i, ci in enumerate(lst):
        tem_trick = []
        if i > 0:
            for j, cj in enumerate(lst[:i]):
                if join_able(ci, cj):
                    tem_trick.append(trick[j])
                else:
                    tem_trick.append(0)
            max_trick = max(tem_trick)
            trick[i] = 1 + max_trick
            ind_max =np.argmax(tem_trick)
            if join_able(ci, lst[ind_max]):
                parent[i] = ind_max
            else:
                parent[i] = None
    return trick, parent


def card_lst(number):
    import random
    option = '234567890JQKA'
    car_color = 'qwer'
    c_lst = [0] * number
    for i in range(number):
        c_l
