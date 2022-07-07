from flask import Flask, request
import sqlite3

app = Flask(__name__)


@app.route('/phones/create/')
def phones_create():
    try:
        conn = sqlite3.connect('phones.db')
        cur = conn.cursor()
        sql = f'''
        INSERT INTO phones
        VALUES ('Viktor', '0504513281');
        '''
        cur.execute(sql)
        conn.commit()
    finally:
        conn.close()

    return 'Phones Create'


@app.route('/phones/read/')
def phones_read():
    try:
        conn = sqlite3.connect('phones.db')
        cur = conn.cursor()
        sql = f'''
        SELECT * FROM phones;
        '''
        cur.execute(sql)
        phones = cur.fetchall()

    finally:
        conn.close()

    return str(phones)


@app.route('/phones/delete/')
def phones_delete():
    try:
        conn = sqlite3.connect('phones.db')
        cur = conn.cursor()
        sql = f'''
        DELETE FROM phones WHERE phone == '0934513285';
        '''
        cur.execute(sql)
        conn.commit()
    finally:
        conn.close()

    return 'Phone Delete'


@app.route('/phones/update/')
def phones_update():
    name = request.args['name']
    phone = request.args['phone']

    try:
        conn = sqlite3.connect('phones.db')
        cur = conn.cursor()
        sql = f'''
        UPDATE phones
        SET phone = '{phone}'
        WHERE ContactName == '{name}';
        '''
        cur.execute(sql)
        conn.commit()
    finally:
        conn.close()

    return 'Phones Update'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)


'''
2. Реализовать CRUD операции для таблицы phones (/phones/create/, /phones/read/, /phones/update/, /phones/delete/)

CRUD
C - Create
R - Read
U - Update
D - Delete
'''
