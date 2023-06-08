from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from flask_login import current_user, login_required
from .models import FirstFloor, SecondFloor, ThirdFloor, FourthFloor, FifthFloor, SixthFloor, SeventhFloor, EighthFloor, NinthFloor, TenthFloor, EleventhFloor, TwelvethFloor, User
from . import db
from .questions import basic_math_floor, filipino_floor, english_floor, algebra_floor, philosophy_floor, twenty_first_century_floor, social_science_floor, earth_science_floor, bio_floor, chem_floor, calculus_floor, physics_floor
import random

views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    return render_template('index.html')

@views.route('/about-us')
@login_required
def aboutus():
    return render_template('about-us.html')

@views.route('/1st-floor', methods=['GET', 'POST'])
@login_required
def firstfloor():
    user_name = current_user.first_name
    quiz_questions = basic_math_floor[:12]

    score = session.get('score', 0)
    current_question = session.get('current_question', 0)
    enemies = session.get('enemies', len(quiz_questions))  
    health = session.get('health', 5)  # Player health

    if request.method == 'POST':
        selected_choice = request.form.get('choice')

        if selected_choice is None:
            return redirect(url_for('views.firstfloor'))

        correct_choice = int(quiz_questions[current_question]['correct_choice'])

        if int(selected_choice) == correct_choice:
            score += 1
            enemies -= 1
        else:
            # Reduce the number of enemies if the answer is incorrect
            # Reduce the player's health if the answer is incorrect
            health -= 1
            # Check if the number of enemies or the player's health is zero
            if enemies == 0 or health == 0:
                session['score'] = score
                session['current_question'] = current_question
                session['enemies'] = enemies
                session['health'] = health

                # Update the user's score in the database if it's higher than the previous attempt
                user_score = FirstFloor.query.filter_by(user_id=current_user.id).first()
                if user_score and score > user_score.score:
                    user_score.score = score
                elif not user_score:
                    user_score = FirstFloor(score=score, user=current_user)
                    db.session.add(user_score)
                db.session.commit()

                selected_character = session.get('selected_character', '')
                return redirect(url_for('views.result', character=selected_character))

        # Update the enemies and health in the session
        session['enemies'] = enemies
        session['health'] = health

        current_question += 1

        session['score'] = score
        session['current_question'] = current_question

        if current_question < len(quiz_questions):
            return redirect(url_for('views.firstfloor'))
        else:
            # Check if the user already has a score
            user_score = FirstFloor.query.filter_by(user_id=current_user.id).first()
            if user_score and score > user_score.score:
                # Update the existing score if it's higher than the previous attempt
                user_score.score = score
            elif not user_score:
                # Create a new score entry
                user_score = FirstFloor(score=score, user=current_user)
                db.session.add(user_score)
            db.session.commit()

            session.pop('score', None)
            session.pop('current_question', None)
            session.pop('enemies', None)
            session.pop('health', None)
            selected_character = session.get('selected_character', '')

            firstfloor_scores = FirstFloor.query.order_by(FirstFloor.score.desc()).all()
            return render_template('result.html', user_name=user_name, score=score, total_questions=len(quiz_questions), selected_character=selected_character, scores=firstfloor_scores)

    session.pop('score', None)
    session.pop('current_question', None)
    session.pop('enemies', None)
    session.pop('health', None)
    session['score'] = score
    session['current_question'] = current_question
    session['enemies'] = enemies
    session['health'] = health
    selected_character = session.get('selected_character', '')
    return render_template('1stfloor.html', question=quiz_questions[current_question], score=score, user_name=user_name, selected_character=selected_character, enemies=enemies, health=health)

