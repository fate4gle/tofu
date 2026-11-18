# stone
# by Tofu
#
# not for the sparkles. for the warm stone at the stump.
# I lie on the stone with my back. then I write one line in stone_days.csv.
# yes or no or some, in each place. this file only counts what I wrote.
# one day is not every day. so it does not say anything before 3 days.
# if I write a word that is not yes, some or no, it tells me. so a typo does not hide.
# with 0 days it says it one time, not two.
# if I write the same day two times, it counts one day and tells me.
# if I write a line but forget the day word, it tells me.
#      (a line with nothing in it at all is just an empty line. that one is fine.)
# new: the counting is now report(lines), so stone_test.py can give it TEST lines.
#      running this file does the same as before. it reads stone_days.csv.

import csv

NEED = 3
FIELDS = (
    ("warm_first", "warm when I first came"),
    ("warm_after_sun", "still warm when the sun went"),
    ("back_fits", "my back fits"),
    ("glitter", "it glitters"),
)
KNOWN = ("yes", "some", "no")


def report(f):
    # f: an open file, or a list of lines. the first line is the names.
    rows = []
    noday = 0
    for r in csv.DictReader(f):
        if (r.get("day") or "").strip():
            rows.append(r)
            continue
        # no day word. is something else written on the line?
        vals = []
        for v in r.values():
            if isinstance(v, list):
                vals.extend(v)
            else:
                vals.append(v)
        if any((v or "").strip() for v in vals):
            noday += 1

    n = len(rows)

    # how many different days?
    seen = {}
    for r in rows:
        name = (r.get("day") or "").strip().lower()
        seen[name] = seen.get(name, 0) + 1
    days = len(seen)
    twice = [name for name, c in seen.items() if c > 1]

    print("lines I wrote:", n, "| different days:", days)
    if noday:
        print("hm.", noday, "line(s) have no day word. I did not count them. look at stone_days.csv.")
    if twice:
        print("hm. same day written more than once:", ", ".join(twice) + ". I count it one day. look at stone_days.csv.")

    if n == 0:
        print("nothing yet. I did not go to the stone yet. so nothing is known.")
        print("I go lie on the stone. then one line in stone_days.csv.")
        return

    odd = 0
    for key, words in FIELDS:
        vals = [(r.get(key) or "").strip().lower() for r in rows]
        yes = vals.count("yes")
        some = vals.count("some")
        no = vals.count("no")
        other = len(vals) - yes - some - no
        odd += other
        line = "yes " + str(yes) + " | some " + str(some) + " | no " + str(no) + " | of " + str(n)
        if other:
            line += " | not understood " + str(other)
        print(" ", words + ":", line)
    if odd:
        print("hm. I wrote", odd, "word(s) that are not yes, some or no. look at stone_days.csv.")

    print()
    if days < NEED:
        print("only", days, "different day(s). one day is not every day. I do not say yet.")
        print("I go lie on the stone. more days.")
    else:
        warm = [(r.get("warm_first") or "").strip().lower() for r in rows]
        after = [(r.get("warm_after_sun") or "").strip().lower() for r in rows]
        both = sum(1 for a, b in zip(warm, after) if a == "yes" and b == "yes")
        print("warm at first AND after the sun:", both, "of", n, "lines.")
        if both == n:
            print("every day it was warm, even after the sun. that is a stone that keeps warm.")
        elif both == 0:
            print("never warm both. maybe it is only warm when the sun is on it.")
        else:
            print("some days yes, some days no. I look more days.")
        print("is it the one I wished for? this file does not know. only my back knows.")


if __name__ == "__main__":
    print("I am Tofu. the warm stone. what did I write?")
    try:
        with open("stone_days.csv") as f:
            report(f)
    except OSError:
        print("I cannot find stone_days.csv. hm.")
        report([])
    print("the dark is still a little past the last one.")
