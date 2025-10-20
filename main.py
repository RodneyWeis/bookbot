import sys
from stats import count_words, count_characters, sort_dict

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_and_file = sys.argv[1]
    print("============ BOOKBOT ============")
    print("Analyzing book found at {path_and_file}...".format(path_and_file=path_and_file))
    print("----------- Word Count ----------")
    book_text = get_book_text(path_and_file)
    num_words = count_words(book_text)
    print('Found {num_words} total words'.format(num_words=num_words))
    character_dict = count_characters(book_text)
    print("--------- Character Count -------")
    sorted_characters = sort_dict(character_dict)
    for character in sorted_characters:
        print("{char}: {count}".format(char=character[0], count=character[1])   )
    print("============= END ===============")

main()