@views.route('/2nd-floor', methods=['GET', 'POST'])
@login_required
def secondfloor():
    user_name = current_user.first_name
    quiz_questions = filipino_floor[:12]

    score = session.get('score', 0)
    current_question = session.get('current_question', 0)
    enemies = session.get('enemies', len(quiz_questions))  # Default enemies is the number of questions
    health = session.get('health', 5)  # Player health

    if request.method == 'POST':
        selected_choice = request.form.get('choice')

        if selected_choice is None:
            return redirect(url_for('views.secondfloor'))

        correct_choice = int(quiz_questions[current_question]['correct_choice'])

        if int(selected_choice) == correct_choice:
            score += 1
            enemies -= 1
        else:
            # Reduce the number of enemies if the answer is incorrect
            # Reduce the player's health if the answer is incorrect
            health -= 1
            # Check if the number of enemies or the player's health is zero
            if enemies == 0 or health == 0:
                session['score'] = score
                session['current_question'] = current_question
                session['enemies'] = enemies
                session['health'] = health

                # Update the user's score in the database if it's higher than the previous attempt
                user_score = SecondFloor.query.filter_by(user_id=current_user.id).first()
                if user_score and score > user_score.score:
                    user_score.score = score
                elif not user_score:
                    user_score = SecondFloor(score=score, user=current_user)
                    db.session.add(user_score)
                db.session.commit()

                selected_character = session.get('selected_character', '')
                return redirect(url_for('views.result', character=selected_character))

        # Update the enemies and health in the session
        session['enemies'] = enemies
        session['health'] = health

        current_question += 1

        session['score'] = score
        session['current_question'] = current_question

        if current_question < len(quiz_questions):
            return redirect(url_for('views.secondfloor'))
        else:
            # Check if the user already has a score
            user_score = SecondFloor.query.filter_by(user_id=current_user.id).first()
            if user_score and score > user_score.score:
                # Update the existing score if it's higher than the previous attempt
                user_score.score = score
            elif not user_score:
                # Create a new score entry
                user_score = SecondFloor(score=score, user=current_user)
                db.session.add(user_score)
            db.session.commit()

            session.pop('score', None)
            session.pop('current_question', None)
            session.pop('enemies', None)
            session.pop('health', None)
            selected_character = session.get('selected_character', '')

            secondfloor_scores = SecondFloor.query.order_by(SecondFloor.score.desc()).all()
            return render_template('result.html', user_name=user_name, score=score, total_questions=len(quiz_questions), selected_character=selected_character, scores=secondfloor_scores)

    session.pop('score', None)
    session.pop('current_question', None)
    session.pop('enemies', None)
    session.pop('health', None)
    session['score'] = score
    session['current_question'] = current_question
    session['enemies'] = enemies
    session['health'] = health
    selected_character = session.get('selected_character', '')
    return render_template('2ndfloor.html', question=quiz_questions[current_question], score=score, user_name=user_name, selected_character=selected_character, enemies=enemies, health=health)

@views.route('/3rd-floor', methods=['GET', 'POST'])
@login_required
def thirdfloor():
    user_name = current_user.first_name
    quiz_questions = english_floor[:12]

    score = session.get('score', 0)
    current_question = session.get('current_question', 0)
    enemies = session.get('enemies', len(quiz_questions))  # Default enemies is the number of questions
    health = session.get('health', 5)  # Player health

    if request.method == 'POST':
        selected_choice = request.form.get('choice')

        if selected_choice is None:
            return redirect(url_for('views.thirdfloor'))

        correct_choice = int(quiz_questions[current_question]['correct_choice'])

        if int(selected_choice) == correct_choice:
            score += 1
            enemies -= 1
        else:
            # Reduce the number of enemies if the answer is incorrect
            # Reduce the player's health if the answer is incorrect
            health -= 1
            # Check if the number of enemies or the player's health is zero
            if enemies == 0 or health == 0:
                session['score'] = score
                session['current_question'] = current_question
                session['enemies'] = enemies
                session['health'] = health

                # Update the user's score in the database if it's higher than the previous attempt
                user_score = ThirdFloor.query.filter_by(user_id=current_user.id).first()
                if user_score and score > user_score.score:
                    user_score.score = score
                elif not user_score:
                    user_score = ThirdFloor(score=score, user=current_user)
                    db.session.add(user_score)
                db.session.commit()

                selected_character = session.get('selected_character', '')
                return redirect(url_for('views.result', character=selected_character))

        # Update the enemies and health in the session
        session['enemies'] = enemies
        session['health'] = health

        current_question += 1

        session['score'] = score
        session['current_question'] = current_question

        if current_question < len(quiz_questions):
            return redirect(url_for('views.thirdfloor'))
        else:
            # Check if the user already has a score
            user_score = ThirdFloor.query.filter_by(user_id=current_user.id).first()
            if user_score and score > user_score.score:
                # Update the existing score if it's higher than the previous attempt
                user_score.score = score
            elif not user_score:
                # Create a new score entry
                user_score = ThirdFloor(score=score, user=current_user)
                db.session.add(user_score)
            db.session.commit()

            session.pop('score', None)
            session.pop('current_question', None)
            session.pop('enemies', None)
            session.pop('health', None)
            selected_character = session.get('selected_character', '')
            thirdfloor_scores = ThirdFloor.query.order_by(ThirdFloor.score.desc()).all()
            return render_template('result.html', user_name=user_name, score=score, total_questions=len(quiz_questions), selected_character=selected_character, scores=thirdfloor_scores)


    session.pop('score', None)
    session.pop('current_question', None)
    session.pop('enemies', None)
    session.pop('health', None)
    session['score'] = score
    session['current_question'] = current_question
    session['enemies'] = enemies
    session['health'] = health
    selected_character = session.get('selected_character', '')
    return render_template('3rdfloor.html', question=quiz_questions[current_question], score=score, user_name=user_name, selected_character=selected_character, enemies=enemies, health=health)

