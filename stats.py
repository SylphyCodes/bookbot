def get_num_words(text):
    words = []
    words = text.split()
    counter = len(words)
    return counter

def get_char_count(text):

    char_count = {}
    lowered_text = text.lower()
        
    for char in lowered_text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    #print(char_count)
    return char_count
