from flask import render_template

def render_home():
    return render_template('home.html')

def render_login():
    return render_template('login.html')

def render_register():
    return render_template('register.html')
