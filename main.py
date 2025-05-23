from stats import get_num_words, get_character_count

def get_book_test(file_path):
  with open(file_path) as f:
    file_contents = f.read()
  return file_contents

def main():
  book_contents = get_book_test("books/frankenstein.txt")
  num_words = get_num_words(book_contents)
  word_count_dict = get_character_count(book_contents)
  print(f"{num_words} words found in the document")
  print(word_count_dict)

main()
