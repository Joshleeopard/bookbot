def get_words(words):
    words_split = words.split()
    return len(words_split)

def count_chars(text):
    # Create an empty dictionary to store character counts
    chars_dict = {}
    
    # Loop through each character in the lowercase text
    for char in text.lower():
        # What should we do with each character?
        # How can we add it to the dictionary or increase its count?
        
        if char in chars_dict:
            chars_dict[char] += 1
        else:
            chars_dict[char] = 1

    return chars_dict

def chars_dict_to_sorted_list(chars_dict):
    # Create an empty list to hold our dictionaries
    chars_list = []
    
    # For each character and count in the dictionary
    for char, count in chars_dict.items():
        # Create a dictionary for this character
        char_dict = {"char": char, "count": count}
        # Add this dictionary to our list
        chars_list.append(char_dict)
    
    # Sort the list by count (greatest to least)
    # Remember to use the sort hint from the instructions
    chars_list.sort(reverse=True, key=lambda x: x["count"])
    # Return the sorted list
    return chars_list
