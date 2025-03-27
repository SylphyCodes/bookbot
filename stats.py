def sort_on(dict):
    return dict["num"]

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

def get_sorted(dict):
    char_list = []
    char_list = list(dict)
    #print(char_list)
    value_list = []
    dict_list = []

    for char in char_list:
        value_list.append(dict[char])

    #print(value_list)
    #print(char_list)

    for i in range(0, len(value_list)):
        if char_list[i].isalpha():   
            new_dict = {}
            new_dict["char"] = char_list[i]
            new_dict["num"] = value_list[i]
            dict_list.append(new_dict)
    
    dict_list.sort(reverse=True, key=sort_on)
    
    return dict_list
    
