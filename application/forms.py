from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired,Email,Length

class UserForm(FlaskForm):
    name = StringField('Name', validators=[Length(min=2,max=30),DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email(message='Invalid email address')])
    role = StringField('Role', validators=[Length(min=2,max=20),DataRequired()])
    submit = SubmitField('Submit')
    