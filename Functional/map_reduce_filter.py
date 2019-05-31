#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-29 10:38
# @Author  : minp
# @contact : king101125s@gmail.com
# @Site    :
# @File    : map_reduce_filter.py
# @Software: PyCharm

"""
map 函数的使用形式如下：
map(function, sequence)

解释：对 sequence 中的 item 依次执行 function(item)，并将结果组成一个 List 返回，也就是：

[function(item1), function(item2), function(item3), ...]

在 Python2 中 map 直接返回列表，Python3 中返回迭代器
"""


import unittest
from functools import reduce


def square(x):
    return x * x


def double(x):
    return 2 * x


def triple(x):
    return 3 * x


class Test(unittest.TestCase):

    # @unittest.skip('测试map')
    def test_map(self):
        """
        形式:     map(function, sequence)
        解释:     对 sequence 中的 item 依次执行 function(item) [function(item1), function(item2), function(item3), ...]
        返回类型:  Python2 中 map 直接返回列表，Python3 中返回迭代器
        """
        map1 = map(square, [1, 2, 3, 4])            # 通用入参
        map2 = map(lambda x: x * x, [1, 2, 3, 4])   # 使用 lambda
        map3 = map(str, [1, 2, 3, 4])               # str() 格式化为str类型
        map4 = map(int, ['1', '2', '3', '4'])       # int() 格式化为int类型
        funcs = [double, triple, square]            # 列表元素是函数对象
        map5 = list(map(lambda f: f(4), funcs))
        print('数据类型：', type(map1), list(map1))  # Python3 中返回迭代器 需要强转成list显示
        print(list(map2))
        print(list(map3))
        print(list(map4))
        print(list(map5))

    @unittest.skip('测试reduce')
    def test_reduce(self):
        """
        形式：reduce(function, sequence[, initial])
        解释：先将 sequence 的前两个 item 传给 function，即 function(item1, item2)，
            函数的返回值和 sequence 的下一个 item 再传给 function，即 function(function(item1, item2), item3)，
            如此迭代，直到 sequence 没有元素，如果有 initial，则作为初始值调用
        :return:
        """
        reduce1 = reduce(lambda x, y: x *
                         y, [1, 2, 3, 4])            # 相当于 ((1 * 2) * 3) * 4
        # ((((5 * 1) * 2) * 3)) * 4
        reduce2 = reduce(lambda x, y: x * y, [1, 2, 3, 4], 5)
        reduce3 = reduce(lambda x, y: x /
                         y, [2, 3, 4], 72)     # (((72 / 2) / 3)) / 4
        # ((((5 + 1) + 2) + 3)) + 4
        reduce4 = reduce(lambda x, y: x + y, [1, 2, 3, 4], 5)
        reduce5 = reduce(lambda x, y: x -
                         y, [8, 5, 1], 20)     # ((20 - 8) - 5) - 1

        def f(a, b): return a if (a > b) else b                    # 两两比较，取最大值
        reduce6 = reduce(f, [5, 8, 1, 10])
        print(reduce1)
        print(reduce2)
        print(reduce3)
        print(reduce4)
        print(reduce5)
        print(reduce6)

    @unittest.skip('测试filter')
    def test_filter(self):
        """
        形式：filter(function, sequnce)
        将 function 依次作用于 sequnce 的每个 item，即 function(item)，将返回值为 True 的 item 组成一个 List/String/Tuple
        返回类型:  Python2 中 map 直接返回列表，Python3 中返回迭代器
        """
        even_num = list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6]))
        odd_num = list(filter(lambda x: x % 2, [1, 2, 3, 4, 5, 6]))
        print(even_num)
        print(odd_num)


if __name__ == "__main__":
    unittest.main(verbosity=2)
