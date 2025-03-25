def get_num_words(text):
    words = []
    words = text.split()
    counter = len(words)
    return counter

def get_char_count(text):

    list_of_chars = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p",
                     "q","r","s","t","u","v","w","y","z"]
    char_count = {}
    lowered_text = text.lower()
    #print(lowered_text)
    #amount_t = lowered_text.count("t")
    #print(amount_t)
    
    for char in list_of_chars:
        #print(char)
        #print(lowered_text.count(char))
        char_count[char] = lowered_text.count(char)
        #print(char_count)

    #print(char_count)
    return char_count
