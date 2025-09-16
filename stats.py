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

def sorted_cc(characters):
    def sort_on(characters):
        return characters["count"]
    
    sorted = []
    
    for character in characters:
        count = characters[character]
        cc = {
            "character": character,
            "count": count
        }
        sorted.append(cc)

    sorted.sort(reverse=True, key=sort_on)
    return sorted