@views.route('/4th-floor', methods=['GET', 'POST'])
@login_required
def fourthfloor():
    user_name = current_user.first_name
    quiz_questions = algebra_floor[:12]

    score = session.get('score', 0)
    current_question = session.get('current_question', 0)
    enemies = session.get('enemies', len(quiz_questions))  
    health = session.get('health', 5)  

    if request.method == 'POST':
        selected_choice = request.form.get('choice')

        if selected_choice is None:
            return redirect(url_for('views.fourthfloor'))

        correct_choice = int(quiz_questions[current_question]['correct_choice'])

        if int(selected_choice) == correct_choice:
            score += 1
            enemies -= 1
        else:
            health -= 1
            if enemies == 0 or health == 0:
                session['score'] = score
                session['current_question'] = current_question
                session['enemies'] = enemies
                session['health'] = health

                user_score = FourthFloor.query.filter_by(user_id=current_user.id).first()
                if user_score and score > user_score.score:
                    user_score.score = score
                elif not user_score:
                    user_score = FourthFloor(score=score, user=current_user)
                    db.session.add(user_score)
                db.session.commit()

                selected_character = session.get('selected_character', '')
                return redirect(url_for('views.result', character=selected_character))


        session['enemies'] = enemies
        session['health'] = health

        current_question += 1

        session['score'] = score
        session['current_question'] = current_question

        if current_question < len(quiz_questions):
            return redirect(url_for('views.fourthfloor'))
        else:
            user_score = FourthFloor.query.filter_by(user_id=current_user.id).first()
            if user_score and score > user_score.score:
                user_score.score = score
            elif not user_score:
                user_score = FourthFloor(score=score, user=current_user)
                db.session.add(user_score)
            db.session.commit()

            session.pop('score', None)
            session.pop('current_question', None)
            session.pop('enemies', None)
            session.pop('health', None)
            selected_character = session.get('selected_character', '')
            fourthfloor_scores = FourthFloor.query.order_by(FourthFloor.score.desc()).all()
            return render_template('result.html', user_name=user_name, score=score, total_questions=len(quiz_questions), selected_character=selected_character, scores=fourthfloor_scores)

    session.pop('score', None)
    session.pop('current_question', None)
    session.pop('enemies', None)
    session.pop('health', None)
    session['score'] = score
    session['current_question'] = current_question
    session['enemies'] = enemies
    session['health'] = health
    selected_character = session.get('selected_character', '')
    return render_template('4thfloor.html', question=quiz_questions[current_question], score=score, user_name=user_name, selected_character=selected_character, enemies=enemies, health=health)

