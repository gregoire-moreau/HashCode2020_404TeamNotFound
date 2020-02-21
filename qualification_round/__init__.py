import sys
from evaluate import evaluate
from pick import choose_library
import random

if __name__ == '__main__':
    FILE = sys.argv[1]
    with open('input/'+FILE+'.txt', 'r') as f:
        first = f.readline().strip().split()
        B = int(first[0])
        L = int(first[1])
        D = int(first[2])
        line = f.readline().strip().split()
        book_scores = {i:int(line[i]) for i in range(len(line))}
        libraries = {}
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
            libraries[i] = (i, N, T, M, books)
        max_occ = -1
        for key in library_books:
            if len(library_books[key]) > max_occ:
                max_occ = len(library_books[key])
        print(max_occ)
    # WHILE D > 0
    while D > 0:
        best_library = []
        best_score = []
        best_books = []
        for library in libraries.values():
            score, books = evaluate(library, D, book_scores, library_books, max_occ)
            '''
            if score > best_score:
                best_score = score
                best_library = library[0]
                best_books = books
            '''
            if score > 0:
                best_score.append(score)
                best_books.append(books)
                best_library.append(library[0])
        if len(best_score) == 0:
            break

        a = []
        for i in range(len(best_score)):
            a.append((best_score[i], best_books[i], best_library[i]))
        a.sort(key=lambda i:i[0], reverse=True)
        index = random.randint(0, min(len(a)-1, 2))
        best_library = a[index][2]
        best_score = a[index][0]
        best_books = a[index][1]
        #print(D)

        # FIND BEST LIBRARY
        # ADD TO OUTPUT LIBRARY AND ITS BOOKS
        # REMOVE BOOKS
        # REMOVE LIBRARY
        D -= libraries[best_library][2]
        choose_library(best_library, output, libraries, library_books, best_books)
        # DECREASE D


    with open('output/'+FILE+'.txt', 'w') as out:
        out.write(str(len(output)))
        out.write('\n')
        for library in output:
            out.write('%d %d\n' % (library[0], len(library[1])))
            for bookid in library[1]:
                out.write('%d ' % bookid)
            out.write('\n')
