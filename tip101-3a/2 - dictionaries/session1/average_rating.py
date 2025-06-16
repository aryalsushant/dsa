
"""
Example Input:

book_ratings = {
    "The Great Gatsby": [4.5, 3.0, 5.0],
    "To Kill a Mockingbird": [4.8, 5.0, 4.0, 4.9]
}
Example Output:

{
    "The Great Gatsby": 4.2,
    "To Kill a Mockingbird": 4.7
}

"""

def average_book_ratings(book_ratings):
    average_ratings = {}
    for book,rating in book_ratings.items():
        average = sum(rating)/len(rating)
        average = round(average, 1)
        average_ratings[book] = average
    return average_ratings

#test case
book_ratings = {
    "The Great Gatsby": [4.5, 3.0, 5.0],
    "To Kill a Mockingbird": [4.8, 5.0, 4.0, 4.9]
}

print(average_book_ratings(book_ratings))
