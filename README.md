# lifepicker
A randomized activity picker for your 5 minites

## Usage

Add some 5-min activities:

```
$ python3 bin/lifepicker.py add read book A
$ python3 bin/lifepicker.py add watch coursera calculus course
```

Let the program choose your next activity:

```
$ python3 bin/lifepicker.py pick
read book A
do it for five minutes
```

And after five minutes, give a feedback:
```
g: it was good; b: it was bad> b
```

After you say it was good, the activity is more likely to be chosen.

## Note

The program uses `~/lifepicker.json` as storage.
