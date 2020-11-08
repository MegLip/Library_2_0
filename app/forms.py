from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField
from wtforms.validators import DataRequired
from app.models import Book, Author, Borrowed


class BooksLibForm(FlaskForm):
    title = StringField('Tytuł', validators=[DataRequired()])
    year = IntegerField('Rok wydania')
    author = SelectField('Autor')

    @classmethod
    def new(cls):
        # Instantiate the form
        form = cls()
        # Update the choices for the author field
        form.author.choices = [x.name for x in Author.query.all()]
        return form


class AuthorLibForm(FlaskForm):
    name = StringField('Autor', validators=[DataRequired()])


class BorrowedForm(FlaskForm):
    title = SelectField('Tytuł książki')
    date = StringField(
        'Data wypożyczenia, YYYY-MM-DD', validators=[DataRequired()])
    where = StringField('Komu wypożyczono', validators=[DataRequired()])

    @classmethod
    def new(cls):
        form = cls()
        form.title.choices = [x.title for x in Book.query.all()]
        return form


class DeleteForm(FlaskForm):
    id = IntegerField('Id', validators=[DataRequired()])
