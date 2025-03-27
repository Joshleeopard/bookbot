import sys

from stats import get_words, count_chars, chars_dict_to_sorted_list

import sys

# Check if we have the right number of arguments
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

# If we reach here, we have the right number of arguments
# Grab the book path from sys.argv[1]
path_to_book = sys.argv[1]

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        words = f.read()
        return words
    
    
def main():
    path_to_book = sys.argv[1]
    content = get_book_text(path_to_book)
    num_words = get_words(content)
    chars_dict = count_chars(content)
    
    # Get the sorted list of character counts
    chars_sorted = chars_dict_to_sorted_list(chars_dict)
    
    # Print the report header
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
    
    # Print word count section
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    
    # Print character count section
    print("--------- Character Count -------")
    
    # REMOVE THIS LINE:
    # print(f"Found {chars_dict} total words")
    
    # Loop through the sorted characters and print them
    for char_item in chars_sorted:
        char = char_item["char"]
        count = char_item["count"]
        
        if char.isalpha():
            print(f"{char}: {count}")
    
    # Print footer
    print("============= END ===============")

main()