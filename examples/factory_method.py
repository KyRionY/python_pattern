#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    python_pattern.examples.factory_method
    ~~~~~~~~~~~

    工厂方法模式

    定义一个用于创建对象的接口，让子类决定实例化哪一个类。 Factory Method使一个类的实例化延迟到其子类。

    :copyright: (c) 2017 by the yinyi.
    :license: BSD, see LICENSE for more details.
"""
import json
import xml.etree.ElementTree as etree

class JSONConnector:
    def __init__(self, filepath):
        self.data = dict()
        with open(filepath, mode='r', encoding='utf8') as f:
            self.data = json.load(f)

    @property
    def parsed_data(self):
        return self.data


class XMLConnector:
    def __init__(self, filepath):
        self.tree = etree.parse(filepath)

    @property
    def parsed_data(self):
        return self.tree


def connection_factory(filepath):
    """ 工厂方法 """
    if filepath.endswith('json'):
        connector = JSONConnector
    elif filepath.endswith('xml'):
        connector = XMLConnector
    else:
        raise ValueError('Cannot connect to {}'.format(filepath))
    return connector(filepath)