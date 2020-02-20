
def evaluate_count(library, remaining_days, book_scores):
    score = min((remaining_days - library[2]) * library[3], len(library[4]))
    return score, library[4][:score]


def evaluate(library, remaining_days, book_scores):
    number, books = evaluate_count(library, remaining_days, book_scores)
    score = 0
    for book in books:
        score += book_scores[book]
    return score, books
