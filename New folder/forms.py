from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SelectField,SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, NumberRange

from .models import User


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please user a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a diffrerent email address.')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class addproduct(FlaskForm):
    prodname = StringField('Product Name', validators=[DataRequired()])
    prodqty = IntegerField('Quantity', validators=[NumberRange(min=5, max=1000000),DataRequired()])
    prodsubmit = SubmitField('Save Changes')

class editproduct(FlaskForm):
    editname = StringField('Product Name', validators=[DataRequired()])
    editqty = IntegerField('Quantity', validators=[NumberRange(min=5, max=1000000),DataRequired()])
    editsubmit = SubmitField('Save Changes')

class addlocation(FlaskForm):
    locname = StringField('Location Name', validators=[DataRequired()])
    locsubmit = SubmitField('Save Changes')

class editlocation(FlaskForm):
    editlocname = StringField('Location Name', validators=[DataRequired()])
    editlocsubmit = SubmitField('Save Changes')

class moveproduct(FlaskForm):
    mprodname = SelectField(
        'Product Name')
    src = SelectField(
        'Source')
    destination = SelectField(
        'Destination')
    mprodqty = IntegerField('Quantity', validators=[NumberRange(min=5, max=1000000),DataRequired()])
    movesubmit = SubmitField('Move')
