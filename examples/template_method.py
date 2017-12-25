#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    python_pattern.examples.adapter
    ~~~~~~~~~~~

    模版方法模式

    定义一个操作中的算法的骨架，而将一些步骤延迟到子类中。 TemplateMethod使得子类可以不改变一个算法的结构即可重定义该算法的某些特定步骤。

    :copyright: (c) 2017 by the yinyi.
    :license: BSD, see LICENSE for more details.
"""
from cowpy import cow


def dots_style(msg):
    msg = msg.capitalize()
    msg = '.' * 10 + msg + '.' * 10
    return msg


def admire_style(msg):
    msg = msg.upper()
    return '!'.join(msg)


def cow_style(msg):
    msg = cow.milk_random_cow(msg)
    return msg


def generate_banner(msg, style=dots_style):
    print('-- start of banner --')
    print(style(msg))
    print('-- end of banner --\n\n')


def main():
    msg = 'happy coding'
    [generate_banner(msg, style) for style in (dots_style, admire_style,
                                            cow_style)]

if __name__ == "__main__":
    main()


"""
-- start of banner --
..........Happy coding..........
-- end of banner --


-- start of banner --
H!A!P!P!Y! !C!O!D!I!N!G
-- end of banner --


-- start of banner --
______________
< happy coding >
--------------
    o
    o
    ^__^         /
    (**)\_______/  _________
    (__)\       )=(  ____|_ \_____
U    ||----w |  \ \     \_____ |
        ||     ||   ||           ||
-- end of banner --
"""
