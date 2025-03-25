from stats import get_num_words
from stats import get_char_count

def get_book_text(path_to_file):
    
    file_contents = ""
    with open(path_to_file) as f:
        file_contents = f.read()

    return file_contents

def main():

    text = ""
    count = 0
    path = ("./books/frankenstein.txt")
    char_count = {}
    #print(get_book_text(path))
    text = get_book_text(path)
    count = get_num_words(text)
    print(f"{count} words found in the document")
    char_count = get_char_count(text)
    print(char_count)

main ()
