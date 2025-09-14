def get_book_text(path):
    with open(path) as book:
        return book.read()
    
def main():
    return get_book_text("books/frankenstein.txt")

words = main().split()

def word_count(words):
    return len(words)

print(f"{word_count(words)} words found in the document.")       


