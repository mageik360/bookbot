

def word_counter(text):
    text_array = text.split()
    word_count = len(text_array)
    return word_count

def letter_counter(text):
    
    letter_dict = {}
    for char in text.lower():
        if char in letter_dict:
            letter_dict[char] += 1
        else:
            letter_dict[char] =1
    
    return letter_dict

def sort_on(dict):
    return dict["count"]

def dict_sorter(dict):
    list = [{"character": char, "count":count} for char, count in dict.items()]
    list.sort(reverse=True, key=sort_on)
    return list