""" lifepicker.py

Usage:
    ./lifepicker.py [command] ...

Commands
    add [activity]
        Adds the activity in the pool.
    pick
        The command picks an activity from the pool,
        The user can then start, skip or remove the activity.
        If the user starts the activity, after 5 minutes, the command asks
        the user whether the activity was good or bad.
"""

import argparse

def add():
    print('add')
    raise NotImplementedError

def pick():
    print('pick')
    raise NotImplementedError

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()

add_parser = subparsers.add_parser('add')
add_parser.set_defaults(func=add)
pick_parser = subparsers.add_parser('pick')
pick_parser.set_defaults(func=pick)

if __name__ == '__main__':
    args = parser.parse_args()
    try:
        args.func()
    except AttributeError:
        # When neither 'add' or 'pick' is specified, execute 'pick'
        pick()
