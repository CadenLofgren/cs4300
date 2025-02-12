favorite_books = [
    ("The Lord of the Rings", "J.R.R. Tolkien"),
    ("Dune", "Frank Herbert"),
    ("Harry Potter and the Sorcerer’s Stone", "J.K. Rowling"),
    ("All Quiet on the Western Front", "Erich Maria Remarque"),
]


first_three_books = favorite_books[:3]
print("First three favorite books:", first_three_books)


student_database = {
    "Caden Lofgren": 1,
    "John Doe": 2
}

print("Student Database:", student_database)

def test_favorite_books():
    assert len(favorite_books) >= 3 
    assert first_three_books == favorite_books[:3]  
    assert favorite_books[0] == ("The Lord of the Rings", "J.R.R. Tolkien") 

def test_student_database():
    assert isinstance(student_database, dict)  
    assert "Caden Lofgren" in student_database  
    assert student_database["John Doe"] == 2