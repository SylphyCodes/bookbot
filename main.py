def get_book_text(path_to_file):
    
    file_contents = ""
    with open(path_to_file) as f:
        file_contents = f.read()

    return file_contents

def word_count(text):
    words = []
    words = text.split()
    counter = len(words)
    return counter

def main():

    text = ""
    count = 0
    path = ("./books/frankenstein.txt")
    #print(get_book_text(path))
    text = get_book_text(path)
    count = word_count(text)
    print(f"{count} words found in the document")

main ()
