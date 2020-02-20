import sys
from evaluate import evaluate
from pick import choose_library

if __name__ == '__main__':
    FILE = sys.argv[1]
    with open('input/'+FILE+'.txt', 'r') as f:
        first = f.readline().strip().split()
        B = int(first[0])
        L = int(first[1])
        D = int(first[2])
        line = f.readline().strip().split()
        book_scores = {i:int(line[i]) for i in range(len(line))}
        libraries = []
        library_books = {i:[] for i in range(B)}
        output = []
        for i in range(L):
            line = f.readline().strip().split()
            N = int(line[0])
            T = int(line[1])
            M = int(line[2])
            books = [int(i) for i in f.readline().strip().split()]
            for book in books:
                library_books[book].append(i)
            books.sort(key=lambda x: book_scores[x], reverse=True)
            libraries.append((i, N, T, M, books))
    # WHILE D > 0
    while D > 0:
        best_library = None
        best_score = -1
        best_books = None
        for library in libraries:
            score, books = evaluate(library, D, book_scores)
            if score > best_score:
                best_score = score
                best_library = library
                best_books = books
        if not best_library:
            break

        # FIND BEST LIBRARY
        # ADD TO OUTPUT LIBRARY AND ITS BOOKS
        # REMOVE BOOKS
        # REMOVE LIBRARY
        choose_library(best_library, output, book_scores, libraries, library_books)
        # DECREASE D
        D -= best_library[2]

    with open('output/'+FILE+'.txt', 'w') as out:
        out.write(len(output))
        out.write('\n')
        for library in output:
            out.write('%d %d\n' % (library[0], len(library[1])))
            for bookid in library[1]:
                out.write('%d ' % bookid)
            out.write('\n')
