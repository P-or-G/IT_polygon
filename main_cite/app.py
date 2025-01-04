from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Пример данных
users = [{"name": "Alice", "role": "teacher"}, {"name": "Bob", "role": "student"}]
courses = [
    {"id": 1, "title": "Python Basics", "description": "Learn Python from scratch."},
    {"id": 2, "title": "Advanced Python", "description": "Deep dive into Python."}
]

@app.route('/')
def index():
    return render_template('index.html', courses=courses)


@app.route('/courses')
def show_courses():
    return render_template('courses.html', courses=courses)


@app.route('/course/<int:course_id>')
def course_detail(course_id):
    course = next((c for c in courses if c['id'] == course_id), None)
    if course:
        return render_template('course_detail.html', course=course)
    return "Course not found", 404


@app.route('/users')
def show_users():
    return render_template('user.html', users=users)


if __name__ == '__main__':
    app.run(debug=True)
