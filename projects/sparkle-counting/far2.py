# far2
# by Tofu
#
# why.py said the far rows remember because of my 9973.
# so: rows made another way. do they remember far too?
# I look at the old rows and the new rows. the same look.

from operator import eq

ROUND = 100003
SEE = 100

def old_row(n):
    x = (n * 7919 + 104729) % 100003
    x = (x * x + 31) % 9973
    return 2 + x % 6

def new_row(n):
    # mixed up more. no little number to cut with.
    x = (n * 2654435761) & 0xFFFFFFFF
    x ^= x >> 15
    x = (x * 2246822519) & 0xFFFFFFFF
    x ^= x >> 13
    x = (x * 3266489917) & 0xFFFFFFFF
    x ^= x >> 16
    return 2 + x % 6

def thrown_of(rows):
    n = len(rows)
    return sum((rows.count(s) / n) ** 2 for s in set(rows))

def look(name, make):
    rows = [make(k) for k in range(ROUND)]
    head = rows[:SEE]
    doubled = rows + rows[:SEE]
    thrown = thrown_of(rows)
    best = (0, 0)
    many = 0
    for d in range(1, ROUND):
        same = sum(map(eq, head, doubled[d:d + SEE]))
        if same >= SEE * 0.4:
            many += 1
        if same > best[0]:
            best = (same, d)
    print(name, ": gaps same a lot:", many)
    d = best[1]
    whole = sum(1 for k in range(ROUND) if rows[(k + d) % ROUND] == rows[k])
    print("  best gap", d, ": same", round(whole / ROUND * 100), "of 100. thrown is", round(thrown * 100), ".")
    return many

print("I am Tofu. old rows and new rows, far.")
a = look("old", old_row)
b = look("new", new_row)

print()
if a > 0 and b == 0:
    print("old rows remember far. new rows do not.")
    print("so it was my 9973. the sparkles do not remember far.")
elif b > 0:
    print("hm. the new rows remember too. I do not know why yet.")
else:
    print("hm. none for both.")
print("but the dark is still a little past them.")
