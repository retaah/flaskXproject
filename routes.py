from app import app
from flask import render_template, redirect, url_for, request, flash
import sqlite3


def db_connect():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


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
            flash('Field "name" ', 'warning')
        elif not email:
            flash('Field email ', 'warning')
        else:
            try:
                connection = db_connect()
                connection.execute('INSERT INTO users (name, email, phone) VALUES (?, ?, ?)',
                                   (name, email, phone))
                connection.commit()
                connection.close()
                flash('form successfully sent')
                return redirect(url_for('about'))
            except sqlite3.IntegrityError:
                flash('User with this email already exist')
                return redirect(url_for('about'))
    return render_template('about.html')

@app.route('/admin')
def admin():
    connection = db_connect()
    users = connection.execute('SELECT * FROM users')
    return render_template('admin.html', users=users)
