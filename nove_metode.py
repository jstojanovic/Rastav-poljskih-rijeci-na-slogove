import re

def rastav_na_slova(word):
  return re.findall(r'(i[ąęoóuy]|ii|[^iąęoóuy]+)', word)

word = input().lower()
slova = rastav_na_slova(word)
print(slova)

def classify_letters(word):
  categories = {
    'V' : ('a', 'ą', 'e', 'ę', 'i', 'o', 'ó', 'u', 'y'),
    'C' : ('G','L','O','F','S','N'),

    'G' : ('j', 'ł'),
    'L' : ('l', 'r'),
    'O' : ('p', 't', 'k', 'b', 'd', 'g', 'q', 'x'),
    'F' : ('dz', 'dż', 'f', 'cz', 'c', 'ć', 'dź', 'z', 'ź', 'ż', 'w', 'h', 'v'),
    'S' : ('ś', 's', 'sz'),
    'N' :  ('n', 'ń', 'm'),
  }

  letters = list(word)
  letter_categories = []
  for letter in letters:
    for category, letters in categories.items():
      if letter in letters:
        letter_categories.append(category)
        break

  return letter_categories
