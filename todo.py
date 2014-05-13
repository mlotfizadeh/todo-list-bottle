import os
import sqlite3
from bottle import Bottle, run, route, template, request

DATABASE = 'todo.db'

app = Bottle()

@app.route('/')
def hello_world():
    return template('index')

@app.route('/todo')
def todo_list():
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute("SELECT id, task FROM todo WHERE status = 1")
    result = cur.fetchall()
    conn.close()
    return template('make_table', rows=result)

@app.route('/new')
def new_item():
    return template('new_task.tpl')

@app.route('/new', method='POST')
def insert_new_item():
    new_task = request.forms.get('task').encode('latin1').decode('utf8')
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute("INSERT INTO todo (task, status) VALUES (?, ?)", (new_task, 1))
    new_id = cur.lastrowid
    conn.commit()
    conn.close()
    return ('<p>The new task was inserted into the database, the ID is %s</p>'
            % new_id)

@app.route('/edit/<idx>')
def get_item(idx):
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute("SELECT task, status FROM todo WHERE id = ?", (idx))
    cur_data = cur.fetchone()
    conn.close()
    return template('edit_task', task=cur_data[0], status=cur_data[1], no=idx)

@app.route('/edit/<idx>', method='POST')
def edit_item(idx):
    task = request.forms.get('task').encode('latin1').decode('utf8')
    status = request.forms.get('status')
    if status == 'open':
        status = 1
    else:
        status = 0
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute("UPDATE todo SET task = ?, status = ? WHERE id = ?",
            (task, status, idx))
    conn.commit()
    conn.close()
    return '<p>The item number %s was seccessfully updated</p>' % idx

run(app, host='0.0.0.0', port=os.environ.get('PORT', 5000))
