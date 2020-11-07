from app import app, db
from app.models import Book, Author, Borrowed


@app.shell_context_processor
def make_shell_context():
    return {
       "db": db,
       "Book": Book,
       "Author": Author,
       "Borrowed": Borrowed}


if __name__ == "__main__":
    app.run(debug=True)
