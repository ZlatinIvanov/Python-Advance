        # 1st solve
# occurrences = {}
#
# for letter in input():
#     # same as the bellow
#     occurrences[letter] = occurrences.get(letter, 0) + 1
#     # if letter not in occurrences:
#     #     occurrences[letter] = 0
#     # occurrences[letter] += 1
#
# for letter, times in sorted(occurrences.items()):
#     print(f"{letter}: {times} time/s")

        # 2nd solve
text = input()
for letter in sorted(set(text)):
    print(f"{letter}: {text.count(letter)} time/s")
