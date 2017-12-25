#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    python_pattern.examples.adapter
    ~~~~~~~~~~~

    解释器模式

    给定一个语言，定义它的文法的一种表示，并定义一个解释 ，这个解释器使用该表示来解释语言中的句子。

    :copyright: (c) 2017 by the yinyi.
    :license: BSD, see LICENSE for more details.
"""
from pyparsing import Word, OneOrMore, Optional, Group, Suppress, alphanums

class Gate:
    def __init__(self):
        self.is_open = False

    def __str__(self):
        return 'open' if self.is_open else 'closed'

    def open(self):
        print('opening the gate')
        self.is_open = True

    def close(self):
        print('closing the gate')
        self.is_open = False


def main():
    # 首先定义我们的DSL格式，我们这里最简单的控制语法就是   "open -> gate"
    word = Word(alphanums)
    command = Group(OneOrMore(word))
    token = Suppress("->")
    device = Group(OneOrMore(word))
    argument = Group(OneOrMore(word))
    event = command + token + device + Optional(token + argument)

    gate = Gate()
    cmds = ['open -> gate', 'close -> gate']    # 两个自定义的命令
    open_actions = {'gate': gate.open}
    close_actions = {'gate': gate.close}

    for cmd in cmds:
        print(event.parseString(cmd))    # [['open'], ['gate']]
        cmd, dev = event.parseString(cmd)
        cmd_str, dev_str = ' '.join(cmd), ' '.join(dev)
        print(cmd_str, dev_str)
        if 'open' in cmd_str:
            open_actions[dev_str]()
        elif 'close' in cmd_str:
            close_actions[dev_str]()

if __name__ == "__main__":
    main()