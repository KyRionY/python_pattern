#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    python_pattern.examples.adapter
    ~~~~~~~~~~~

    装饰器模式

    动态地给一个对象添加一些额外的职责。就增加功能来说， Decorator模式相比于成子类更为为灵活。

    :copyright: (c) 2017 by the yinyi.
    :license: BSD, see LICENSE for more details.
"""
from functools import wraps

def memoize(fn):
    known = dict()

    @wraps(fn)
    def memoizer(*args):
        if args not in known:
            known[args] = fn(*args)
        return known[args]
    return memoizer


@memoize
def fibonacci(n):
    assert(n >= 0), 'n must be >= 0'
    return n if n in (0, 1) else fibonacci(n-1) + fibonacci(n-2)

def roles_required(*roles):
    """Decorator which specifies that a user must have all the specified roles.
    Example::

        @app.route('/dashboard')
        @roles_required('admin', 'editor')
        def dashboard():
            return 'Dashboard'

    The current user must have both the `admin` role and `editor` role in order
    to view the page.

    :param args: The required roles.
    """
    def wrapper(func):
        @wraps(func)
        def decorated_view(*args, **kwargs):
            if args not in roles:
                return None
            return func(*args, **kwargs)
        return decorated_view
    return wrapper

@roles_required('admin')
def admin_required_method(role):
    print(role)
