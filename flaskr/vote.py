import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

bp = Blueprint('vote', __name__, url_prefix='/vote')


@bp.route('/<car_id>', methods=['GET', 'POST'])
def vote(car_id):
    db = get_db()
    if car_id is not None:
        car = db.execute(f'SELECT * FROM car WHERE id = {car_id}').fetchall()[0]
        company = db.execute(f'SELECT * FROM company WHERE id = {car["company_id"]}').fetchone()
        if car is None:
            raise Exception('Please provide a valid Car ID')
    if request.method == 'GET':
        return render_template('vote.html', car=car, company=company)
    if request.method == 'POST':
        color_option_id = db.execute('SELECT * FROM option WHERE name = "color"').fetchone()['id']
        is_popular_option_id = db.execute(f'SELECT * FROM option WHERE name="is_popular"').fetchone()['id']
        color = '"'+request.form["color"]+'"'
        popular = '"'+request.form["is_popular"]+'"'
        db.execute(f'INSERT INTO vote(option_id, car_id, vote_value) VALUES({color_option_id}, {car_id}, {color})')
        db.execute(f'INSERT INTO vote(option_id, car_id, vote_value) VALUES({is_popular_option_id}, {car_id}, {popular})')
        db.commit()
        return ("Thanks")
