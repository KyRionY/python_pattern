#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    python_pattern.examples.adapter
    ~~~~~~~~~~~

    原型模式

    原型实例指定创建对象的种类，并且通过拷贝这些原型创建新的对象。

    :copyright: (c) 2017 by the yinyi.
    :license: BSD, see LICENSE for more details.
"""
import copy
from collections import OrderedDict

class Book:
    def __init__(self, name, authors, price, **rest):
        '''Examples of rest: publisher, length, tags, publication
        date'''
        self.name = name
        self.authors = authors
        self.price = price      # in US dollars
        self.__dict__.update(rest)

    def __str__(self):
        mylist = []
        ordered = OrderedDict(sorted(self.__dict__.items()))
        for i in ordered.keys():
            mylist.append('{}: {}'.format(i, ordered[i]))
            if i == 'price':
                mylist.append('$')
            mylist.append('\n')
        return ''.join(mylist)


class Prototype:
    def __init__(self):
        self.objects = {}

    def register(self, identifier, obj):
        self.objects[identifier] = obj

    def unregister(self, identifier):
        del self.objects[identifier]

    def clone(self, identifier, **attr):
        """ 实现对象拷贝 """
        found = self.objects.get(identifier)
        if not found:
            raise ValueError('Incorrect object identifier: {}'.format(identifier))
        obj = copy.deepcopy(found)
        obj.__dict__.update(attr)    # 实现拷贝时自定义更新
        return obj


def main():
    b1 = Book('The C Programming Language', ('Brian W. Kernighan', 'Dennis M.Ritchie'),
            price=118, publisher='Prentice Hall', length=228, publication_date='1978-02-22',
            tags=('C', 'programming', 'algorithms', 'data structures'))

    prototype = Prototype()
    cid = 'k&r-first'
    prototype.register(cid, b1)
    b2 = prototype.clone(cid, name='The C Programming Language (ANSI)', price=48.99, length=274,
                        publication_date='1988-04-01', edition=2)
    for i in (b1, b2):
        print(i)
        print("ID b1 : {} != ID b2 : {}".format(id(b1), id(b2)))