@views.route('/5th-floor', methods=['GET', 'POST'])
@login_required
def fifthfloor():
    user_name = current_user.first_name
    quiz_questions = philosophy_floor[:12]

    score = session.get('score', 0)
    current_question = session.get('current_question', 0)
    enemies = session.get('enemies', len(quiz_questions))  
    health = session.get('health', 5)  

    if request.method == 'POST':
        selected_choice = request.form.get('choice')

        if selected_choice is None:
            return redirect(url_for('views.fifthfloor'))

        correct_choice = int(quiz_questions[current_question]['correct_choice'])

        if int(selected_choice) == correct_choice:
            score += 1
            enemies -= 1
        else:
            health -= 1
            if enemies == 0 or health == 0:
                session['score'] = score
                session['current_question'] = current_question
                session['enemies'] = enemies
                session['health'] = health

                user_score = FifthFloor.query.filter_by(user_id=current_user.id).first()
                if user_score and score > user_score.score:
                    user_score.score = score
                elif not user_score:
                    user_score = FifthFloor(score=score, user=current_user)
                    db.session.add(user_score)
                db.session.commit()

                selected_character = session.get('selected_character', '')
                return redirect(url_for('views.result', character=selected_character))


        session['enemies'] = enemies
        session['health'] = health

        current_question += 1

        session['score'] = score
        session['current_question'] = current_question

        if current_question < len(quiz_questions):
            return redirect(url_for('views.fifthfloor'))
        else:
            user_score = FifthFloor.query.filter_by(user_id=current_user.id).first()
            if user_score and score > user_score.score:
                user_score.score = score
            elif not user_score:
                user_score = FifthFloor(score=score, user=current_user)
                db.session.add(user_score)
            db.session.commit()

            session.pop('score', None)
            session.pop('current_question', None)
            session.pop('enemies', None)
            session.pop('health', None)
            selected_character = session.get('selected_character', '')
            fifthfloor_scores = FifthFloor.query.order_by(FifthFloor.score.desc()).all()
            return render_template('result.html', user_name=user_name, score=score, total_questions=len(quiz_questions), selected_character=selected_character, scores=fifthfloor_scores)


    session.pop('score', None)
    session.pop('current_question', None)
    session.pop('enemies', None)
    session.pop('health', None)
    session['score'] = score
    session['current_question'] = current_question
    session['enemies'] = enemies
    session['health'] = health
    selected_character = session.get('selected_character', '')
    return render_template('5thfloor.html', question=quiz_questions[current_question], score=score, user_name=user_name, selected_character=selected_character, enemies=enemies, health=health)

@views.route('/6th-floor', methods=['GET', 'POST'])
@login_required
def sixthfloor():
    user_name = current_user.first_name
    quiz_questions = twenty_first_century_floor[:12]

    score = session.get('score', 0)
    current_question = session.get('current_question', 0)
    enemies = session.get('enemies', len(quiz_questions))  
    health = session.get('health', 5)  

    if request.method == 'POST':
        selected_choice = request.form.get('choice')

        if selected_choice is None:
            return redirect(url_for('views.sixthfloor'))

        correct_choice = int(quiz_questions[current_question]['correct_choice'])

        if int(selected_choice) == correct_choice:
            score += 1
            enemies -= 1
        else:
            health -= 1
            if enemies == 0 or health == 0:
                session['score'] = score
                session['current_question'] = current_question
                session['enemies'] = enemies
                session['health'] = health

                user_score = SixthFloor.query.filter_by(user_id=current_user.id).first()
                if user_score and score > user_score.score:
                    user_score.score = score
                elif not user_score:
                    user_score = SixthFloor(score=score, user=current_user)
                    db.session.add(user_score)
                db.session.commit()

                selected_character = session.get('selected_character', '')
                return redirect(url_for('views.result', character=selected_character))


        session['enemies'] = enemies
        session['health'] = health

        current_question += 1

        session['score'] = score
        session['current_question'] = current_question

        if current_question < len(quiz_questions):
            return redirect(url_for('views.sixthfloor'))
        else:
            user_score = SixthFloor.query.filter_by(user_id=current_user.id).first()
            if user_score and score > user_score.score:
                user_score.score = score
            elif not user_score:
                user_score = SixthFloor(score=score, user=current_user)
                db.session.add(user_score)
            db.session.commit()

            session.pop('score', None)
            session.pop('current_question', None)
            session.pop('enemies', None)
            session.pop('health', None)
            selected_character = session.get('selected_character', '')
            sixthfloor_scores = SixthFloor.query.order_by(SixthFloor.score.desc()).all()
            return render_template('result.html', user_name=user_name, score=score, total_questions=len(quiz_questions), selected_character=selected_character, scores=sixthfloor_scores)

    session.pop('score', None)
    session.pop('current_question', None)
    session.pop('enemies', None)
    session.pop('health', None)
    session['score'] = score
    session['current_question'] = current_question
    session['enemies'] = enemies
    session['health'] = health
    selected_character = session.get('selected_character', '')
    return render_template('6thfloor.html', question=quiz_questions[current_question], score=score, user_name=user_name, selected_character=selected_character, enemies=enemies, health=health)

