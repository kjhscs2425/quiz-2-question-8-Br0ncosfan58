"""
8. Use for-loops to print out every 3-letter word that:
starts with one of these letters: c, t,, b
has one of these letters in the middle: a, o
ends with one of these letters: p, t, n

(This should print out 18 words in total)
"""
import random

def random_word():
    first_letters = ["c", "t", "b"]
    middle_letters = ["a", "o"]
    last_letters = ["p", "t", "n"]
    return f"{random.choice(first_letters)}{random.choice(middle_letters)}{random.choice(last_letters)}"

if __name__ == "__main__":
  for _ in range(18):
    print(random_word())