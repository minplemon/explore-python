#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-29 14:03
# @Author  : minp
# @contact : king101125s@gmail.com
# @Site    :
# @File    : decorator.py
# @Software: PyCharm

import unittest


def makeitalic(func):
    def wrapped():
        return '<i>' + func() + '</i>'
    return wrapped

@makeitalic
def hello():
    return 'hello world'



def multiply(x, y):
    return x * y

multiply(3, y=2)

hello = makeitalic(hello)  # 返回一个函数，将其赋给 hello
print(hello())


# class Test(unittest.TestCase):
#     @unittest.skip('测试decorator')
#     def test_decorator(self):
#         print('out')
#
#
#
#     # @unittest.skip('暂时跳过用例fun2的测试')
#     def test_fun2(self):
#         print('out')
#         # TODO add something
#
#
# if __name__ == "__main__":
#     unittest.main(verbosity=2)
