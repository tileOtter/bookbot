def word_count(words):
    return len(words)

def character_count(main):
    characters = {}
    lowercase = main().lower()
    for letter in lowercase:
        if letter not in characters:
            characters[letter] = 1
        else:
            characters[letter] += 1

    return characters 