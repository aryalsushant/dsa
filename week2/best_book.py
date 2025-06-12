"""
take in a dictionary of books and their ratings.
return the book with the highest rating

step 1. iterate through the dictionary
step 2. create an empty variable and set it to the value of the first key
step 3. if value > variable, replace variable with the value.
step 4. returm dictionary item with the highest value

this wont work cause the input is not a single dictionary but a list of dictionaries and we are returning the dictionary
with the highest value for the key "rating"

step 1. set a variable for highest rating and assume the first iteration is the best
step 2. loop through the list
step 3. if rating for item is higher than assumed best, replace
step 4. return the best book
"""
def highest_rated(books):
    best = books[0]
    for book in books:
        if book["rating"] > best["rating"]:
            best = book
    return best

#example test case
books = [
    {"title": "Tomorrow, and Tomorrow, and Tomorrow",
     "author": "Gabrielle Zevin",
     "rating": 4.18
    },
    {"title": "A Fortune For Your Disaster",
     "author": "Hanif Abdurraqib",
     "rating": 4.47
    },
    {"title": "The Seven Husbands of Evenlyn Hugo",
     "author": "Taylor Jenkins Reid",
     "rating": 4.40
    }
]

print(highest_rated(books))
