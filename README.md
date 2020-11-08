# Library_2_0

Welcome to my home_library app!

Initially, you can test the application with the test database that is attached.

The requirements.txt file contains all the modules that are needed for the application to work properly.

After activate installed virtual environment, you need to type 'flask run' into your command line being in the folder where the 'home_library.py' is.

Type http://localhost:5000/books/ in your browser to view the books in your database.

By given links there, you can see the list of authors and the list of borrowings.
You can also add a new title, but remember that you have to add new author first if he/she's not already on your list.
By clicking on the existing title you can see details of this book, you can change data or delete it from database.
By given link or typing http://localhost:5000/authors/ you can see the list of authors.
You can add new author.
By clicking on the author name you can see all of his books in your library. You can delete author or one of his book if needed.
By given link or typing http://localhost:5000/borrowing/ you can see the list of your book borrowings.
You can add some records about which book, when and to whom it was loaned.
You can choose the record of given id and change the status to returned.
