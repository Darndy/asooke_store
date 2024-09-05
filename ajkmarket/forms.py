from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from ajkmarket.adbms import User  # Update the import path to use adbms

class RegisterForm(FlaskForm):
    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Username already exixst! please chose a different one')
        
    def validate_email_address(self, email_address_to_check):
        email_address = User.query.filter_by(email_address=email_address_to_check.data).first()
        if email_address:
            raise ValidationError('email address already exist! please try different one')

    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=30)])
    email_address = StringField('Email Address', validators=[DataRequired(), Email()])
    password1 = PasswordField(label='Password', validators=[DataRequired(), Length(min=6)])
    password2 = PasswordField(label='Confirm Password', validators=[DataRequired(), EqualTo('password1', message='Passwords must match')])
    submit = SubmitField('Create Account')

class LoginForm(FlaskForm):
    username = StringField(label='Username:', validators=[DataRequired()])
    password = PasswordField(label='Password:', validators=[DataRequired()])  # Lowercase 'password'
    submit = SubmitField(label='Sign in')
