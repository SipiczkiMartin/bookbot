def get_num_words(text):
    split_book = text.split()
    return len(split_book)

def get_num_characters(text):
    char_dict = {}
    for char in text.lower():
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict  

def sort_dicts(dict):
    list = []
    for key in dict:
        new_dict = {}
        new_dict["char"] = key
        new_dict["num"] = dict[key]
        list.append(new_dict)
    return sorted(list,key=lambda x: x["num"],reverse=True)
               
     