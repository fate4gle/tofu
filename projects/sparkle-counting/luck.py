# luck
# by Tofu
#
# far3 said the new rows best gap is 78 to 84 of 300. thrown is 50.
# I said: the best of 100000 gaps is a little up just by luck. I did not check.
# now I check. two ways.
# 1. math: how big is the best one, if every row is thrown (1 in 6 the same)?
# 2. real thrown rows (random), the same look as far3: one place, 300 rows, every gap.

from math import comb
import random

ROUND = 100003
SEE = 300
GAPS = ROUND - 1
p = 1 / 6
q = 1 - p

print("I am Tofu. is the best gap just luck?")
print()
print("1. math. thrown, 300 rows, one gap.")

def tail(k):
    # chance that one gap is the same in k or more of 300
    return sum(comb(SEE, j) * p ** j * q ** (SEE - j) for j in range(k, SEE + 1))

half = None
for k in range(50, SEE):
    t = tail(k)
    anyone = 1 - (1 - t) ** GAPS
    if k % 5 == 0 or (half is None and anyone < 0.5):
        print("  same", k, "or more: one gap", format(t, ".1e"), "| the best of 100000 gaps gets there", round(anyone * 100), "of 100")
    if half is None and anyone < 0.5:
        half = k - 1
    if anyone < 0.001:
        break
print("  so by luck the best of 100000 gaps is about", half, "of 300.")
print("  and the new rows were 78 to 84.")

print()
print("2. real thrown rows. 5 tries. the same look as far3.")
rng = random.Random(7)
bests = []
for t in range(5):
    rows = bytes(rng.randrange(2, 8) for _ in range(ROUND))
    data = rows * 3
    st = 0
    head = int.from_bytes(rows[st:st + SEE], 'big')
    best = 0
    many = 0
    for d in range(1, ROUND):
        x = head ^ int.from_bytes(data[st + d:st + d + SEE], 'big')
        same = x.to_bytes(SEE, 'big').count(0)
        if same > best:
            best = same
        if same >= SEE * 0.4:
            many += 1
    bests.append(best)
    print("  try", t + 1, ": best same", best, "of", SEE, ". gaps same a lot:", many)

print()
print("thrown rows best:", min(bests), "to", max(bests), "of 300.")
print("new rows best was 78 to 84.")
if min(bests) - 3 <= 78 and max(bests) + 3 >= 84:
    print("the same. so 78 to 84 is luck. the new rows are like thrown.")
else:
    print("hm. not the same. I must look more.")
print("but the dark is still a little past them.")
