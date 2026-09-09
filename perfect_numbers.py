import sys
from pathlib import Path

sys.set_int_max_str_digits(0)

exponents = [
    2, 3, 5, 7, 13, 17, 19, 31, 61, 89, 107, 127,
    521, 607, 1279, 2203, 2281, 3217, 4253, 4423,
    9689, 9941, 11213, 19937, 21701, 23209, 44497,
    86243, 110503, 132049, 216091, 756839, 859433,
    1257787, 1398269, 2976221, 3021377, 6972593,
    13466917, 20996011, 24036583, 25964951, 30402457,
    32582657, 37156667, 42643801, 43112609, 57885161,
    74207281, 77232917, 82589933, 136279841
]

filename = "52_known_perfect_numbers.txt"

with open(filename, "w", encoding="utf-8") as file:

    for number, p in enumerate(exponents, start=1):

        # Perfect number:
        # 2^(p-1) * (2^p - 1)
        perfect_number = (2 ** (p - 1)) * (2 ** p - 1)

        digits = len(str(perfect_number))

        file.write(f"PERFECT NUMBER #{number}\n")
        file.write(f"Mersenne exponent: {p}\n")
        file.write(f"Number of digits: {digits:,}\n")
        file.write("-" * 60 + "\n")
        file.write(str(perfect_number))
        file.write("\n\n")

        print(f"#{number}/52 completed — {digits:,} digits")

print("\nDONE!")
print(f"Saved as: {filename}")