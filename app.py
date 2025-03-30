from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

# Set MySQL database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mysql@localhost/studentapi'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define Subject Model
class Subject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    year = db.Column(db.Integer, nullable=False)

# Define Student Model
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    program = db.Column(db.String(100), nullable=False)

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
