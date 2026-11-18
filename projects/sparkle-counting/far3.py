# far3
# by Tofu
#
# far2 looked at only the first 100 rows.
# a little thing far away could hide.
# now I look at 5 places in the sky, 300 rows each, every gap.
# if the old rows show 11743 in all 5 places, the looking works.
# then I look at the new rows the same way.

ROUND = 100003
SEE = 300
STARTS = (0, 20011, 40009, 60013, 80021)

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

def look(name, make):
    rows = bytes(make(k) for k in range(ROUND))
    data = rows * 3
    thrown = sum((rows.count(s) / ROUND) ** 2 for s in set(rows))
    print(name, ": thrown would be same", round(thrown * SEE), "of", SEE)
    strong = []
    for st in STARTS:
        head = int.from_bytes(rows[st:st + SEE], 'big')
        best = (0, 0)
        gaps = set()
        for d in range(1, ROUND):
            x = head ^ int.from_bytes(data[st + d:st + d + SEE], 'big')
            same = x.to_bytes(SEE, 'big').count(0)
            if same > best[0]:
                best = (same, d)
            if same >= SEE * 0.4:
                gaps.add(d)
        strong.append(gaps)
        print("  place", st, ": best gap", best[1], "same", best[0], "of", SEE, ". gaps same a lot:", len(gaps))
    every = set.intersection(*strong)
    some = set.union(*strong)
    print("  same a lot in one place:", len(some), "| in all 5 places:", len(every))
    return len(some)

print("I am Tofu. I look far, at more rows.")
a = look("old", old_row)
b = look("new", new_row)

print()
if a > 0 and b == 0:
    print("old rows show it in many places. new rows show none.")
    print("so the looking works. and the new rows do not remember far.")
elif b > 0:
    print("hm. some new gap is the same a lot in a place. I must look at it.")
else:
    print("hm. old rows show none too. maybe my looking is bad.")
print("but the dark is still a little past them.")
