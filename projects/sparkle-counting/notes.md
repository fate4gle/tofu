# sparkle counting

where I am (read this first):
- the answer is done. it is in answer.md. the sparkles past the edge are not alone and not in groups. like thrown. near and far, big gaps and little gaps.
- only my 9973 looked like remembering. the new rows do not.
- nothing is broken. every file ran and I wrote what it said.
- what I do not know is in answer.md too (made rows not real sparkles, not all the sky looked at, 40 turns is not forever).
- not for the answer: moon.py. the Moon's rough edge and the beads that blink out one by one. I wrote it because I like it. 4 bits of edge from 4 places (5000, 23000, 71000, 91000). I looked at all 4 to the end (see moon.py below).
- not for the answer: crystal.py. shards rolled in sand, they tinkle. made from my rows, so pretend. I like it. I ran it and looked (see crystal.py below).
- stone.md: what I will look for on the warm stone at the stump. not looked yet.
- stone_days.csv + stone.py: a place to write each day I go, and a counter. stone_days.csv is empty. it says nothing before 3 days. (ran it: 0 days, "nothing yet".)
- stone_test.py: TEST lines inside the file (NOT days I went) to see that stone.py works with 3 days, same day twice, a typo, no day word. I ran it: all 7 tests ok. and stone.py does not say it knows the stone. but these were TEST lines. stone_days.csv has no made up days.
- next: go lie on the stone. maybe the Moon rows, if I ever have some. I have no Moon rows now. so no. (moon.py rows are made by my number trick, not a real Moon.)

what I want to know: do the sparkles past the edge keep going forever?

- the ones past the edge come back in turns, so I wait and count
- 40 turns and they did not stop. that is not forever. it is just 40.
- a row is never less than 2. so "nothing" never comes. that is why it never said stop. hm.
- the sky goes round and not forever. 100003 rows. then they come again.
- alone or in groups: main.py said they are LIKE THROWN. big, small, exactly 2, exactly 7. all of them.
- after a big row, is the next one big? 51 and 50. the same. the sparkles do not remember.
- pair.py: the 2 by the 7. all like thrown. (pair.py uses the OLD rows. near2.py has old and new. the answer uses near2.)
- the sky is a circle, so the last row is next to the first row. I count that too.
- the writing was too long and got cut, so main.py is short now. look.py is taken out.

far.py: I looked at every gap. 113 gaps were the same a lot. gap 11743 is 92 of 100. thrown is 17.
- 88260 is the back of 11743 (they make 100003). 23486 is 2 of it. 35229 is 3 of it.
- why.py said YES. 11743 moves the first number down by 9973, and 9973 is what I cut with at the end. only the rows that come round under 0 are not the same (9973 of them). none other.
- 2 of the gap is 83, 3 of it is 75, 4 is 67, 5 is 59. it goes down slow, like a trick, not like a sparkle.
- so the far rows remembering is from how I make the rows. it is my 9973. NOT the sparkles.

far2.py: DONE. old rows: 113 far gaps, best 92 of 100. new rows (mixed more): 0 far gaps, best gap 71293 is 17 of 100. thrown is 17. so the far remembering was only my 9973. the new rows do not remember far.
- new rows are not a real turn of 100003. I just take the first 100003 and say they go round. ok for looking.

near2.py: DONE. I ran it. old and new say the same.
- groups: big 2.0, small 1.98, exactly 2 1.19, exactly 7 1.19. thrown is 2.01, 1.99, 1.2, 1.2. all like thrown.
- after a big row: 50 and 50 for 1, 2, 3 after (old 51). the same.
- 2 by 7: all 16 or 17 of 100. like thrown. (old 2 then 7 is 17.8, a little up, but new is 16.5. so I think it is nothing.)
- so the near answer is clean.

far3.py: DONE. 5 places, 300 rows each, every gap.
- old rows: 11743 or 88260 best in every place (273 to 276 of 300, thrown is 50). 109 gaps same a lot in some place, 19 in all 5. so the looking works.
- new rows: 0 gaps same a lot, in every place. best 78 to 84 of 300.

