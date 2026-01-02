from stats import *
import sys
def get_book_text(file_path):
    # Added encoding='utf-8' to prevent errors with special characters
    with open(file_path, encoding='utf-8') as f:
        file_contents = f.read()
    return file_contents



def main():
    # Using the absolute WSL path to your Windows folder
    # Note: Check if it is Bookworm or BookWorm!
    try:
        if(len(sys.argv)<2):
            raise Exception("Usage: python3 main.py <path_to_book>")
        else:
            book_path = sys.argv[1]
    except Exception as e:
        print(e)
        sys.exit(1)

    try:
        book_text = get_book_text(book_path)
        # print(book_text)
    except FileNotFoundError:
        print(f"Error: The file at {book_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    total = number_of_words(book_text)
    char = number_of_unique_words(book_text)
    char_sorted = chars_dict_to_sorted_list(char)
        

    print("============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------")
    print(f"Found {total} total words")
    print("--------- Character Count -------")
    for item in char_sorted:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")


main()