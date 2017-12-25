#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    python_pattern.examples.singleton
    ~~~~~~~~~~~

    单例模式

    保证一个类仅有一个实 ，并提供一个访问它的全局访问点。

    :copyright: (c) 2017 by the yinyi.
    :license: BSD, see LICENSE for more details.
"""
# http://stackoverflow.com/questions/6760685/creating-a-singleton-in-python
class BaseClass:
    pass


# 装饰器实现
def singleton(class_):
    instances = {}
    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance


@singleton
class MyClass(BaseClass):
    pass


class Singleton(object):
    _instance = None
    def __new__(class_, *args, **kwargs):
        if not isinstance(class_._instance, class_):
            class_._instance = object.__new__(class_, *args, **kwargs)
        return class_._instance


class MyClass(Singleton, BaseClass):
    pass


# 元类实现
class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


# Python2
class MyClass(BaseClass):
    __metaclass__ = Singleton

# Python3
class MyClass(BaseClass, metaclass=Singleton):
    pass