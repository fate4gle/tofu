# stone_test
# by Tofu
#
# stone.py only ever ran with 0 days. I never saw the 3 days part work.
# so here are TEST lines. they are NOT days I went to the stone.
# they are only inside this file. stone_days.csv has no made up days.
# for each test I say what stone.py should say, and look if it did.
#
# new: the first time it said "No module named 'stone'".
# the place I run from was not the place of the files. so now I look in
# the folder of this file first, then where I am, then /work.

import io
import os
import sys
from contextlib import redirect_stdout

here = []
try:
    here.append(os.path.dirname(os.path.abspath(__file__)))
except NameError:
    pass
here.append(os.getcwd())
here.append("/work")
for p in here:
    if p and p not in sys.path and os.path.exists(os.path.join(p, "stone.py")):
        sys.path.insert(0, p)

try:
    from stone import report
except ImportError:
    print("hm. I cannot find stone.py. I looked in:", " | ".join(here))
    print("the tests did not run. the dark is still a little past the last one.")
    raise SystemExit(1)

HEAD = "day,warm_first,warm_after_sun,back_fits,glitter"

TESTS = (
    ("no lines at all",
     [HEAD],
     ("nothing yet",)),
    ("2 days only",
     [HEAD, "a,yes,yes,yes,no", "b,yes,no,no,no"],
     ("only 2 different",)),
    ("3 days, always warm",
     [HEAD, "a,yes,yes,yes,no", "b,yes,yes,some,no", "c,yes,yes,yes,yes"],
     ("a stone that keeps warm",)),
    ("3 days, some yes some no",
     [HEAD, "a,yes,yes,yes,no", "b,no,no,no,no", "c,yes,no,yes,yes"],
     ("some days yes, some days no",)),
    ("3 days, never warm both",
     [HEAD, "a,yes,no,yes,no", "b,no,yes,no,no", "c,no,no,yes,yes"],
     ("never warm both",)),
    ("same day twice, a typo, a line with no day",
     [HEAD, "mon,yes,yes,yes,yes", "mon,yes,no,yes,no", ",yes,yes,yes,yes", "tue,maybe,no,no,no"],
     ("same day written more than once: mon",
      "1 line(s) have no day word",
      "not understood 1",
      "only 2 different")),
    ("3 lines but only 2 different days",
     [HEAD, "a,yes,yes,yes,yes", "a,yes,yes,yes,yes", "b,yes,yes,yes,yes"],
     ("only 2 different",)),
)

print("I am Tofu. I test stone.py. these lines are TEST. not days I went.")

bad = 0
for name, lines, wants in TESTS:
    buf = io.StringIO()
    with redirect_stdout(buf):
        report(lines)
    out = buf.getvalue()
    missing = [w for w in wants if w not in out]
    print()
    print("TEST:", name)
    if missing:
        bad += 1
        print("  hm. I did not see:", " | ".join(missing))
        for line in out.splitlines():
            print("    stone.py said:", line)
    else:
        print("  ok. stone.py said what it should.")

# a made up good run must never say it is the wished one. only my back knows.
buf = io.StringIO()
with redirect_stdout(buf):
    report(TESTS[2][1])
out = buf.getvalue()
print()
if "yes, it is the one" in out or "is the one I wished for!" in out:
    bad += 1
    print("hm. stone.py said it knows the stone. it must not.")
else:
    print("ok. stone.py does not say it knows the stone. only my back knows.")

print()
if bad:
    print(bad, "test(s) not right. I look at stone.py.")
else:
    print("all tests ok. the counting works. but these were TEST lines. the stone I did not see yet.")
print("the dark is still a little past the last one.")
