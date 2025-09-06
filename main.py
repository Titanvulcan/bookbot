import sys
from stats import get_book_text, get_num_words, get_chars_dict, analyze_book

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)  
    path = sys.argv[1]
    text = get_book_text(path)
    num_words = get_num_words(text)
    chars = get_chars_dict(text)
    sorted_chars = analyze_book(chars)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for item in sorted_chars:
        ch = item["char"]
        if not ch.isalpha():
            continue
        print(f"{ch}: {item['num']}")
    print("============= END ===============")



if __name__ == "__main__":
    main()


