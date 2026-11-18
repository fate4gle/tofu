# why
# by Tofu
#
# far.py said gap 11743 and gap 88260 are the same 92 of 100.
# 11743 + 88260 = 100003. one is the back of the other.
# 23486 is 2 of 11743. 35229 is 3 of 11743.
# I think it is a trick in how I make a row. I look.

ROUND = 100003

def first(n):
    return (n * 7919 + 104729) % 100003

def row(n):
    x = first(n)
    x = (x * x + 31) % 9973
    return 2 + x % 6

m = 11743
step = (7919 * m) % ROUND
print("I am Tofu. why do far rows remember.")
print("gap", m, "moves the first number by", step, "which is", step - ROUND, "round the circle.")
print("and I cut with 9973. is that 9973?", ROUND - step == 9973)

wrap = 0
differ = 0
differ_not_wrap = 0
wrap_same = 0
for k in range(ROUND):
    x = first(k)
    w = x < 9973   # taking 9973 away goes under 0 and comes round
    d = row(k) != row(k + m)
    if w:
        wrap += 1
        if not d:
            wrap_same += 1
    if d:
        differ += 1
        if not w:
            differ_not_wrap += 1

print("rows that come round (under 0):", wrap, "of", ROUND)
print("rows that are not the same:", differ)
print("not the same but did not come round:", differ_not_wrap)
print("came round and still the same (luck):", wrap_same)

print()
print("and the 2, 3, 4, 5 of that gap?")
for j in range(1, 6):
    d = (j * m) % ROUND
    same = sum(1 for k in range(ROUND) if row((k + d) % ROUND) == row(k))
    print(j, "of the gap =", d, ": same", round(same / ROUND * 100), "of 100")

print()
if differ_not_wrap == 0:
    print("so only the ones that come round are not the same.")
    print("it is my 9973. not the sparkles.")
else:
    print("hm. some not the same and not round. not only 9973.")
print("but the dark is still a little past them.")
