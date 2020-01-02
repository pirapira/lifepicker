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

import argparse, json
from pathlib import Path

def add_element(original_list, activity):
    return original_list + [{ "name": activity, "good": 0, "bad": 0 }]

def add(args):
    print('add')
    new_activity = ' '.join(args.activity)
    with open(storage, encoding='utf-8') as json_file:
        current_list = json.load(json_file)
    with open(storage, 'w', encoding='utf-8') as json_file:
        new_list = add_element(current_list, new_activity)
        json.dump(new_list, json_file)

storage = Path.home() / Path('lifepicker.json')

def pick_param(activity):
    from scipy.stats import beta
    return beta.rvs(activity["good"] + 1, activity["bad"] + 1)

def pick_activity(activities):
    params = map(pick_param, activities)
    pairs = list(zip(params, activities))
    pairs.sort(key=lambda pair: pair[0])
    return pairs[-1][1]["name"]

def pick(args):
    print('pick')
    with open(storage, encoding='utf-8') as json_file:
        activities = json.load(json_file)
    activity = pick_activity(activities)
    print(activity)
    print('do it for five minutes')
    from time import sleep
    sleep(300)
    good_or_bad = input('g: it was good; b: it was bad> ')
    if good_or_bad == 'g':
        record("good", activity)
    elif good_or_bad == 'b':
        record("bad", activity)

def record(label, activity):
    with open(storage, encoding='utf-8') as json_file:
        activities = json.load(json_file)
    for entry in activities:
        if(entry["name"] == activity):
            entry[label] += 1
            with open(storage, 'w', encoding='utf-8') as json_file:
                json.dump(activities, json_file)
            return
    raise RuntimeError("activity not found")

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()

add_parser = subparsers.add_parser('add')
add_parser.set_defaults(func=add)
add_parser.add_argument('activity', nargs='+')
pick_parser = subparsers.add_parser('pick')
pick_parser.set_defaults(func=pick)

if __name__ == '__main__':
    args = parser.parse_args()
    try:
        args.func(args)
    except AttributeError:
        # When neither 'add' or 'pick' is specified, execute 'pick'
        pick(args)
