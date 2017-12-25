#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    python_pattern.examples.adapter
    ~~~~~~~~~~~

    观察者模式

    定义对象间的一种一对多的依赖关系 ,当一个对象的状态发生改变时 , 所有依赖于它的对象都得到通知并被自动刷新。

    :copyright: (c) 2017 by the yinyi.
    :license: BSD, see LICENSE for more details.
"""
class Publisher:
    def __init__(self):
        self.observers = []

    def add(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)
        else:
            print('Failed to add : {}').format(observer)

    def remove(self, observer):
        try:
            self.observers.remove(observer)
        except ValueError:
            print('Failed to remove : {}').format(observer)

    def notify(self):
        [o.notify_by(self) for o in self.observers]


class DefaultFormatter(Publisher):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self._data = 0

    def __str__(self):
        return "{}: '{}' has data = {}".format(
            type(self).__name__, self.name, self._data)

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, new_value):
        try:
            self._data = int(new_value)
        except ValueError as e:
            print('Error: {}'.format(e))
        else:
            self.notify()    # data 在被合法赋值以后会执行notify


class HexFormatter:
    """ 订阅者 """
    def notify_by(self, publisher):
        print("{}: '{}' has now hex data = {}".format(
            type(self).__name__, publisher.name, hex(publisher.data)))


class BinaryFormatter:
    """ 订阅者 """
    def notify_by(self, publisher):
        print("{}: '{}' has now bin data = {}".format(
            type(self).__name__, publisher.name, bin(publisher.data)))


if __name__ == "__main__":
    df = DefaultFormatter('test1')
    print(df)
    print()
    hf = HexFormatter()
    df.add(hf)
    df.data = 3
    print(df)

    print()
    bf = BinaryFormatter()
    df.add(bf)
    df.data = 21
    print(df)