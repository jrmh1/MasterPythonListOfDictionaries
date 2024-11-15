
book_ids = [1, 2, 3, 4, 5]
book_titles = ["The Great Gatsby", "To Kill a Mockingbird", "1984", "The Catcher in the Rye", "A Brief History of Time"]
book_authors = ["F. Scott Fitzgerald", "Harper Lee", "George Orwell", "J.D. Salinger", "Stephen Hawking"]
book_genres = ["Fiction", "Fiction", "Dystopian", "Fiction", "Non-fiction"]
book_published_years = [1925, 1960, 1949, 1951, 1988]
book_isbns = ["978-0743273565", "978-0060935467", "978-0451524935", "978-0316769488", "978-0553380163"]
book_stocks = [20, 35, 40, 25, 10]
book_prices = [15.99, 10.99, 9.99, 8.99, 18.99]


print("Book Data:")
for i in range(len(book_ids)):
    print(f"Book ID: {book_ids[i]}, Title: {book_titles[i]}, Author: {book_authors[i]}, Genre: {book_genres[i]}, Published Year: {book_published_years[i]}, ISBN: {book_isbns[i]}, Stock: {book_stocks[i]}, Price: ₱{book_prices[i]}")
