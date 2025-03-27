from stats import get_num_words
from stats import get_char_count
from stats import get_sorted

def get_book_text(path_to_file):
    
    file_contents = ""
    with open(path_to_file) as f:
        file_contents = f.read()

    return file_contents

def main():

    text = ""
    count = 0
    path = ("books/frankenstein.txt")
    char_count = {}
    #print(get_book_text(path))
    text = get_book_text(path)
    count = get_num_words(text)
    #print(f"{count} words found in the document")
    char_count = get_char_count(text)
    #print(char_count)
    get_sorted(char_count)
    sorted_dict = get_sorted(char_count) 
    #print(sorted_dict)

    # Report

    print(f"============ BOOKBOT ============")
    print(f"Analysing book found at {path}")
    print(f"----------- Word Count ----------")
    print(f"Found {count} total words")
    print(f"--------- Character Count -------")

    for i in range(0, len(sorted_dict)):
        print(f"{sorted_dict[i]['char']}: {sorted_dict[i]['num']}")

    print(f"============= END ===============")
main ()
