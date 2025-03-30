from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

# MySQL Database Connection
db = mysql.connector.connect(
    host="localhost",  
    user="root",       
    password="mysql",  
    database="studentapi"
)

@app.route('/students', methods=['GET'])
def get_students():
    """Fetch all students with their enrolled programs."""
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT name, program FROM students")  
    students = cursor.fetchall()
    cursor.close()
    return jsonify(students)

@app.route('/subjects', methods=['GET'])
def get_subjects():
    """Fetch all subjects categorized by year."""
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT name, year FROM subjects ORDER BY year ASC")
    subjects = cursor.fetchall()
    cursor.close()

    # Group subjects by academic year
    subjects_by_year = {}
    for subject in subjects:
        year = f"Year {subject['year']}"
        if year not in subjects_by_year:
            subjects_by_year[year] = []
        subjects_by_year[year].append(subject["name"])

    return jsonify(subjects_by_year)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
