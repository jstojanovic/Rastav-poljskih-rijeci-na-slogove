Here is a function that takes a Polish word as a parameter, splits it into individual letters, and maps those letters to the corresponding categories specified in the question:

Copy code
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
