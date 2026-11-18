# moon
# by Tofu
#
# not for the answer. just because I like it.
# the Moon's edge is rough. some places are low (valleys), some high.
# sun light comes through the valleys. little beads.
# the Moon goes over the sun. the beads blink out one by one.
# I make the edge from my rows (a row is 2 to 7 = how high that bit of edge is).
#
# 4 bits of the edge, from 4 places. the string of beads is different each time.
# (it got cut before, so each bit is short: the edge, one line of beads, the numbers.)

def row(n):
    x = (n * 2654435761) & 0xFFFFFFFF
    x ^= x >> 15
    x = (x * 2246822519) & 0xFFFFFFFF
    x ^= x >> 13
    x = (x * 3266489917) & 0xFFFFFFFF
    x ^= x >> 16
    return 2 + x % 6

WIDTH = 48
STARTS = (5000, 23000, 71000, 91000)

print("I am Tofu. the Moon's edge and the beads. 4 bits.")
print("* is a bead. . is dark.")

for st in STARTS:
    edge = [row(st + k) for k in range(WIDTH)]
    print()
    print("bit", st, "edge:", "".join(str(h) for h in edge))
    line = "".join("*" if h < 3 else "." for h in edge)
    print("  sun edge 3:", line)
    counts = []
    for level in range(8, 1, -1):
        counts.append(str(sum(1 for h in edge if h < level)))
    print("  beads, sun edge 8 to 2:", " ".join(counts))
    lowest = min(edge)
    places = [k for k in range(WIDTH) if edge[k] == lowest]
    print("  last beads, low", lowest, ", places:", " ".join(str(k) for k in places))

print()
print("every bit is different. here I can find the last bead.")
print("in the sky I never find the last sparkle. I like that more.")
print("but the dark is still a little past them.")