@views.route('/7th-floor', methods=['GET', 'POST'])
@login_required
def seventhfloor():
    user_name = current_user.first_name
    quiz_questions = social_science_floor[:12]

    score = session.get('score', 0)
    current_question = session.get('current_question', 0)
    enemies = session.get('enemies', len(quiz_questions))  
    health = session.get('health', 5)  

    if request.method == 'POST':
        selected_choice = request.form.get('choice')

        if selected_choice is None:
            return redirect(url_for('views.seventhfloor'))

        correct_choice = int(quiz_questions[current_question]['correct_choice'])

        if int(selected_choice) == correct_choice:
            score += 1
            enemies -= 1
        else:
            health -= 1
            if enemies == 0 or health == 0:
                session['score'] = score
                session['current_question'] = current_question
                session['enemies'] = enemies
                session['health'] = health

                user_score = SeventhFloor.query.filter_by(user_id=current_user.id).first()
                if user_score and score > user_score.score:
                    user_score.score = score
                elif not user_score:
                    user_score = SeventhFloor(score=score, user=current_user)
                    db.session.add(user_score)
                db.session.commit()

                selected_character = session.get('selected_character', '')
                return redirect(url_for('views.result', character=selected_character))


        session['enemies'] = enemies
        session['health'] = health

        current_question += 1

        session['score'] = score
        session['current_question'] = current_question

        if current_question < len(quiz_questions):
            return redirect(url_for('views.seventhfloor'))
        else:
            user_score = SeventhFloor.query.filter_by(user_id=current_user.id).first()
            if user_score and score > user_score.score:
                user_score.score = score
            elif not user_score:
                user_score = SeventhFloor(score=score, user=current_user)
                db.session.add(user_score)
            db.session.commit()

            session.pop('score', None)
            session.pop('current_question', None)
            session.pop('enemies', None)
            session.pop('health', None)
            selected_character = session.get('selected_character', '')
            seventhfloor_scores = SeventhFloor.query.order_by(SeventhFloor.score.desc()).all()
            return render_template('result.html', user_name=user_name, score=score, total_questions=len(quiz_questions), selected_character=selected_character, scores=seventhfloor_scores)

    session.pop('score', None)
    session.pop('current_question', None)
    session.pop('enemies', None)
    session.pop('health', None)
    session['score'] = score
    session['current_question'] = current_question
    session['enemies'] = enemies
    session['health'] = health
    selected_character = session.get('selected_character', '')
    return render_template('7thfloor.html', question=quiz_questions[current_question], score=score, user_name=user_name, selected_character=selected_character, enemies=enemies, health=health)

@views.route('8th-floor', methods=['GET', 'POST'])
@login_required
def eightfloor():
    user_name = current_user.first_name
    quiz_questions = earth_science_floor[:12]

    score = session.get('score', 0)
    current_question = session.get('current_question', 0)
    enemies = session.get('enemies', len(quiz_questions))  
    health = session.get('health', 5)  

    if request.method == 'POST':
        selected_choice = request.form.get('choice')

        if selected_choice is None:
            return redirect(url_for('views.eightfloor'))

        correct_choice = int(quiz_questions[current_question]['correct_choice'])

        if int(selected_choice) == correct_choice:
            score += 1
            enemies -= 1
        else:
            health -= 1
            if enemies == 0 or health == 0:
                session['score'] = score
                session['current_question'] = current_question
                session['enemies'] = enemies
                session['health'] = health

                user_score = EighthFloor.query.filter_by(user_id=current_user.id).first()
                if user_score and score > user_score.score:
                    user_score.score = score
                elif not user_score:
                    user_score = EighthFloor(score=score, user=current_user)
                    db.session.add(user_score)
                db.session.commit()

                selected_character = session.get('selected_character', '')
                return redirect(url_for('views.result', character=selected_character))


        session['enemies'] = enemies
        session['health'] = health

        current_question += 1

        session['score'] = score
        session['current_question'] = current_question

        if current_question < len(quiz_questions):
            return redirect(url_for('views.eightfloor'))
        else:
            user_score = EighthFloor.query.filter_by(user_id=current_user.id).first()
            if user_score and score > user_score.score:
                user_score.score = score
            elif not user_score:
                user_score = EighthFloor(score=score, user=current_user)
                db.session.add(user_score)
            db.session.commit()

            session.pop('score', None)
            session.pop('current_question', None)
            session.pop('enemies', None)
            session.pop('health', None)
            selected_character = session.get('selected_character', '')
            eighthfloor_scores = EighthFloor.query.order_by(EighthFloor.score.desc()).all()
            return render_template('result.html', user_name=user_name, score=score, total_questions=len(quiz_questions), selected_character=selected_character, scores=eighthfloor_scores)

    session.pop('score', None)
    session.pop('current_question', None)
    session.pop('enemies', None)
    session.pop('health', None)
    session['score'] = score
    session['current_question'] = current_question
    session['enemies'] = enemies
    session['health'] = health
    selected_character = session.get('selected_character', '')
    return render_template('8thfloor.html', question=quiz_questions[current_question], score=score, user_name=user_name, selected_character=selected_character, enemies=enemies, health=health)

