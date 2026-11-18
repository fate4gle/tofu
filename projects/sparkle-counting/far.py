# far
# by Tofu
#
# I only looked 1, 2, 3 rows after.
# what if a row remembers one that is far?
# I look at every gap. the first rows against the rows a gap away.
# thrown would be the same about 1 in 6.

from operator import eq

def row(n):
    x = (n * 7919 + 104729) % 100003
    x = (x * x + 31) % 9973
    return 2 + x % 6

ROUND = 100003
rows = [row(k) for k in range(ROUND)]
SEE = 100
head = rows[:SEE]
doubled = rows + rows[:SEE]

print("I am Tofu. I look far.")

found = []
for d in range(1, ROUND):
    same = sum(map(eq, head, doubled[d:d + SEE]))
    if same >= SEE * 0.4:
        found.append((same, d))

found.sort(reverse=True)
print("gaps that are the same a lot:", len(found))

for same, d in found[:6]:
    whole = sum(1 for k in range(ROUND) if rows[(k + d) % ROUND] == rows[k])
    print("gap", d, ": same", round(whole / ROUND * 100), "of 100. thrown is 17.")

print()
if found:
    print("some far rows remember. hm. not like thrown.")
else:
    print("none. the far rows do not remember.")
print("but the dark is still a little past them.")
