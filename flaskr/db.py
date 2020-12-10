import sqlite3
import click
import emoji
from flask import current_app, g
from flask.cli import with_appcontext


def get_db():
    if 'db' not in g:
        """
        Establishes a connection to the file pointed at by the DATABASE configuration key. 
        This file doesn’t have to exist yet, and won’t until you initialize the database later.
        """
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row
        # Allows access columns by name.

    return g.db


def close_db(e=None) -> None:
    """
    This function will be called after each request to ensure that the connection is closed. Factory function should
    call it.
    :param e:
    :return: None
    """
    db = g.pop('db', None)

    if db is not None:
        db.close()


def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database :rocket:')


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)