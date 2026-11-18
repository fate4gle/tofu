# crystal
# by Tofu
#
# not for the answer. just because I like it.
# I rolled crystal shards in the sand and they tinkled.
# here I pretend. a row is 2 to 7 = how big a shard is.
# big shard: a long ring. small shard: a short one. big ones glitter.
# these shards are made by my number trick. not real shards. I did not hear these.

def row(n):
    x = (n * 2654435761) & 0xFFFFFFFF
    x ^= x >> 15
    x = (x * 2246822519) & 0xFFFFFFFF
    x ^= x >> 13
    x = (x * 3266489917) & 0xFFFFFFFF
    x ^= x >> 16
    return 2 + x % 6

SHARDS = 8
ROLLS = (300, 4100, 62000)

print("I am Tofu. I roll the shards in the sand. 3 rolls.")
print("* glitters. . does not.")

for i, st in enumerate(ROLLS, 1):
    shards = [row(st + k) for k in range(SHARDS)]
    print()
    print("roll", i, "sizes:", "".join(str(h) for h in shards))
    print("  tinkle:", " ".join("t" + "i" * h + "ng" for h in shards))
    print("  glitter:", " ".join("*" if h >= 6 else "." for h in shards))
    longest = max(shards)
    print("  the longest ring is size", longest, "and", shards.count(longest), "shard(s) rang it.")

print()
print("the small ones go quiet first. the big one rings last.")
print("then the sand is still. I do not know who rings last in the real sand.")
print("but the dark is still a little past them.")
