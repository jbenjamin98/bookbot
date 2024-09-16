def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    character_dictionary = get_character_dictionary(text)
    character_list = convert_dict_to_list(character_dictionary)
    character_list_sorted = sort_character_list(character_list)
    print_report(book_path, word_count, character_list_sorted)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    words = text.split()
    return len(words)

def get_character_dictionary(text):
    character_dictionary = {}
    lowered_string = text.lower()
    for character in lowered_string:
        if character_dictionary.get(character) == None:
            character_dictionary[character] = 1
        else:
            character_dictionary[character] += 1
    return character_dictionary

def convert_dict_to_list(character_dictionary): 
    character_list = []
    for item in character_dictionary:
        if item.isalpha():
            character_list.append({"character": item, "count": character_dictionary[item]})
    return character_list

def sort_character_list(character_list):
    character_list_sorted = character_list
    character_list_sorted.sort(reverse=True, key=sort_on)
    return character_list_sorted

def sort_on(dict):
    return dict["count"]

def format_character_count(character_list):
    formatted_character_count = ""
    for item in character_list:
        formatted_character_count = f"{formatted_character_count} \n The '{item["character"]}' character was found {item["count"]} times"
    return formatted_character_count

def print_report(path, word_count, character_list):
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document")
    print(format_character_count(character_list))
    print("--- End Report ---")


main()