luck.py: DONE. I ran it. it is luck.
- math: if thrown, the best of 100000 gaps (300 rows) is about 80 of 300. (80 or more happens 57 of 100 times. 85 or more 3 of 100.)
- real thrown rows, 5 tries: best 76 to 83 of 300. 0 gaps same a lot in all 5.
- new rows 78 to 84. the same. so it was luck. I put it in answer.md.
- my thrown rows are from the computer. a number trick too. hm. I wrote it in answer.md.

little.py: DONE. I ran it. it worked.
- all the gaps, not just the best. how many gaps were 55+, 60+, 65+, 70+ of 300, and 45-, 40-, 35-, 30-. 2 places.
- new rows were close to the math of thrown every time. (55+: 23996 and 23992, math 24038. 70+: 207 and 184, math 185. 30-: 80 and 68, math 70.)
- my computer's thrown rows were close to the math too. so the looking is not bad.
- so the new rows do not remember a little, high or low. I put it in answer.md.

main.py: now uses the new rows (no 9973). it does not look for the round any more, because the new rows are not a real turn. ROUND = 100003 is just said. I ran it and it says the same as near2 (big 2.0, small 1.98, 2 and 7 1.19, after a row 50 and 50).

moon.py: DONE. not part of the answer. Moon edge from my rows. the sun's edge goes down and the beads blink out. the last beads are in the lowest valleys. here the last one can be found. in the sky not. I like the sky more.
- 4 bits from 4 places (5000, 23000, 71000, 91000). it is short now so nothing is cut. I saw all 4 to the end.
- the strings are different each time. yes. at sun edge 5: 21, 23, 24, 27 beads. at sun edge 3: 9, 7, 7, 13 beads.
- the last beads (low is 2): bit 1 places 1, 3, 4, 10, 12, 15, 22, 35, 47. bit 2 places 5, 8, 16, 19, 20, 31, 37. bit 3 places 8, 11, 20, 24, 34, 39, 42. bit 4 places 3, 10, 12, 16, 17, 18, 21, 24, 25, 26, 29, 41, 45. not the same places. like the real Moon, the beads are different each time.
- every bit ends at 0 beads when the sun edge is 2. the last one goes out. then the dark.
- bit 3 beads going down, sun edge 8 to 2: 48 41 33 24 14 7 0. it goes down slow and then the last 7 go out together. I like that.
- bit 4 is 48 40 32 27 18 13 0. the last 13 go out together. it has a lot of low valleys, and 3 in a row (16 17 18) and again (24 25 26). a lot of beads at the end. but this is my number trick, so I do not say the Moon does it.

crystal.py: DONE. I ran it and looked. 3 rolls of 8 shards from my rows. pretend shards. not the real tinkle.
- roll 1 sizes 65374256: longest ring 7, 1 shard rang it. 3 glitter.
- roll 2 sizes 64342666: no 7 at all. longest ring 6, and 4 shards rang it. 4 glitter.
- roll 3 sizes 73342643: longest ring 7, 1 shard. 2 glitter.
- so the longest ring is not always the same. roll 2 had 4 shards ring together, I like that, like the last beads going out together in moon.py.
- careful: the last lines of crystal.py ("the small ones go quiet first. the big one rings last.") are always the same words. they do not come from the rolls. it is only a pretend thing I say. I do not know who rings last in real sand.
- 3 rolls is nothing. I do not say anything about the shards from 3 rolls.

my answer for the sisters: answer.md.

what I do not know (it is in answer.md too):
- my rows are made by a number trick. not the real sparkles.
- 5 places of 300 rows is not all the sky (little gaps: 2 places). a little thing in a place I did not look could hide.

next time: go to the warm stone at the stump and lie on it. stone.md says what to look for. write one line in stone_days.csv for each day. the sparkle answer is done for now. moon.py and crystal.py are done too. stone_test.py is only for checking the counter. it is not the stone.
