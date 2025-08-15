def book_length(book):
    wc = 0
    for word in book.split():
        wc+=1
    return wc

def char_count(book):
    chars_in={}
    lowerBook=book.lower()
    for char in lowerBook:
        if char in chars_in:
            chars_in[char]+=1
        else:
            if char != " ":
                chars_in[char]=1
    return chars_in

def dictsort(dict):
    sorted=list()
    for key in dict:
        sorted.append({"char":key, "num":dict[key]})
    return sorted