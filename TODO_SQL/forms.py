from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField
from wtforms.validators import DataRequired

class TodoForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    details = TextAreaField('details', validators=[DataRequired()])
    finish = BooleanField('task is done', validators=[DataRequired()])