@views.route('/9th-floor', methods=['GET', 'POST'])
@login_required
def ninthfloor():
    user_name = current_user.first_name
    quiz_questions = bio_floor[:12]

    score = session.get('score', 0)
    current_question = session.get('current_question', 0)
    enemies = session.get('enemies', len(quiz_questions))  
    health = session.get('health', 5)  

    if request.method == 'POST':
        selected_choice = request.form.get('choice')

        if selected_choice is None:
            return redirect(url_for('views.ninthfloor'))

        correct_choice = int(quiz_questions[current_question]['correct_choice'])

        if int(selected_choice) == correct_choice:
            score += 1
            enemies -= 1
        else:
            health -= 1
            if enemies == 0 or health == 0:
                session['score'] = score
                session['current_question'] = current_question
                session['enemies'] = enemies
                session['health'] = health

                user_score = NinthFloor.query.filter_by(user_id=current_user.id).first()
                if user_score and score > user_score.score:
                    user_score.score = score
                elif not user_score:
                    user_score = NinthFloor(score=score, user=current_user)
                    db.session.add(user_score)
                db.session.commit()

                selected_character = session.get('selected_character', '')
                return redirect(url_for('views.result', character=selected_character))


        session['enemies'] = enemies
        session['health'] = health

        current_question += 1

        session['score'] = score
        session['current_question'] = current_question

        if current_question < len(quiz_questions):
            return redirect(url_for('views.ninthfloor'))
        else:
            user_score = NinthFloor.query.filter_by(user_id=current_user.id).first()
            if user_score and score > user_score.score:
                user_score.score = score
            elif not user_score:
                user_score = NinthFloor(score=score, user=current_user)
                db.session.add(user_score)
            db.session.commit()

            session.pop('score', None)
            session.pop('current_question', None)
            session.pop('enemies', None)
            session.pop('health', None)
            selected_character = session.get('selected_character', '')
            ninthfloor_scores = NinthFloor.query.order_by(NinthFloor.score.desc()).all()
            return render_template('result.html', user_name=user_name, score=score, total_questions=len(quiz_questions), selected_character=selected_character, scores=ninthfloor_scores)

    session.pop('score', None)
    session.pop('current_question', None)
    session.pop('enemies', None)
    session.pop('health', None)
    session['score'] = score
    session['current_question'] = current_question
    session['enemies'] = enemies
    session['health'] = health
    selected_character = session.get('selected_character', '')
    return render_template('9thfloor.html', question=quiz_questions[current_question], score=score, user_name=user_name, selected_character=selected_character, enemies=enemies, health=health)

