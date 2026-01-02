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

