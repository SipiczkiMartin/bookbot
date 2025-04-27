from stats import sort_dicts
from stats import get_num_characters
from stats import get_num_words
import sys

def get_book_text(filepath):
    content_of_file = None
    with open(filepath) as f:
        content_of_file = f.read()
    return content_of_file


def main():
    if len(sys.argv) <=1:
         print("Usage: python3 main.py <path_to_book>")
         sys.exit(1)
    count = get_num_characters(get_book_text(sys.argv[1]))
    num_words = get_num_words(get_book_text(sys.argv[1]))
    list_dicts = sort_dicts(count)
    print(f"""============ BOOKBOT ============
Analyzing book found at {sys.argv[1]}...
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------""")
    for c in list_dicts:
         if c["char"].isalpha():
              print(f"{c["char"]}: {c["num"]}")
    print("============= END ===============")
            
         

if __name__ == "__main__":
         main()