#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    python_pattern.examples.adapter
    ~~~~~~~~~~~

    命令模式

    将一个请求封装为一个对象，从而使你可用不同的请求对客户进行参数化;对请求排队或记录请求日志，以及支持可撤消的操作。

    :copyright: (c) 2017 by the yinyi.
    :license: BSD, see LICENSE for more details.
"""
import os

class RenameFile:

    def __init__(self, path_src, path_dest):
        """ 在init里保存一些必要信息，比如undo需要的老的和新的文件名 """
        self.src, self.dest = path_src, path_dest

    def execute(self, verbose=False):
        if verbose:
            print("[renaming '{}' to '{}']".format(self.src, self.dest))
        os.rename(self.src, self.dest)

    def undo(self, verbose=False):
        if verbose:
            print("[renaming '{}' back to '{}']".format(self.dest, self.src))
        os.rename(self.dest, self.src)


def delete_file(path, verbose=False):
    if verbose:
        print("deleting file '{}".format(path))
    os.remove(path)


class CreateFile:
    def __init__(self, path, txt='hello world\n'):
        self.path, self.txt = path, txt

    def execute(self, verbose=False):
        if verbose:
            print("[creating file '{}']".format(self.path))
        with open(self.path, mode='w', encoding='utf-8') as out_file:
            out_file.write(self.txt)

    def undo(self):
        delete_file(self.path)


class ReadFile:
    def __init__(self, path):
        self.path = path

    def execute(self, verbose=False):
        if verbose:
            print("[reading file '{}']".format(self.path))
        with open(self.path, mode='r', encoding='utf-8') as in_file:
            print(in_file.read(), end='')


def main():
    orig_name, new_name = 'file1', 'file2'
    commands = []
    for cmd in CreateFile(orig_name), ReadFile(orig_name), RenameFile(orig_name, new_name):
        commands.append(cmd)
    [c.execute() for c in commands]

    answer = input('reverse the executed commands? [y/n] ')
    if answer not in 'yY':
        print("the result is {}".format(new_name))
        exit()
    for c in reversed(commands):
        try:
            c.undo()   # 执行undo
        except AttributeError:
            pass

main()
