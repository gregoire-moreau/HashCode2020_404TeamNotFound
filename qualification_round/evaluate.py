
def evaluate_count(library, remaining_days, book_scores):
    score = min((remaining_days - library[2]) * library[3], len(library[4]))
    if score <= 0:
        return 0, []
    return score, library[4][:score]


def evaluate(library, remaining_days, book_scores):
    number, books = evaluate_count(library, remaining_days, book_scores)
    score = 0
    for book in books:
        score += book_scores[book]
    return score / library[2], books
