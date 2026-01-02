def number_of_words(text):
    num = text.split()
    return len(num)

def number_of_unique_words(text):
    text = text.lower()
    words = list(text)
    unique_words = set(words)
    chars = {}
    for word in words:
        if(word in chars):
            chars[word]+=1
        else:
            chars[word] =1
    return chars


def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
   