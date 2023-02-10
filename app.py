from utils import database

user_choice = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit
Your choice:
"""

def menu():
    database.create_table()
    user_input = input(user_choice)
    while user_input != 'q':
        if user_input == 'a':
            title = input("what's the title?")
            author = input("what's the author")
            database.addNewBook(title, author)
        elif user_input == 'l':
            res = database.listAllBooks()
            if res:
                for x in res:
                    print(f'{x["Name"]},{x["Author"]},{x["Read"]}')
            else:
                print('No books found')
        elif user_input == 'r':
            title = input("what's the title?")
            database.mark(title)
        elif user_input == 'd':
            title = input("what's the title?")
            database.deleteBook(title)
        user_input = input(user_choice)
menu()


