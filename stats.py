def get_num_words(string):
    words = string.split()
    return len(words)
    pass

def get_character_count(string):
    characters = {}
    for character in string:
            if character.lower() in characters:
                characters[character.lower()] += 1
            else:
                characters[character.lower()] = 1
    return characters
    pass