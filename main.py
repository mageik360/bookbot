from stats import word_counter
from stats import letter_counter
from stats import dict_sorter
from sys import argv

def get_book_text(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return f"Error: File '{filepath}' not found."
    



def main():
    input = argv
    filepath = input[1]
    book_text = get_book_text(filepath)
    num_words = word_counter(book_text)
    letter_dictionary = letter_counter(book_text)
    sorted_list = dict_sorter(letter_dictionary)

    
    
    

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for pair in sorted_list:
        if pair["character"].isalpha():
            print(f"{pair["character"]}: {pair["count"]}")
    print("============= END ===============")
if __name__ == "__main__":
    main()