from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

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

@app.route('/students', methods=['GET'])
def get_students():
    students = [
        {"name": "Alice", "program": "Software Engineering"},
        {"name": "Bob", "program": "Computer Science"},
        {"name": "Charlie", "program": "Software Engineering"},
        {"name": "David", "program": "Information Technology"},
        {"name": "Eve", "program": "Cybersecurity"},
        {"name": "Frank", "program": "Data Science"},
        {"name": "Grace", "program": "Artificial Intelligence"},
        {"name": "Hannah", "program": "Machine Learning"},
        {"name": "Ian", "program": "Software Engineering"},
        {"name": "Jack", "program": "Cloud Computing"}
    ]
    return jsonify(students)

@app.route('/subjects', methods=['GET'])
def get_subjects():
    subjects = {
        "Year 1": [
            ("Principles of Programming Languages(CP 111)", 1),
            ("Development Perspectives(DS 102)", 1),
            ("Mathematical Foundations of Information Security-(IA 112)", 1),
            ("Introduction to Information Technology(IT 111)", 1),
            ("Communication Skills(LG 102)", 1),
            ("Discrete Mathematics for ICT(MT1111)", 1),
            ("Calculus(MT 1112)", 1),
            ("Linear Algebra for ICT(MT 1117)", 1),
            ("Introduction to Computer Networking(CN 121)", 1),
            ("Introduction to Database systems(CP 121)", 1),
            ("Introduction to High Level Programming(CP 123)", 1),
            ("Introduction to Software Engineering(CS 123)", 1),
            ("Introduction to IT Security(IA 124)", 1),
            ("Numerical Analysis for ICT(MT 1211)", 1),
            ("Introduction to Probability and Statistics(ST 1210)", 1)
        ],
        "Year 2": [
            ("Computer Networking Protocols(CN 211)", 2),
            ("Introduction To Linux/Unix Systems(CP 211)", 2),
            ("Systems Analysis and Design(CP 212)", 2),
            ("Data Structures and Algorithms Analysis(CP 213)", 2),
            ("Computational Theory(CP 214)", 2),
            ("Object Oriented Programming in Java(CP 215)", 2),
            ("Industrial Practical Training I(CS 131)", 2),
            ("Computer Organization and Architecture I(CT 211)", 2),
            ("Internet Programming And Application I(CP 221)", 2),
            ("Open Source Technologies(CP 222)", 2),
            ("Object-Oriented Systems Design(CP 223)", 2),
            ("Database Management Systems(CP 224)", 2),
            ("Software Testing and Quality Assurance(CP 225)", 2),
            ("Operating Systems(CP 226)", 2),
            ("ICT Research Methods(IS 221)", 2)
        ],
        "Year 3": [
            ("Internet Programming and Applications II(CP 311)", 3),
            ("Python Programming(CP 312)", 3),
            ("Mobile Applications Development(CP 313)", 3),
            ("Selected Topics in Software Engineering(CP 316)", 3),
            ("Computer Graphics(CP 318)", 3),
            ("Industrial Practical Training II(CS 231)", 3),
            ("ICT Entrepreneurship(EME 314)", 3),
            ("Mathematical Logic and Formal Semantics(MT 3111)", 3),
            ("Distributed Database Systems(CP 321)", 3),
            ("Data Mining and Warehousing(CP 322)", 3),
            ("Web Framework Development Using Javascript(CP 323)", 3),
            ("Compiler Technology(CP 324)", 3),
            ("Advanced Java Programming(CS 321)", 3),
            ("Information and Communication Systems Security(IA 321)", 3)
        ],
        "Year 4": [
            ("ICT Project Management(BT 413)", 4),
            ("Distributed Computing(CP 314)", 4),
            ("C# Programming(CP 412)", 4),
            ("Industrial Practical Training III(CS 332)", 4),
            ("Software Reverse Engineering(CS 411)", 4),
            ("Software Engineering Project I(CS 431)", 4),
            ("Computer Maintenance(CT 312)", 4),
            ("Human Computer Interaction(IM 411)", 4),
            ("Professional Ethics and Conduct Core(SI 311)", 4),
            ("Software Deployment and Management(CS 421)", 4),
            ("Big Data Analysis(CS 329)", 4),
            ("Software Engineering Project II(CS 432)", 4),
            ("Artificial Intelligence(CP 422)", 4),
            ("System Administration and Management(CP 423)", 4),
            ("Cloud Computing(CP 424)", 4),
            ("Foundations of Data Science(CG 222)", 4)
        ]
    }

    # Optionally, insert subjects into the database
    for year, subjects_list in subjects.items():
        for subject_name, year_value in subjects_list:
            subject = Subject.query.filter_by(name=subject_name).first()
            if not subject:  # Add subject only if it doesn't exist
                new_subject = Subject(name=subject_name, year=year_value)
                db.session.add(new_subject)
                db.session.commit()

    return jsonify(subjects)
if __name__ == '__main__':
    app.run(debug=True, port=5001)  


with app.app_context():
    db.create_all()