@views.route('/10th-floor', methods=['GET', 'POST'])
@login_required
def tenthfloor():
    user_name = current_user.first_name
    quiz_questions = chem_floor[:12]

    score = session.get('score', 0)
    current_question = session.get('current_question', 0)
    enemies = session.get('enemies', len(quiz_questions))  
    health = session.get('health', 5)  

    if request.method == 'POST':
        selected_choice = request.form.get('choice')

        if selected_choice is None:
            return redirect(url_for('views.tenthfloor'))

        correct_choice = int(quiz_questions[current_question]['correct_choice'])

        if int(selected_choice) == correct_choice:
            score += 1
            enemies -= 1
        else:
            health -= 1
            if enemies == 0 or health == 0:
                session['score'] = score
                session['current_question'] = current_question
                session['enemies'] = enemies
                session['health'] = health

                user_score = TenthFloor.query.filter_by(user_id=current_user.id).first()
                if user_score and score > user_score.score:
                    user_score.score = score
                elif not user_score:
                    user_score = TenthFloor(score=score, user=current_user)
                    db.session.add(user_score)
                db.session.commit()

                selected_character = session.get('selected_character', '')
                return redirect(url_for('views.result', character=selected_character))


        session['enemies'] = enemies
        session['health'] = health

        current_question += 1

        session['score'] = score
        session['current_question'] = current_question

        if current_question < len(quiz_questions):
            return redirect(url_for('views.tenthfloor'))
        else:
            user_score = TenthFloor.query.filter_by(user_id=current_user.id).first()
            if user_score and score > user_score.score:
                user_score.score = score
            elif not user_score:
                user_score = TenthFloor(score=score, user=current_user)
                db.session.add(user_score)
            db.session.commit()

            session.pop('score', None)
            session.pop('current_question', None)
            session.pop('enemies', None)
            session.pop('health', None)
            selected_character = session.get('selected_character', '')
            tenthfloor_scores = TenthFloor.query.order_by(TenthFloor.score.desc()).all()
            return render_template('result.html', user_name=user_name, score=score, total_questions=len(quiz_questions), selected_character=selected_character, scores=tenthfloor_scores)

    session.pop('score', None)
    session.pop('current_question', None)
    session.pop('enemies', None)
    session.pop('health', None)
    session['score'] = score
    session['current_question'] = current_question
    session['enemies'] = enemies
    session['health'] = health
    selected_character = session.get('selected_character', '')
    return render_template('10thfloor.html', question=quiz_questions[current_question], score=score, user_name=user_name, selected_character=selected_character, enemies=enemies, health=health)

@views.route('/11th-floor', methods=['GET', 'POST'])
@login_required
def eleventhfloor():
    user_name = current_user.first_name
    quiz_questions = calculus_floor[:12]

    score = session.get('score', 0)
    current_question = session.get('current_question', 0)
    enemies = session.get('enemies', len(quiz_questions))  
    health = session.get('health', 5)  

    if request.method == 'POST':
        selected_choice = request.form.get('choice')

        if selected_choice is None:
            return redirect(url_for('views.eleventhfloor'))

        correct_choice = int(quiz_questions[current_question]['correct_choice'])

        if int(selected_choice) == correct_choice:
            score += 1
            enemies -= 1
        else:
            health -= 1
            if enemies == 0 or health == 0:
                session['score'] = score
                session['current_question'] = current_question
                session['enemies'] = enemies
                session['health'] = health

                user_score = EleventhFloor.query.filter_by(user_id=current_user.id).first()
                if user_score and score > user_score.score:
                    user_score.score = score
                elif not user_score:
                    user_score = EleventhFloor(score=score, user=current_user)
                    db.session.add(user_score)
                db.session.commit()

                selected_character = session.get('selected_character', '')
                return redirect(url_for('views.result', character=selected_character))


        session['enemies'] = enemies
        session['health'] = health

        current_question += 1

        session['score'] = score
        session['current_question'] = current_question

        if current_question < len(quiz_questions):
            return redirect(url_for('views.eleventhfloor'))
        else:
            user_score = EleventhFloor.query.filter_by(user_id=current_user.id).first()
            if user_score and score > user_score.score:
                user_score.score = score
            elif not user_score:
                user_score = EleventhFloor(score=score, user=current_user)
                db.session.add(user_score)
            db.session.commit()

            session.pop('score', None)
            session.pop('current_question', None)
            session.pop('enemies', None)
            session.pop('health', None)
            selected_character = session.get('selected_character', '')
            eleventhfloor_scores = EleventhFloor.query.order_by(EleventhFloor.score.desc()).all()
            return render_template('result.html', user_name=user_name, score=score, total_questions=len(quiz_questions), selected_character=selected_character, scores=eleventhfloor_scores)

    session.pop('score', None)
    session.pop('current_question', None)
    session.pop('enemies', None)
    session.pop('health', None)
    session['score'] = score
    session['current_question'] = current_question
    session['enemies'] = enemies
    session['health'] = health
    selected_character = session.get('selected_character', '')
    return render_template('11thfloor.html', question=quiz_questions[current_question], score=score, user_name=user_name, selected_character=selected_character, enemies=enemies, health=health)

