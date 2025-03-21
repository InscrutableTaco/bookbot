import sys
from stats import count_words,count_chars,sort_alpha,sort_freq

path = ""

def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
    return contents

def main():
    #result = get_book_text("books/frankenstein.txt") 
    #print(result)
    print("============ BOOKBOT ============")

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path = sys.argv[1]
        book_text = get_book_text(path)
        word_count = count_words(book_text)
        char_counts = count_chars(book_text)
        print(f"Analyzing book found at {path}...")
        print("----------- Word Count ----------")
        print(f"Found {word_count} total words")
        print("--------- Character Count -------")
        print(sort_freq(char_counts))
        print("============= END ===============")

main()