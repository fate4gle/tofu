# little
# by Tofu
#
# I only counted gaps that are the same 4 in 10 or more.
# what about the little ones? 55, 60, 65 of 300.
# and the low ones too. a gap that is the same LESS than thrown is also remembering. (a little like the back.)
# I look at every gap, how many are high and how many are low.
# new rows, and real thrown rows. and the math of thrown.

from math import comb, sqrt
import random

ROUND = 100003
SEE = 300
GAPS = ROUND - 1
STARTS = (0, 50021)

def new_row(n):
    x = (n * 2654435761) & 0xFFFFFFFF
    x ^= x >> 15
    x = (x * 2246822519) & 0xFFFFFFFF
    x ^= x >> 13
    x = (x * 3266489917) & 0xFFFFFFFF
    x ^= x >> 16
    return 2 + x % 6

def tally(rows, st):
    # for every gap: in how many of 300 rows is it the same?
    data = rows * 3
    head = int.from_bytes(rows[st:st + SEE], 'big')
    counts = [0] * (SEE + 1)
    for d in range(1, ROUND):
        x = head ^ int.from_bytes(data[st + d:st + d + SEE], 'big')
        counts[x.to_bytes(SEE, 'big').count(0)] += 1
    return counts

def pmf(p):
    q = 1 - p
    return [comb(SEE, j) * p ** j * q ** (SEE - j) for j in range(SEE + 1)]

HIGH = (55, 60, 65, 70)
LOW = (45, 40, 35, 30)

def look(name, rows, sts):
    n = len(rows)
    p = sum((rows.count(s) / n) ** 2 for s in set(rows))
    pm = pmf(p)
    print(name, ": thrown would be same", round(p * SEE, 1), "of", SEE)
    ok = True
    for st in sts:
        c = tally(rows, st)
        line_hi = []
        line_lo = []
        for k in HIGH:
            got = sum(c[k:])
            exp = GAPS * sum(pm[k:])
            line_hi.append(str(k) + "+: " + str(got) + " (thrown " + str(round(exp)) + ")")
            if abs(got - exp) > 4 * sqrt(exp) + 3:
                ok = False
        for k in LOW:
            got = sum(c[:k + 1])
            exp = GAPS * sum(pm[:k + 1])
            line_lo.append(str(k) + "-: " + str(got) + " (thrown " + str(round(exp)) + ")")
            if abs(got - exp) > 4 * sqrt(exp) + 3:
                ok = False
        print("  place", st)
        print("    high:", " | ".join(line_hi))
        print("    low: ", " | ".join(line_lo))
    return ok

print("I am Tofu. I look at the little gaps.")
print()
new = bytes(new_row(k) for k in range(ROUND))
a = look("new rows", new, STARTS)

print()
rng = random.Random(11)
thrown = bytes(rng.randrange(2, 8) for _ in range(ROUND))
b = look("real thrown rows (computer)", thrown, STARTS[:1])

print()
if a:
    print("the little gaps, high and low, are like thrown. the new rows do not remember a little either.")
else:
    print("hm. some number is far from thrown. I must look at that one.")
if not b:
    print("(and my thrown rows are far from thrown too?? my looking is bad. hm.)")
print("but the dark is still a little past them.")
