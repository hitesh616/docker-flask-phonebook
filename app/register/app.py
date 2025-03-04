from flask import Flask, render_template, request, redirect, flash
from flask_mysqldb import MySQL
import MySQLdb.cursors
import os 
import sys

app= Flask(__name__, template_folder='templates')
app.secret_key = "your_secret_key"

app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST')
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = os.getenv('MYSQL_DB')
app.config['MYSQL_CURSORCLASS'] = os.getenv('MYSQL_CURSORCLASS')


print(app.config['MYSQL_HOST'])
print(app.config['MYSQL_USER'])
print(app.config['MYSQL_PASSWORD'])
print(app.config['MYSQL_DB'])

mysql = MySQL(app)

def init_db():
    try:
        conn = MySQLdb.connect(
            host=app.config['MYSQL_HOST'],
            user=app.config['MYSQL_USER'],
            passwd=app.config['MYSQL_PASSWORD'],
            database=app.config['MYSQL_DB'],
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
    
    return redirect("/")

@app.route('/health')
def health():
    return 'Server is running'

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=5001)
