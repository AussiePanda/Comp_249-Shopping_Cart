
import random
from bottle import Bottle, template, static_file, request, redirect, HTTPError

import model
import session

app = Bottle()

"""route address"""
@app.route('/')
def index(db):
    session.get_or_create_session(db)
    data = model.product_list(db)
    info = {
        'title': ' The WT Store',
        'data': data,
    }
    return template('index', info,)

""" our cart page with form already processed and template filled"""
@app.route('/cart', method="GET")
def index(db):
    session.get_or_create_session(db)
    data = session.get_cart_contents(db)
    cost = 0
    for x in data:
        temp = x['cost']
        cost += temp
    info = {
        'title': 'Current Shopping Cart Contents',
        'data': data,
        'cost': cost
    }
    return template('cart',info)

"""cart processing from form"""
@app.route('/cart', method="POST")
def index(db):
    session.get_or_create_session(db)
    productid = request.forms.get("product")
    quantity = request.forms.get("quantity")
    session.add_to_cart(db,productid,quantity)
    session.get_or_create_session(db)
    redirect('/cart')

@app.route('/static/<filename:path>')
def static(filename):
    return static_file(filename=filename, root='static')

if __name__ == '__main__':
    from bottle.ext import sqlite
    from dbschema import DATABASE_NAME
    # install the database plugin
    app.install(sqlite.Plugin(dbfile=DATABASE_NAME))
    app.run(debug=True, port=8010)

#########################################
###############producct pages ###########
@app.route('/product/0')
def index(db,id):
    session.get_or_create_session(db)

    data = model.product_get(db, id)
    info = {
        'data': data
    }
    return template('product_page', info)

@app.route('/product/1')
def index(db):
    session.get_or_create_session(db)
    data = model.product_get(db,1)
    info = {
        'data': data
    }
    return template('product_page',info)

@app.route('/product/2')
def index(db):
    session.get_or_create_session(db)
    data = model.product_get(db,2)
    info = {
        'data': data
    }
    return template('product_page',info)

@app.route('/product/3')
def index(db):
    session.get_or_create_session(db)
    data = model.product_get(db,3)
    info = {
        'data': data
    }
    return template('product_page',info)

@app.route('/product/4')
def index(db):
    session.get_or_create_session(db)
    data = model.product_get(db,4)
    info = {
        'data': data
    }
    return template('product_page',info)

@app.route('/product/5')
def index(db):
    session.get_or_create_session(db)
    data = model.product_get(db,5)
    info = {
        'data': data
    }
    return template('product_page',info)

@app.route('/product/6')
def index(db):
    session.get_or_create_session(db)
    data = model.product_get(db,6)
    info = {
        'data': data
    }
    return template('product_page',info)

@app.route('/product/7')
def index(db):
    session.get_or_create_session(db)
    data = model.product_get(db,7)
    info = {
        'data': data
    }
    return template('product_page',info)

@app.route('/product/8')
def index(db):
    session.get_or_create_session(db)
    data = model.product_get(db,8)
    info = {
        'data': data
    }
    return template('product_page',info)

@app.route('/product/9')
def index(db):
    session.get_or_create_session(db)
    data = model.product_get(db,9)
    info = {
        'data': data
    }
    return template('product_page',info)

@app.route('/product/10')
def index(db):
    session.get_or_create_session(db)
    data = model.product_get(db,10)
    info = {
        'data': data
    }
    return template('product_page',info)

@app.route('/product/11')
def index(db):
    session.get_or_create_session(db)
    data = model.product_get(db,11)
    info = {
        'data': data
    }
    return template('product_page',info)

@app.route('/product/12')
def index(db):
    session.get_or_create_session(db)
    data = model.product_get(db,12)
    info = {
        'data': data
    }
    return template('product_page',info)

@app.route('/product/13')
def index(db):
    session.get_or_create_session(db)
    data = model.product_get(db,13)
    info = {
        'data': data
    }
    return template('product_page',info)

@app.route('/product/14')
def index(db):
    session.get_or_create_session(db)
    data = model.product_get(db,14)
    info = {
        'data': data
    }
    return template('product_page',info)

@app.route('/product/15')
def index(db):
    session.get_or_create_session(db)
    data = model.product_get(db,15)
    info = {
        'data': data
    }
    return template('product_page',info)
@app.route('/product/16')
def index(db):
    session.get_or_create_session(db)
    data = model.product_get(db,16)
    info = {
        'data': data
    }
    return template('product_page',info)

@app.route('/product/17')
def index(db):
    session.get_or_create_session(db)
    data = model.product_get(db,17)
    info = {
        'data': data
    }
    return template('product_page',info)

@app.route('/product/18')
def index(db):
    session.get_or_create_session(db)
    data = model.product_get(db,18)
    info = {
        'data': data
    }
    return template('product_page',info)

@app.route('/product/19')
def index(db):
    session.get_or_create_session(db)
    data = model.product_get(db,19)
    info = {
        'data': data
    }
    return template('product_page',info)

