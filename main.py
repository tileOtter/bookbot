def get_book_text(path):
    with open(path) as book:
        return book.read()
    
def main():
    return get_book_text("books/frankenstein.txt")

book_fp = "books/frankenstein.txt"
from stats import word_count, character_count, sorted_cc

words = main().split()
cc = character_count(main)
sortedchar = sorted_cc(cc)

print("============ BOOKBOT ============")
print(f"Analyzing book found at {book_fp}...")
print("----------- Word Count ----------")
print(f"Found {word_count(words)} total words")  
print("--------- Character Count -------")    
for char in sortedchar:
    if char["character"].isalpha() is True:
        print(f"{char["character"]}: {char["count"]}")
print("============= END ===============")

