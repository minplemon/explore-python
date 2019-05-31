#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-28 18:34
# @Author  : minp
# @contact : king101125s@gmail.com
# @Site    :
# @File    : func_parameter.py
# @Software: PyCharm

import unittest


def param_must(x, y):
    """
    必填参数
    :param x: 必填
    :param y: 必填
    :return: x+y
    """
    print(x + y)
    return x + y


def param_default(x, y, z=1):
    """
    默认参数
    :param x: 必填
    :param y: 必填
    :param z: 1.默认参数，非必填，没有传递该参数，则自动使用默认值，否则使用传递时该参数的值
              2.默认参数要放在所有必选参数的后面 如: add(x=1, y, z) add(x, y=1, z)
              3.默认参数应该使用不可变对象  如: add_to_list(L=[])
    :return: x+y+z
    """
    print(x + y + z)


def param_change(*numbers):
    """
    可变参数
    :param numbers: 传递 * 表示任意参数
    :return: 返回tuple类型
    """
    sum = 0
    for i in numbers:
        sum += i
    print('numbers:', numbers)
    print('sum:', sum)


def param_function(x, y, z):
    """
    可变参数|关键字参数 使用方法
    * 表示任意参数，它的另外一个用法是，给函数传递参数
    :param1 (x, y, z): 比如 (4, 5, 6)
    :param2 [x, y, z]: 比如 [1, 2, 3]
    :param3 {x = 1, y = 2, z = 3}: 比如 {x = 1, y = 2, z = 3}
    :return: x+y+z
    """
    print(x + y + z)
    return x + y + z


def param_kwparam(**kwargs):
    """
    关键字参数
    :param kwargs: 不定长度的键值对, 作为参数传递
    :return: 返回dict kw类型
    """
    print(kwargs)


def func_call(x, y, z=0, *args, **kwargs):
    """
    参数组合
    有顺序的，依次是必选参数、默认参数、可变参数和关键字参数
    :param x: 必填
    :param y: 必填
    :param z: 默认参数，非必填
    :param args: 可变参数
    :param kwargs: 关键字参数
    :return:
    """
    print('x =', x)
    print('y =', y)
    print('z =', z)
    print('args =', args)
    print('kwargs =', kwargs)


class Test(unittest.TestCase):
    @unittest.skip('测试test_param_must')
    def test_param_must(self):
        print(param_must.__doc__)
        param_must(1, 2)    # 数量一致，通过
        param_must()        # 啥都没传，不行
        param_must(1)       # 只传了一个，也不行

    @unittest.skip('测试param_default')
    def test_param_default(self):
        print(param_default.__doc__)
        param_default(1, 2, 3)      # 1+2+3
        param_default(1, 2)         # 没有传递 z，自动使用 z=1，即 1+2+1

    @unittest.skip('测试param_change')
    def test_param_change(self):
        print(param_change.__doc__)
        param_change()          # 传递 0 个参数
        param_change(1)         # 传递 1 个参数
        param_change(1, 2)      # 传递 2 个参数
        param_change(1, 2, 3)   # 传递 3 个参数
        a = [1, 2, 3]
        b = (4, 5, 6)
        param_change(*a)
        param_change(*b)

    @unittest.skip('测试param_function')
    def test_param_function(self):
        print(param_function.__doc__)
        a = [1, 2, 3]
        b = (4, 5, 6)
        dict1 = {'z': 3, 'x': 1, 'y': 6}
        param_function(*a)          # 使用 *a 来参数
        param_function(*b)          # 使用 *b 来参数
        param_function(**dict1)     # **dict1 来传参

    @unittest.skip('测试param_kwparam')
    def test_param_kwparam(self):
        print(param_kwparam.__doc__)
        param_kwparam()             # 没有参数，kwargs 为空字典
        param_kwparam(x=1)          # x=1 => kwargs={'x': 1}
        param_kwparam(x=1, y=2)     # x=1, y=2 => kwargs={'y': 2, 'x': 1}

    @unittest.skip('测试func_call')
    def test_func_call(self):
        print(func_call.__doc__)
        a = (1, 2, 3)
        b = {'u': 6, 'v': 7}
        func_call(1, 2)                     # 至少提供两个参数，因为 x, y
        func_call(1, 2, 3)                  # x=1, y=2, z=3
        func_call(1, 2, 3, 4, 5, 6)         # x=1, y=2, z=3, args=(4, 5, 6), kwargs={}
        func_call(1, 2, 4, u=6, v=7)        # args = (), kwargs = {'u': 6, 'v': 7}
        func_call(1, 2, 3, 4, 5, u=6, v=7)  # args = (4, 5), kwargs = {'u': 6, 'v': 7}
        func_call(*a, **b)

    @unittest.skip('测试param_default')
    def test_fun2(self):
        print(func_call.__doc__)


if __name__ == "__main__":
    unittest.main(verbosity=2)
