from stats import *
def get_book_text(file_path):
    # Added encoding='utf-8' to prevent errors with special characters
    with open(file_path, encoding='utf-8') as f:
        file_contents = f.read()
    return file_contents



def main():
    # Using the absolute WSL path to your Windows folder
    # Note: Check if it is Bookworm or BookWorm!
    book_path = "books/frankenstein.txt"
    
    try:
        book_text = get_book_text(book_path)
        # print(book_text)
    except FileNotFoundError:
        print(f"Error: The file at {book_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    total = number_of_words(book_text)
        
    print(f"Found {total} total words")
    char = number_of_unique_words(book_text)
    print(f"Ocuurance of each character is - {char}")
main()