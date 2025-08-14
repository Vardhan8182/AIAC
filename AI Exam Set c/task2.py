def recommend_books_by_genre(books, preferred_genre):
    recommended = [book for book, genre in books if genre.lower() == preferred_genre.lower()]
    return recommended

# Example list of books with their genres
books = [
    ("To Kill a Mockingbird", "Fiction"),
    ("A Brief History of Time", "Science"),
    ("The Great Gatsby", "Fiction"),
    ("The Art of Computer Programming", "Technology"),
    ("The Hobbit", "Fantasy"),
    ("The Lord of the Rings", "Fantasy"),
    ("Sapiens", "History"),
    ("1984", "Fiction"),
    ("The Selfish Gene", "Science"),
    ("Clean Code", "Technology")
]

preferred_genre = input("Enter your preferred genre: ")

recommended = recommend_books_by_genre(books, preferred_genre)

if recommended:
    print("Recommended books in the genre '{}':".format(preferred_genre))
    for book in recommended:
        print("-", book)
else:
    print("No books found in the genre '{}'.".format(preferred_genre))
