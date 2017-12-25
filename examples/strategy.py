#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    python_pattern.examples.adapter
    ~~~~~~~~~~~

    策略模式

    定义一系列的算法,把它们一个个封装起来, 并且使它们可相互替换。本模式使得算法可独立于使用它的客户而变化。

    :copyright: (c) 2017 by the yinyi.
    :license: BSD, see LICENSE for more details.
"""

def f1(seq):
    pass

def f2(seq):
    pass

def f(seq):
    threshold_value = 10
    if len(seq) >= threshold_value:    # 大于某个阈值
        f1(seq)    # 在数量较多时候具有良好的效率
    else:
        f2(seq)