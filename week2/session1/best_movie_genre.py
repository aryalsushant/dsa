"""
so we take in a list of dictionaries with keys movie, genre, and rating
our goal is to return the genre with highest average rating

first, we create two empty lists
one maps genre to total count
another maps genre to total rating

then, we loop through original list

if genre is not in total count, we append genre+its count(1)
we also append genre+rating in another dict
if it is, we incrase the value by 1
in another list, we add the ratings

then,
we create a integer highest_avg for best average rating
we create an empty string for best genre

average = totalrating/count
loop through the dictionary of genre and total rating

if average is higher than best average,
best average = average
best genre = genre

then at the end we return the best genre
"""

def most_popular_genre(movies):
    total_count={}
    total_rating={}

    

    for movie in movies:

        genre = movie["genre"]
        rating = movie["rating"]

        if genre not in total_rating:
            total_rating[genre] = rating
            total_count[genre] = 1
        else:
            total_rating[genre] += rating
            total_count[genre] += 1

    highest_avg = 0
    best_genre = ""

    for genre in total_rating:
        average = total_rating[genre]/total_count[genre]
        if average > highest_avg:
            highest_avg = average
            best_genre = genre
    return best_genre

#test case
movies = [
    {"title": "Inception",
     "genre": "Science Fiction",
     "rating": 8.8
    },
    {"title": "The Matrix", 
     "genre": "Science Fiction",
     "rating": 8.7
    },
    {"title": "Pride and Prejudice", 
     "genre": "Romance",
     "rating": 7.8
    },
    {"title": "Sense and Sensibility", 
     "genre": "Romance",
     "rating": 7.7
    }
]

print(most_popular_genre(movies))