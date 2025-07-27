import sys
from stats import count_words, character_count, get_book_text,sorted_count, sorted_count

    
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path = sys.argv[1]
    ##path = 'books/frankenstein.txt'
    text = get_book_text(path)
    word_count = count_words(text)

    char_count = character_count(text)

    print("============ BOOKBOT ============")
    print(f"\n Analyzing book found at {path}...")
    print("\n----------- Word Count ----------")
    print(f"\n Found {word_count} total words")
    print("\n--------- Character Count -------")




    ##char_count.sorta
    ##print(f"'{char_count}':{char_count.items()}")
    ##print (sorted_count(char_count))
    

    for value in sorted_count(char_count):
        if value["char"].isalpha():
            print (f'{value["char"]}: {value["num"]}')


    print("\n============= END ===============")

    ##for i, count in char_count.items():
        ##print(f"'{char_count}':{count}"



    print (sys.argv)

main()