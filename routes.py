from app import app
from flask import render_template, redirect, url_for, request, flash

messages = []

@app.route('/')
def main_page():

    return render_template('index.html')

@app.route('/about', methods=['GET', 'POST'])
def about():
    if request.method == 'POST':
        name = request.form['username']
        email = request.form['email']
        phone = request.form['phone_number']

        if not name:
            flash('Field "name" ')
        elif not email:
            flash('Field email ')
        else:
            messages.append({'username': name, 'email': email, 'phone': phone})
            return redirect(url_for('main_page'))
    return render_template('about.html')

@app.route('/admin')
def admin():
    return render_template('admin.html', user_messages=messages)
