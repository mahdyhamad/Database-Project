
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from flaskr.db import get_db

bp = Blueprint("index", __name__, url_prefix="/")


@bp.route('/', methods=['GET'])
def index():
    db = get_db()

    most_popular_color = dict(db.execute("SELECT *, COUNT(*) as 'count' FROM vote WHERE vote.option_id=2 GROUP BY vote.vote_value, vote.car_id ORDER BY COUNT(*) DESC LIMIT 1").fetchall()[0])
    
    most_popular_color['car'] = db.execute(f"SELECT * from car WHERE car.id={most_popular_color['car_id']}").fetchone()
    most_popular_color['logo_url'] = db.execute(f"SELECT logo_url from company where company.id={most_popular_color['car']['company_id']}").fetchone()['logo_url']

    most_popular_car = dict(
        db.execute("SELECT *, COUNT(*) as 'count' FROM vote WHERE vote.vote_value='1' GROUP BY vote.vote_value, vote.car_id ORDER BY COUNT(*) DESC LIMIT 1").fetchone())

    most_popular_car['car'] = db.execute(f"SELECT * from car WHERE car.id={most_popular_car['car_id']}").fetchone()
    most_popular_car['logo_url'] = db.execute(f"SELECT logo_url from company where company.id={most_popular_car['car']['company_id']}").fetchone()['logo_url']

    cars = db.execute("SELECT * from car").fetchall()

    return render_template('index.html', color=most_popular_color, most_popular=most_popular_car, cars=cars, pageUrl="/")
