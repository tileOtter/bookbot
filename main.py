def get_book_text(path):
    with open(path) as book:
        return book.read()
    
def main():
    return get_book_text("books/frankenstein.txt")

from stats import word_count

words = main().split()

print(f"{word_count(words)} words found in the document.")       