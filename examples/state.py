#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    python_pattern.examples.adapter
    ~~~~~~~~~~~

    状态模式

    允许一个对象在其内部状态改变时改变它的行为。对象看起来似乎修改了它的类。

    :copyright: (c) 2017 by the yinyi.
    :license: BSD, see LICENSE for more details.
"""
# 先装下pip3 install state_machine
from state_machine import (
    acts_as_state_machine, State, Event, before, after, InvalidStateTransition
)


@acts_as_state_machine
class Process:
    # 先来定义状态机的状态 states
    created = State(initial=True)    # 初始状态
    waiting = State()
    running = State()
    terminated = State()
    blocked = State()
    swapped_out_waiting = State()
    swapped_out_blocked = State()

    # 再定义状态机的转移 transitions
    wait = Event(from_states=(created, running, blocked,
                            swapped_out_waiting), to_state=waiting)
    run = Event(from_states=waiting, to_state=running)
    terminate = Event(from_states=running, to_state=terminated)
    block = Event(from_states=(running, swapped_out_blocked),
                to_state=blocked)
    swap_wait = Event(from_states=waiting, to_state=swapped_out_waiting)
    swap_block = Event(from_states=blocked, to_state=swapped_out_blocked)

    def __init__(self, name):
        self.name = name

    # The state_machine module provides us with the @before and @after
    # decorators that can be used to execute actions before or after a
    # transition occurs, respectfully.
    @after('wait')
    def wait_info(self):
        print('{} entered waiting mode'.format(self.name))

    @after('run')
    def run_info(self):
        print('{} is running'.format(self.name))

    @before('terminate')
    def terminate_info(self):
        print('{} terminated'.format(self.name))

    @after('block')
    def block_info(self):
        print('{} is blocked'.format(self.name))

    @after('swap_wait')
    def swap_wait_info(self):
        print('{} is swapped out and waiting'.format(self.name))

    @after('swap_block')
    def swap_block_info(self):
        print('{} is swapped out and blocked'.format(self.name))


def transition(process, event, event_name):
    """
    Args:
        process (Process obj):
        event (Event obj): wait, run, terminate...
        event_name (str): name of event
    """
    try:
        event()
    except InvalidStateTransition:
        print('Error: transition of {} from {} to {} failed'.format(
            process.name, process.current_state, event_name))


def state_info(process):
    """ 当前状态机的状态 """
    print('state of {}: {}'.format(process.name, process.current_state))

if __name__ == "__main__":
    RUNNING = 'running'
    WAITING = 'waiting'
    BLOCKED = 'blocked'
    TERMINATED = 'terminated'
    p1, p2 = Process('process1'), Process('process2')
    [state_info(p) for p in (p1, p2)]

    print()
    transition(p1, p1.wait, WAITING)
    transition(p2, p2.terminate, TERMINATED)
    [state_info(p) for p in (p1, p2)]
    print()
    transition(p1, p1.run, RUNNING)
    transition(p2, p2.wait, WAITING)
    [state_info(p) for p in (p1, p2)]
    print()
    transition(p2, p2.run, RUNNING)
    [state_info(p) for p in (p1, p2)]
    print()
    [transition(p, p.block, BLOCKED) for p in (p1, p2)]
    [state_info(p) for p in (p1, p2)]
    print()
    [transition(p, p.terminate, TERMINATED) for p in (p1, p2)]
    [state_info(p) for p in (p1, p2)]