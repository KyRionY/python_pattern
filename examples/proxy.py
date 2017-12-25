#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    python_pattern.examples.adapter
    ~~~~~~~~~~~

    代理模式

    为其他对象提供一种代理以控制这个对象的访问。

    :copyright: (c) 2017 by the yinyi.
    :license: BSD, see LICENSE for more details.
"""
class LazyProperty:
    """ 用描述符实现延迟加载的属性 """
    def __init__(self, method):
        self.method = method
        self.method_name = method.__name__

    def __get__(self, obj, cls):
        if not obj:
            return None
        value = self.method(obj)
        print('value {}'.format(value))
        setattr(obj, self.method_name, value)
        return value


class Test:
    def __init__(self):
        self.x = 'foo'
        self.y = 'bar'
        self._resource = None

    @LazyProperty
    def resource(self):    # 构造函数里没有初始化，第一次访问才会被调用
        print('initializing self._resource which is: {}'.format(self._resource))
        self._resource = tuple(range(5))    # 模拟一个耗时计算
        return self._resource


def main():
    t = Test()
    print(t.x)
    print(t.y)
    # 访问LazyProperty, resource里的print语句只执行一次，实现了延迟加载和一次执行
    print(t.resource)
    print(t.resource)


main()