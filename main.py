def main():
    path = "books/frankenstein.txt"
    with open(path) as f:
        file_contents = f.read()
        frakenstein_word_count = count_words(file_contents)
        frankenstein_character_count = count_characters(file_contents)
        frankenstein_list_of_dictionaries = convert_letters_dict(frankenstein_character_count)
        print_function(frankenstein_list_of_dictionaries, path, frakenstein_word_count)

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    letters_dict = {}
    lower_text = text.lower()
    for char in lower_text:
        if char not in letters_dict:
            letters_dict[char] = 1
        else:
            letters_dict[char] += 1

    return letters_dict

 
def convert_letters_dict(letters_dict):
    letter_dict_list = []
    for letter in letters_dict:
        letter_dict_list.append({"name":letter, "num":letters_dict[letter]})

    alpha_dict_list = []
    for dict in letter_dict_list:
        if dict["name"].isalpha():
            alpha_dict_list.append(dict)
    
    alpha_dict_list.sort(reverse=True, key=sort_on)

    return alpha_dict_list


def sort_on(dict):
    return dict["num"]

def print_function(alpha_dict_list, path, word_count):
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document")
    print()
    for dict in alpha_dict_list:
        name = dict["name"]
        num = dict["num"]
        print(f"The '{name}' character was found {num} times")
    print("--- End report ---")


main()