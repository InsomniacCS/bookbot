def get_num_words(book):
  word_count = book.split()
  return len(word_count)

def get_character_count(book):
  char_dict = {}
  for char in book:
    char_lower = char.lower()
    if char_lower in char_dict:
      char_dict[char_lower] += 1
    else:
      char_dict[char_lower] = 1
  return char_dict

def sort_dict_desc(book_dict):
  return dict(sorted(book_dict.items(), key=lambda x: x[1], reverse=True))
