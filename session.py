

"""
Code for handling sessions in our web application
"""

from bottle import request, response
import uuid
import json

import model
import dbschema

COOKIE_NAME = 'session'


def get_or_create_session(db):
    """Get the current sessionid either from a
    cookie in the current request or by creating a
    new session if none are present.

    If a new session is created, a cookie is set in the response.

    Returns the session key (string)
    """

    key = request.get_cookie(COOKIE_NAME)
    """gets the cookie and checks if there is data within, if true return else make a cookie with data aka "session"""""
    cur = db.cursor()
    cur.execute("SELECT sessionid FROM sessions WHERE sessionid=?", (key,))
    row = cur.fetchone()
    if not row:
        newkey = str(uuid.uuid4())
        cart = []
        data = json.dumps(cart)
        cur.execute("INSERT INTO sessions VALUES (?, ?)", (newkey, data,))
        db.commit()
        response.set_cookie(COOKIE_NAME, newkey,path="/")
        return newkey

    return key


def add_to_cart(db, itemid, quantity):
    """Add an item to the shopping cart"""
    cart = get_cart_contents(db)
    key = request.get_cookie(COOKIE_NAME)
    cur = db.cursor()
    cur.execute("SELECT id, name, unit_cost FROM products WHERE id=?", (itemid,))
    row = cur.fetchone()
    item = {'id': row['id'], 'name': row['name'], 'quantity': int(quantity), 'cost': row['unit_cost'] * int(quantity)}
    cart.append(item)

    data = json.dumps(cart)
    cur.execute("UPDATE sessions SET data=? WHERE sessionid=?", (data, key,))

def get_cart_contents(db):
    """Return the contents of the shopping cart as
    a list of dictionaries:
    [{'id': <id>, 'quantity': <qty>, 'name': <name>, 'cost': <cost>}, ...]
    """
    key = get_or_create_session(db)
    cur = db.cursor()
    cur.execute("SELECT data FROM sessions WHERE sessionid=?", (key,))
    row = cur.fetchone()
    cart = json.loads(row['data'])
    return cart
