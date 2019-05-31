#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-28 18:36
# @Author  : minp
# @contact : king101125s@gmail.com
# @Site    : 
# @File    : testing.py
# @Software: PyCharm

import unittest


class Test(unittest.TestCase):
    @unittest.skip('暂时跳过用例fun1的测试')
    def test_fun1(self):
        print('out')
        # TODO add something

    # @unittest.skip('暂时跳过用例fun2的测试')
    def test_fun2(self):
        print('out')
        # TODO add something


if __name__ == "__main__":
    unittest.main(verbosity=2)