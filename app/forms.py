from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField
from wtforms.validators import DataRequired


class BooksLibForm(FlaskForm):
    title = StringField('Tytuł', validators=[DataRequired()])
    year = IntegerField('Rok wydania')
    author = SelectField('Wybierz autora')


class AuthorLibForm(FlaskForm):
    name = StringField('Autor', validators=[DataRequired()])


class BorrowedForm(FlaskForm):
    title = SelectField('Wybierz tytuł książki')
    date = StringField(
        'Data wypożyczenia, YYYY-MM-DD', validators=[DataRequired()])
    where = StringField('Komu wypożyczono', validators=[DataRequired()])


class DeleteForm(FlaskForm):
    id = IntegerField('Id', validators=[DataRequired()])
