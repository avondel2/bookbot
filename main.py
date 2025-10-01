from stats import get_num_words, get_num_characters
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")

FILEPATH = sys.argv[1]

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


text = get_book_text(FILEPATH)
print("============ BOOKBOT ============")
print(f"Analyzing book found at {FILEPATH}...")
print("----------- Word Count ----------")
num_words = get_num_words(text)
print(f"Found {num_words} total words")
print("--------- Character Count -------")
num_characters = get_num_characters(text)
sorted_num_characters = sorted(num_characters, reverse=True, key=num_characters.get)
for key in sorted_num_characters:
    if key.isalpha():
        print(f"{key}: {num_characters[key]}")
print("============= END ===============")