# route.py
from flask import render_template, redirect, url_for, flash
from ajkmarket import app, db  # Import app and db at the top
from ajkmarket.adbms import User, Item
from ajkmarket.forms import RegisterForm, LoginForm
from flask_login import login_user

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/market')
def market_page():
    items = Item.query.all()
    return render_template('market.html', items=items)

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(
            attempted_password=form.password.data
        ):
            login_user(attempted_user)
            flash(f'Success! You are logged in as: {attempted_user.username}', category='success')
            return redirect(url_for('market_page'))
        else:
            flash('Username and password do not match! Please try again.', category='danger')
    
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        existing_user = User.query.filter_by(email_address=form.email_address.data).first()
        
        if existing_user:
            flash('Email address already in use. Please use a different email address.', category='danger')
            return redirect(url_for('register_page'))
        
        user_to_create = User(
            username=form.username.data, 
            email_address=form.email_address.data,
            password=form.password1.data  # Assuming you'll hash this later
        )
        db.session.add(user_to_create)
        db.session.commit()
        flash(f'Account created successfully! You are now logged in as {user_to_create.username}.', category='success')
        login_user(user_to_create)
        return redirect(url_for('market_page'))
    
    return render_template('register.html', form=form)
