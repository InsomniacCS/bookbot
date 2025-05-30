import sys
from stats import get_num_words, get_character_count, sort_dict_desc

def get_book_test(file_path):
  with open(file_path) as f:
    file_contents = f.read()
  return file_contents

def main():
  if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

  book_contents = get_book_test(sys.argv[1])
  num_words = get_num_words(book_contents)
  word_count_dict = get_character_count(book_contents)
  sorted_dict = sort_dict_desc(word_count_dict)
  print("============ BOOKBOT ============")
  print("Analyzing book found at books/frankenstein.txt...")
  print("----------- Word Count ----------")
  print(f"Found {num_words} total words")
  print("--------- Character Count -------")
  for key, value in sorted_dict.items():
    if key.isalpha():
      print(f"{key}: {value}")
  print("============= END ===============")

main()