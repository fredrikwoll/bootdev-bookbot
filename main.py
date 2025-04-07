from stats import get_num_words, get_character_count

with open("./books/frankenstein.txt") as f:
    file_contents = f.read()
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    num_words = get_num_words(file_contents)
    print(f"{num_words} words found in the document")
    print("--------- Character Count -------")
    num_characters = get_character_count(file_contents)
    print(num_characters)
    print("============= END ===============")
    
    
    
    
