#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    python_pattern.examples.adapter
    ~~~~~~~~~~~

    适配器模式

    将一个类的接口转换成客户希望的另外一个接 。 Adapter模式使得原本由于接口不兼容而不能一起工作的那些类可以一起工作。

    :copyright: (c) 2017 by the yinyi.
    :license: BSD, see LICENSE for more details.
"""
class Computer:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'the {} computer'.format(self.name)

    def execute(self):
        """ call by client code """
        return 'execute a program'


class Synthesizer:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'the {} synthesizer'.format(self.name)

    def play(self):
        return 'is playing an electroinc song'


class Human:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'the {} human'.format(self.name)

    def speak(self):
        return 'says hello'


class Adapter:
    def __init__(self, obj, adapted_methods):
        """ 不使用继承，使用__dict__属性实现适配器模式 """
        self.obj = obj
        self.__dict__.update(adapted_methods)

    def __str__(self):
        return str(self.obj)


# 适配器使用示例
def main():
    objs = [Computer('Asus')]
    synth = Synthesizer('moog')
    objs.append(Adapter(synth, dict(execute=synth.play)))
    human = Human('Wnn')
    objs.append(Adapter(human, dict(execute=human.speak)))

    for o in objs:
        # 用统一的execute适配不同对象的方法，这样在无需修改源对象的情况下就实现了不同对象方法的适配
        print('{} {}'.format(str(o), o.execute()))


if __name__ == "__main__":
    main()