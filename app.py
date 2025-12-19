from flask import Flask, render_template, request, redirect, session
import sqlite3

app = Flask(__name__)
app.secret_key = "event_secret_key"


def get_db():
    return sqlite3.connect("database.db")


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        pwd = request.form['password']

        db = get_db()
        cur = db.cursor()
        cur.execute(
            "SELECT role FROM users WHERE username=? AND password=?",
            (user, pwd)
        )
        result = cur.fetchone()

        if result:
            session['user'] = user
            session['role'] = result[0]
            return redirect('/dashboard')

    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect('/')
    return render_template('dashboard.html', role=session['role'])


@app.route('/add', methods=['GET', 'POST'])
def add_membership():
    if session.get('role') != 'admin':
        return "Access Denied"

    if request.method == 'POST':
        name = request.form['name']
        duration = request.form['duration']

        db = get_db()
        db.execute(
            "INSERT INTO memberships (name, duration, status) VALUES (?, ?, ?)",
            (name, duration, 'Active')
        )
        db.commit()

    return render_template('add_membership.html')

@app.route('/update', methods=['GET', 'POST'])
def update_membership():
    if session.get('role') != 'admin':
        return "Access Denied"

    if request.method == 'POST':
        mid = request.form['mid']
        action = request.form['action']

        db = get_db()

        if action == 'extend':
            db.execute(
                "UPDATE memberships SET duration = duration + 6 WHERE membership_no=?",
                (mid,)
            )

        elif action == 'cancel':
            db.execute(
                "UPDATE memberships SET status='Cancelled' WHERE membership_no=?",
                (mid,)
            )

        elif action == 'delete':
            db.execute(
                "DELETE FROM memberships WHERE membership_no=?",
                (mid,)
            )

        db.commit()

    return render_template('update_membership.html')


@app.route('/report')
def report():
    if 'user' not in session:
        return redirect('/')

    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT * FROM memberships")
    data = cur.fetchall()

    return render_template('report.html', data=data)


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
