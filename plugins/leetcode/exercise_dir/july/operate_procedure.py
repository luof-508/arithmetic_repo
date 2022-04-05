# !/usr/bin/python
# coding: utf-8
from july import JulyExerciseList


class OperateProcedure(object):
    def __init__(self):
        self.exe_list = JulyExerciseList()

    def operate_method(self, *args, **kwargs):
        # attr = input('slect the attribute>>>').strip()
        cur_attr = getattr(self.exe_list, 'num_sub_array_with_sum')
        res = cur_attr(*args)
        return res


if __name__ == '__main__':
    # puts = input('enter you test>>>')
    deliciousness = [1,0,1,0,1]
    goal = 2
    my_or = OperateProcedure().operate_method(deliciousness, goal)
    print(my_or)


