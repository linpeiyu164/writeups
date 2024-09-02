from cvc5.pythonic import *

(
    idx_0,
    idx_1,
    idx_2,
    idx_3,
    idx_4,
    idx_5,
    idx_6,
    idx_7,
    idx_8,
    idx_9,
    idx_10,
    idx_11,
    idx_12,
    idx_13,
    idx_14,
    idx_15,
    idx_16,
    idx_17,
    idx_18,
    idx_19,
    idx_20,
    idx_21,
    idx_22,
    idx_23,
    idx_24,
    idx_25,
) = BitVecs(
    "idx_0, idx_1, idx_2, idx_3, idx_4, idx_5, idx_6, idx_7, idx_8, idx_9, idx_10, idx_11, idx_12, idx_13, idx_14, idx_15, idx_16, idx_17, idx_18, idx_19, idx_20, idx_21, idx_22, idx_23, idx_24, idx_25",
    32,
)


s = Solver()

for i in range(26):
    eval(f"s.add(idx_{i} >= 0, idx_{i} <= 255)")

s.add(idx_4 * idx_11 * idx_19 == 391020)

s.add(idx_8 * idx_13 * idx_22 == 567720)

s.add(idx_22 * idx_0 + idx_15 == 4872)

s.add(idx_0 + idx_8 + idx_11 == 199)

s.add(idx_13 - idx_22 * idx_12 == -3721)

s.add(idx_9 * idx_4 - idx_1 == 8037)

s.add(idx_9 * idx_16 * idx_11 == 272832)

s.add(idx_3 * idx_23 + idx_15 == 9792)

s.add(idx_9 - idx_23 - idx_4 == -70)

s.add(idx_5 - idx_21 - idx_8 == -63)

s.add(idx_24 * idx_3 + idx_0 == 5359)

s.add(idx_25 * idx_1 + idx_17 == 10483)

s.add(idx_7 * idx_19 * idx_2 == 893646)

s.add(idx_11 - idx_4 + idx_19 == 93)

s.add(idx_7 + idx_6 - idx_10 == 136)

s.add(idx_0 + idx_25 + idx_10 == 287)

s.add(idx_12 + idx_5 - idx_22 == 104)

s.add(idx_4 * idx_7 + idx_12 == 8243)

s.add(idx_1 - idx_22 + idx_4 == 81)

s.add(idx_8 - (idx_19 * idx_11) == -5503)

s.add(idx_8 - idx_10 - idx_7 == -129)

s.add(idx_20 + idx_22 + idx_21 == 224)

s.add(idx_24 + idx_23 + idx_12 == 232)

s.add(idx_15 - idx_9 + idx_4 == 2)

s.add(idx_9 * idx_15 + idx_2 == 5635)

s.add(idx_24 + idx_14 + idx_16 == 210)

s.add(idx_1 + idx_10 - idx_12 == 125)

s.add(idx_18 - idx_1 - idx_5 == -111)

s.add(idx_12 - idx_14 - idx_7 == -163)

s.add(idx_1 + idx_5 - idx_16 == 158)

if s.check() == sat:
    m = s.model()
    print("".join(chr(m[eval(f"idx_{i}")].as_long() % 256) for i in range(26)))
else:
    print("unsat")
