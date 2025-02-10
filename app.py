from flask import Flask, render_template, request, redirect, flash
from flask_mysqldb import MySQL
import MySQLdb.cursors
import sys

app = Flask(__name__)
app.secret_key = "your_secret_key"

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'hitesh'
app.config['MYSQL_PASSWORD'] = 'hitesh'
app.config['MYSQL_DB'] = 'phonebook'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

def init_db():
    try:
        conn = MySQLdb.connect(
            host=app.config['MYSQL_HOST'],
            user=app.config['MYSQL_USER'],
            passwd=app.config['MYSQL_PASSWORD'],
            cursorclass=MySQLdb.cursors.DictCursor,
        )
        cursor = conn.cursor()
        
        cursor.execute("CREATE DATABASE IF NOT EXISTS phonebook")
        
        cursor.execute("USE phonebook")
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS contacts (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                phone VARCHAR(15) NOT NULL
            )
        """)
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Error during database initialization: {e}")
        sys.exit(1)

init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_contact', methods=['POST'])
def add_contact():
    name = request.form['name']
    phone = request.form['phone']
    
    if name and phone:
        try:
            cursor = mysql.connection.cursor()
            cursor.execute("INSERT INTO contacts (name, phone) VALUES (%s, %s)", (name, phone))
            mysql.connection.commit()
            flash('Contact added successfully!', 'success')
        except Exception as e:
            flash(f"Error adding contact: {e}", 'error')
    else:
        flash('Please provide both name and phone number.', 'error')
    
    return redirect('/')

@app.route('/view_contacts')
def view_contacts():
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM contacts")
        contacts = cursor.fetchall()
        return render_template('view_contacts.html', contacts=contacts)
    except Exception as e:
        flash(f"Error fetching contacts: {e}", 'error')
        return redirect('/')

@app.route('/delete_contact', methods=['POST'])
def delete_contact():
    contact_id = request.form['id']
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("DELETE FROM contacts WHERE id = %s", (contact_id,))
        mysql.connection.commit()
        flash('Contact deleted successfully!', 'success')
    except Exception as e:
        flash(f"Error deleting contact: {e}", 'error')
    return redirect('/view_contacts')

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
