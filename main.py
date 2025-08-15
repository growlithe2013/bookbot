from stats import book_length, char_count, dictsort
import sys

def get_book_text(file):
    with open(file) as f:
        contents = f.read()
        return contents
    
def count(list):
    return list["num"]

def main():
    print(f"Found {book_length(get_book_text(sys.argv[1]))} total words")
    chars = char_count(get_book_text(sys.argv[1]))
    sorted=dictsort(chars)
    sorted.sort(reverse=True, key=count)
    for charact in sorted:
        if charact["char"].isalpha()==True:
            print(f"{charact['char']}: {charact['num']}")

if len(sys.argv)<2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


try:
    main()  
except:
    print("Book not found")
    sys.exit(1)