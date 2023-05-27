# https://www.geeksforgeeks.org/python-itertools/              itertools examples
# https://www.youtube.com/watch?v=WR7mO_jYN9g                  Iterators, Iterables, and Itertools (video)
# https://docs.python.org/3/library/itertools.html             itertools documentation
# https://www.youtube.com/watch?v=65DeP_qAnX8&list=PLGKQkV4guDKEn-pF85NoIL_-VYIFz3ppo  9 itertools videos

import os
from itertools import combinations, permutations
os.system('cls')

letters = combinations('ABCD', 3)
numbers = combinations(range(4), 3)
either = combinations(['A', 4, 'z', 9], 3)

print('------- COMBINATIONS -------')
print(f"LETTERS: {list(letters)}")
print(f"NUMBERS: {list(numbers)}")
print(f"EITHER: {list(either)}")
print()

letters = permutations('ABCD', 3)
numbers = permutations(range(4), 3)
either = permutations(['A', 4, 'z', 9], 3)


print('------- PERMUTATIONS -------')
print(f"LETTERS: {list(letters)}")
print(f"NUMBERS: {list(numbers)}")
print(f"EITHER: {list(either)}")
print()
