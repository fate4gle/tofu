# pair
# by Tofu
#
# the blue star by the gold one.
# the 2 is the small one. the 7 is the big one.
# is a 2 next to a 7 more than if thrown?
#
# careful: this file uses the OLD rows (the 9973 ones).
# the old rows can look like remembering, only because of how I made them.
# near2.py looks at the 2 and the 7 for old rows AND new rows. the answer uses near2.py.
# I keep this file because it also shows what comes after a 7.

def row(n):
    x = (n * 7919 + 104729) % 100003
    x = (x * x + 31) % 9973
    return 2 + x % 6

ROUND = 100003
rows = [row(k) for k in range(ROUND)]
n = len(rows)

print("I am Tofu. the 2 and the 7. (old rows)")

def share(s):
    return rows.count(s) / n

def next_to(a, b):
    # a row of a. is the one right after it a b?
    As = [k for k in range(n) if rows[k] == a]
    hit = sum(1 for k in As if rows[(k + 1) % n] == b)
    return hit / len(As)

for a, b in ((7, 2), (2, 7), (7, 7), (2, 2)):
    got = next_to(a, b) * 100
    thrown = share(b) * 100
    if got > thrown * 1.1:
        word = "they like each other."
    elif got < thrown * 0.9:
        word = "they stay away."
    else:
        word = "like thrown."
    print(a, "then", b, ":", round(got, 1), " thrown:", round(thrown, 1), word)

print()
print("after a 7, what comes?")
Sevens = [k for k in range(n) if rows[k] == 7]
line = []
for s in range(2, 8):
    c = sum(1 for k in Sevens if rows[(k + 1) % n] == s)
    line.append(str(s) + "=" + str(round(c / len(Sevens) * 100)))
print(" ".join(line))

print()
print("the gold one does not look for the blue one. hm.")
print("(old rows. for old and new together: near2.py)")
print("but the dark is still a little past them.")
