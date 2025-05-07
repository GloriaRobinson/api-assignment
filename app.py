from flask import Flask, jsonify
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

def get_db_connection():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',  
            password='mysql',  
            database='studentapi'
        )
        return conn
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

# Initialize database and insert sample data
def init_db():
    conn = get_db_connection()
    if conn is None:
        return
    cursor = conn.cursor()
    
    # Create database if not exists
    cursor.execute('CREATE DATABASE IF NOT EXISTS studentapi')
    cursor.execute('USE studentapi')
    
    # Create tables
    cursor.execute('''CREATE TABLE IF NOT EXISTS students
                    (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), program VARCHAR(255))''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS subjects
                    (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), year INT)''')
    
    # Insert sample students
    students = [
        ('John Doe', 'Software Engineering'),
        ('Jane Smith', 'Software Engineering'),
        ('Alice Johnson', 'Software Engineering'),
        ('Bob Williams', 'Software Engineering'),
        ('Emma Brown', 'Software Engineering'),
        ('Michael Davis', 'Software Engineering'),
        ('Sarah Wilson', 'Software Engineering'),
        ('David Taylor', 'Software Engineering'),
        ('Lisa Anderson', 'Software Engineering'),
        ('James Martinez', 'Software Engineering')
    ]
    cursor.executemany('INSERT IGNORE INTO students (name, program) VALUES (%s, %s)', students)
    
    # Insert sample subjects for Software Engineering program
    subjects = [
        ('Introduction to Programming', 1),
        ('Mathematics for Computing', 1),
        ('Computer Systems', 1),
        ('Data Structures', 2),
        ('Database Systems', 2),
        ('Operating Systems', 2),
        ('Software Engineering Principles', 3),
        ('Web Development', 3),
        ('Mobile Application Development', 3),
        ('Capstone Project', 4),
        ('Cloud Computing', 4),
        ('Artificial Intelligence', 4)
    ]
    cursor.executemany('INSERT IGNORE INTO subjects (name, year) VALUES (%s, %s)', subjects)
    
    conn.commit()
    conn.close()

@app.route('/students', methods=['GET'])
def get_students():
    conn = get_db_connection()
    if conn is None:
        return jsonify({'error': 'Database connection failed'}), 500
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM students')
    students = cursor.fetchall()
    conn.close()
    return jsonify([{'name': student['name'], 'program': student['program']} for student in students])

@app.route('/subjects', methods=['GET'])
def get_subjects():
    conn = get_db_connection()
    if conn is None:
        return jsonify({'error': 'Database connection failed'}), 500
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM subjects ORDER BY year')
    subjects = cursor.fetchall()
    conn.close()
    result = {}
    for subject in subjects:
        year = f"Year {subject['year']}"
        if year not in result:
            result[year] = []
        result[year].append(subject['name'])
    return jsonify(result)

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)