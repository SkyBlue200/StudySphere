from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from .models import Physics, Chemistry, Maths
from . import db

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    return render_template("home.html", user=current_user, first_name=current_user.first_name)

@views.route('/test/<subject>')
@login_required
def test(subject):
    subject_classes = {
        'physics': Physics,
        'chemistry': Chemistry,
        'maths': Maths
    }
    questions = subject_classes[subject.lower()].query.all()
    return render_template('test.html',questions = questions, subject=subject, user=current_user)

@views.route('/submit_quiz/<subject>', methods=['POST'])
def submit_quiz(subject):
    subject_classes = {
        'physics': Physics,
        'chemistry': Chemistry,
        'maths': Maths
    }

    subject_model = subject_classes[subject.lower()]
    total_questions = subject_model.query.count()
    score = 0
    incorrect_answers = []

    for question in subject_model.query.all():
        user_answer = request.form.get(f'question_{question.id}')
        if user_answer == question.correct_option:
            score += 1
        else:
            incorrect_answers.append({
                "question": question.question,
                "user_answer": user_answer,
                "correct_answer": question.correct_option
            })

    return render_template('result.html', score=score, subject=subject, total=total_questions, incorrect_answers=incorrect_answers, user=current_user)
