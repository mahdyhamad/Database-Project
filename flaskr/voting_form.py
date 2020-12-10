import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

bp = Blueprint('vote', __name__, url_prefix='/vote')


@bp.route('/<carId>', methods=['GET', 'POST'])
def vote(carId):
    if request.method == 'GET':
        db = get_db()
        if carId is not None:
            car = db.execute(f'SELECT * FROM car WHERE id = {carId}').fetchall()[0]

            if car is None:
                raise Exception('Please provide a valid Car ID')
            return f"Model: {car['model']}"
