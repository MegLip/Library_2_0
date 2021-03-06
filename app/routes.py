from flask import Flask, jsonify, abort, make_response
from flask import request, render_template, redirect, url_for
from app import db, app
from app.models import Book, Author, Borrowed
from app.forms import BooksLibForm, AuthorLibForm, DeleteForm, BorrowedForm


# wyświetla wszystkie książki w bazie lub tworzy nową pozycję książkową
@app.route("/books/", methods=["GET", "POST"])
def books_list():
    form = BooksLibForm.new()
    books_all = Book.query.all()
    if request.method == "POST":
        if form.validate_on_submit():
            book1 = Book(title=form.title.data, year=form.year.data)
            db.session.add(book1)
            db.session.commit()
            author1 = Author.query.filter_by(name=form.author.data).first()
            author1.books.append(book1)
            db.session.commit()
            books_all = Book.query.all()
            return redirect(url_for("books_list"))
    return render_template("books.html", books=books_all, form=form)


# wyświetla wszystkich autorów w bazie lub tworzy nową pozycję autora
@app.route("/authors/", methods=["GET", "POST"])
def authors_list():
    form = AuthorLibForm()
    authors = Author.query.all()
    if request.method == "POST":
        if form.validate_on_submit():
            author1 = Author(name=form.name.data)
            db.session.add(author1)
            db.session.commit()
            authors = Author.query.all()
            return redirect(url_for("authors_list"))
    return render_template("authors.html", authors=authors, form=form)

# wyświetla wypożyczone książki i zwraca True jeśli książka jest wypożyczona
@app.route("/borrowed/", methods=["GET", "POST"])
def borrowed_list():
    form = BorrowedForm.new()
    form2 = DeleteForm()
    borrowed = Borrowed.query.all()
    books = Book.query.all()
    if request.method == "POST":
        if form.validate_on_submit():
            book1 = Book.query.filter_by(title=form.title.data).first()
            borrow = Borrowed(borrowed=True, borrow_date=form.date.data, where=form.where.data, book=book1)
            db.session.add(borrow)
            db.session.commit()
            borrowed = Borrowed.query.all()
            return redirect(url_for("borrowed_list"))
        if form2.validate_on_submit():
            borrow = Borrowed.query.filter_by(id=form2.id.data).first()
            borrow.borrowed = False
            db.session.commit()
            return redirect(url_for("borrowed_list"))
    return render_template("borrowed.html", borrowed=borrowed, form=form, books=books, form2=form2)


# pokazuje konkretny rekord z bazy danych, pozwala na zmianę danych lub usunięcie książki
@app.route("/books/<int:book_id>", methods=["GET", "POST"])
def get_book(book_id):
    form = BooksLibForm()
    book = Book.query.get(book_id)
    if request.method == "POST":
        book = Book.query.get(book_id)
        book.title = form.title.data
        book.year = form.year.data
        db.session.commit()
        author1 = Author.query.filter_by(name=form.author.data)
        author1.books.append(book)
        db.session.commit()
        return redirect(url_for("get_book"))
    return render_template("book.html", book=book, form=form, book_id=book_id)


@app.route("/authors/<int:author_id>", methods=["GET", "POST"])
def get_authors_books(author_id):
    form = DeleteForm()
    author = Author.query.get(author_id)
    books = author.books
    if not author:
        abort(404)
    if request.method == "POST":
        book = Book.query.filter_by(id=form.id.data).first()
        author.books.remove(book)
        db.session.commit()
        return redirect(url_for("get_authors_books"))
    return render_template(
        "author_books.html", author=author.name, books=books,
        author_id=author_id, form=form)


# usuwa rekord książki o danym id z bazy danych
@app.route("/books/<int:book_id>/delete", methods=['GET'])
def delete_book(book_id):
    book = Book.query.get(book_id)
    db.session.delete(book)
    db.session.commit()
    return render_template(
        "books.html", books=Book.query.all(), form=BooksLibForm())


# usuwa rekord autora z bazy danych
@app.route("/authors/<int:author_id>/delete", methods=['GET'])
def delete_author(author_id):
    author = Author.query.get(author_id)
    db.session.delete(author)
    db.session.commit()
    return render_template(
        "authors.html", authors=Author.query.all(), form=AuthorLibForm())


@app.errorhandler(404)
def not_found(error):
    return make_response(
        jsonify({'error': 'Not found', 'status_code': 404}), 404)


@app.errorhandler(400)
def bad_request(error):
    return make_response(
        jsonify({'error': 'Bad request', 'status_code': 400}), 400)
