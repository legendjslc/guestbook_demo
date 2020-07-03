from datetime import datetime

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://ncdcdemo:ncdc2020@192.168.92.190/demo_guestbook'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    comment = db.Column(db.String(1000), nullable=False)
    created = db.Column(db.DateTime(), nullable=False)


@app.route('/')
def index():
    #TODO: list all
    results = []
    return render_template('index.html', result=results)

@app.route('/sign')
def sign():
    return render_template('sign.html')

@app.route('/process', methods=['POST'])
def process():
    #TODO: save comment to db。
    return redirect(url_for('index'))


@app.route('/<name>')
def user(name):
    results = Comments.query.filter_by(name=name).all()

    return render_template('index.html', result=results)


if __name__ == '__main__':
    app.run(debug=True)
