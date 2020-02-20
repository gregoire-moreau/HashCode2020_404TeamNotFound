
def choose_library(best_library, output, libraries, library_books, best_books):
    output.append((best_library, best_books))
    for book in best_books:
        for lib in library_books[book]:
            if lib in libraries:
                libraries[lib][4].remove(book)
    del libraries[best_library]