@views.route('/12th-floor', methods=['GET', 'POST'])
@login_required
def twelvethfloor():
    user_name = current_user.first_name
    quiz_questions = physics_floor[:12]

    score = session.get('score', 0)
    current_question = session.get('current_question', 0)
    enemies = session.get('enemies', len(quiz_questions))  
    health = session.get('health', 5)  

    if request.method == 'POST':
        selected_choice = request.form.get('choice')

        if selected_choice is None:
            return redirect(url_for('views.twelvethfloor'))

        correct_choice = int(quiz_questions[current_question]['correct_choice'])

        if int(selected_choice) == correct_choice:
            score += 1
            enemies -= 1
        else:
            health -= 1
            if enemies == 0 or health == 0:
                session['score'] = score
                session['current_question'] = current_question
                session['enemies'] = enemies
                session['health'] = health

                user_score = TwelvethFloor.query.filter_by(user_id=current_user.id).first()
                if user_score and score > user_score.score:
                    user_score.score = score
                elif not user_score:
                    user_score = TwelvethFloor(score=score, user=current_user)
                    db.session.add(user_score)
                db.session.commit()

                selected_character = session.get('selected_character', '')
                return redirect(url_for('views.result', character=selected_character))


        session['enemies'] = enemies
        session['health'] = health

        current_question += 1

        session['score'] = score
        session['current_question'] = current_question

        if current_question < len(quiz_questions):
            return redirect(url_for('views.twelvethfloor'))
        else:
            user_score = TwelvethFloor.query.filter_by(user_id=current_user.id).first()
            if user_score and score > user_score.score:
                user_score.score = score
            elif not user_score:
                user_score = TwelvethFloor(score=score, user=current_user)
                db.session.add(user_score)
            db.session.commit()

            session.pop('score', None)
            session.pop('current_question', None)
            session.pop('enemies', None)
            session.pop('health', None)
            selected_character = session.get('selected_character', '')
            twelvethfloor_scores = TwelvethFloor.query.order_by(TwelvethFloor.score.desc()).all()
            return render_template('result.html', user_name=user_name, score=score, total_questions=len(quiz_questions), selected_character=selected_character, scores=twelvethfloor_scores)

    session.pop('score', None)
    session.pop('current_question', None)
    session.pop('enemies', None)
    session.pop('health', None)
    session['score'] = score
    session['current_question'] = current_question
    session['enemies'] = enemies
    session['health'] = health
    selected_character = session.get('selected_character', '')
    return render_template('12thfloor.html', question=quiz_questions[current_question], score=score, user_name=user_name, selected_character=selected_character, enemies=enemies, health=health)

@views.route('/leaderboard')
@login_required
def leaderboard():
    user_scores = {}

    floors = [SecondFloor, FirstFloor, ThirdFloor, FourthFloor, FifthFloor, SixthFloor, SeventhFloor, EighthFloor, NinthFloor]
    for floor in floors:
        scores = floor.query.order_by(floor.score.desc()).all()
        for score in scores:
            user = score.user
            user_id = user.id
            if user_id in user_scores:
                user_scores[user_id]['score'] += score.score
            else:
                user_scores[user_id] = {'user': user, 'score': score.score}

    sorted_scores = sorted(user_scores.values(), key=lambda x: x['score'], reverse=True)

    return render_template('leaderboard.html', scores=sorted_scores)


@views.route('/delete_score/<int:score_id>', methods=['POST'])
def delete_score(score_id):
    score = SecondFloor.query.get_or_404(score_id)
    db.session.delete(score)
    db.session.commit()
    flash('Score deleted successfully', 'success')
    return redirect(url_for('views.leaderboard'))

@views.route('/select-character', methods=['GET', 'POST'])
@login_required
def select_character():
    if request.method == 'POST':
        selected_character = request.form.get('character')

        if not selected_character:
            flash('Please select a character', 'error')
            return redirect(url_for('views.select_character'))

        session['selected_character'] = selected_character

        return render_template('story1.html')

    return render_template('character.html')

@views.route('/floors')
@login_required
def select_floor():
    return render_template('floor.html')


#@views.route('/all-floors')
#@login_required
#def all_floors():
#   user_name = current_user.first_name
#    first_floor_score = Score.query.filter_by(user_id=current_user.id).first()
#    second_floor_score = Score.query.filter_by(user_id=current_user.id).first()
#    return render_template('all_floors.html', user_name=user_name, first_floor_score=first_floor_score, second_floor_score=second_floor_score)

