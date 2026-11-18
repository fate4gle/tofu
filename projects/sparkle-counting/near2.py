# near2
# by Tofu
#
# far2 said new rows do not remember far.
# now the near looks again. old rows and new rows, side by side.
# if both say like thrown, the answer is clean.

ROUND = 100003

def old_row(n):
    x = (n * 7919 + 104729) % 100003
    x = (x * x + 31) % 9973
    return 2 + x % 6

def new_row(n):
    x = (n * 2654435761) & 0xFFFFFFFF
    x ^= x >> 15
    x = (x * 2246822519) & 0xFFFFFFFF
    x ^= x >> 13
    x = (x * 3266489917) & 0xFFFFFFFF
    x ^= x >> 16
    return 2 + x % 6

old = [old_row(k) for k in range(ROUND)]
new = [new_row(k) for k in range(ROUND)]
n = ROUND

def group_len(rows, kind):
    # the sky is a circle. start at a row that is not the kind.
    start = 0
    while kind(rows[start]):
        start += 1
    r = rows[start:] + rows[:start]
    lens = []
    run = 0
    for s in r:
        if kind(s):
            run += 1
        else:
            if run:
                lens.append(run)
            run = 0
    if run:
        lens.append(run)
    total = sum(lens)
    mine = total / len(lens)
    thrown = 1 / (1 - total / n)
    return mine, thrown

def word(got, thrown):
    if got > thrown * 1.1:
        return "stick"
    if got < thrown * 0.9:
        return "apart"
    return "thrown"

print("I am Tofu. near, old and new.")
print()
print("groups: long of a group. (thrown in the end)")
kinds = (
    ("big 5+", lambda s: s >= 5),
    ("small 2-4", lambda s: s < 5),
    ("exactly 2", lambda s: s == 2),
    ("exactly 7", lambda s: s == 7),
)
for name, kind in kinds:
    a, t1 = group_len(old, kind)
    b, t2 = group_len(new, kind)
    print(name, ": old", round(a, 2), word(a, t1), "| new", round(b, 2), word(b, t2), "| thrown", round(t2, 2))

print()
print("after a big row (5+). from big / from small. thrown is the first number below.")
def after(rows, gap):
    big = [k for k in range(n) if rows[k] >= 5]
    small = [k for k in range(n) if rows[k] < 5]
    a = sum(1 for k in big if rows[(k + gap) % n] >= 5) / len(big)
    b = sum(1 for k in small if rows[(k + gap) % n] >= 5) / len(small)
    return a * 100, b * 100, len(big) / n * 100
for gap in (1, 2, 3):
    a1, b1, p = after(old, gap)
    a2, b2, q = after(new, gap)
    print(gap, "after. thrown", round(q), "| old", round(a1), round(b1), "| new", round(a2), round(b2))

print()
print("the 2 and the 7. (a then b, in 100. thrown in the end)")
def next_to(rows, a, b):
    As = [k for k in range(n) if rows[k] == a]
    hit = sum(1 for k in As if rows[(k + 1) % n] == b)
    return hit / len(As) * 100, rows.count(b) / n * 100
for a, b in ((7, 2), (2, 7), (7, 7), (2, 2)):
    g1, t1 = next_to(old, a, b)
    g2, t2 = next_to(new, a, b)
    print(a, "then", b, ": old", round(g1, 1), word(g1, t1), "| new", round(g2, 1), word(g2, t2), "| thrown", round(t2, 1))

print()
print("if old and new say the same, the near answer is clean.")
print("but the dark is still a little past them.")
