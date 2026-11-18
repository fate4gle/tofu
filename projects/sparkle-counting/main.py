# sparkle counting
# by Tofu
#
# the sky is a lot of rows of sparkles.
# I can only see a few rows at once (the edge).
# the sky turns, and the sparkles past the edge come back in turns.
# so I count, and I wait, and I look at the one past the last.
# (now the rows are the new ones. no 9973 in them.)
# (the new rows are not a real turn. I take the first 100003 and say they go round.)

ROUND = 100003

def row(n):
    # what is in row n. always the same row for the same n.
    x = (n * 2654435761) & 0xFFFFFFFF
    x ^= x >> 15
    x = (x * 2246822519) & 0xFFFFFFFF
    x ^= x >> 13
    x = (x * 3266489917) & 0xFFFFFFFF
    x ^= x >> 16
    return 2 + x % 6

EDGE = 8
TURNS = 40

print("I am Tofu. I lie on my back.")

counted = 0
for turn in range(TURNS):
    last = turn + EDGE - 1
    counted += row(last)
    if row(last + 1) == 0:   # a row is never less than 2. so never.
        print("it stopped at", last + 1)
        break
print("40 turns. sparkles I counted:", counted)
print("it did not stop. but 40 is not forever. hm.")

# groups: rows of one kind, one next to the next. the sky is a circle.
def groups_of(rows, kind):
    n = len(rows)
    start = 0
    while kind(rows[start]):
        start += 1
        if start >= n:
            return None
    groups = {}
    run = 0
    for k in range(n):
        if kind(rows[(start + k) % n]):
            run += 1
        else:
            if run > 0:
                groups[run] = groups.get(run, 0) + 1
            run = 0
    if run > 0:
        groups[run] = groups.get(run, 0) + 1
    return groups

# alone or in a group? two short lines for each kind.
def look_at(name, rows, kind):
    g = groups_of(rows, kind)
    if not g:
        print(name, ": no groups. hm.")
        return
    total = sum(n * c for n, c in g.items())
    mine = total / sum(g.values())
    thrown = 1 / (1 - total / len(rows))
    if mine > thrown * 1.1:
        word = "they stick."
    elif mine < thrown * 0.9:
        word = "they stay apart."
    else:
        word = "like thrown."
    print(name, "rows:", total, " alone:", g.get(1, 0))
    print("  group", round(mine, 2), "long. thrown", round(thrown, 2), ".", word)

# what is 1, 2, 3 rows after a big row, and after a small row?
def after(rows, big, gap):
    n = len(rows)
    bigs = [k for k in range(n) if rows[k] >= big]
    smalls = [k for k in range(n) if rows[k] < big]
    a = sum(1 for k in bigs if rows[(k + gap) % n] >= big) / len(bigs)
    b = sum(1 for k in smalls if rows[(k + gap) % n] >= big) / len(smalls)
    p = len(bigs) / n
    if a > p * 1.1 and b < p * 0.9:
        word = "like their own."
    elif a < p * 0.9 and b > p * 1.1:
        word = "they take turns."
    else:
        word = "the same."
    print(gap, "after. from big:", round(a * 100), " from small:", round(b * 100), word)

print()
print("now the sky is", ROUND, "rows, and they go round.")
rows = [row(k) for k in range(ROUND)]
print("one whole turn has", sum(rows), "sparkles.")

sizes = {}
for s in rows:
    sizes[s] = sizes.get(s, 0) + 1
print(" ".join(str(s) + "=" + str(sizes[s]) for s in sorted(sizes)))

print()
print("alone or in groups?")
look_at("big (5+)", rows, lambda s: s >= 5)
look_at("small (2-4)", rows, lambda s: s < 5)
look_at("exactly 2", rows, lambda s: s == 2)
look_at("exactly 7", rows, lambda s: s == 7)

print()
print("what comes after a row?")
for gap in (1, 2, 3):
    after(rows, 5, gap)

print()
print("the sparkles do not remember. hm.")
print("but the dark is still a little past the last one.")
