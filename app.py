# pipenv install
    # pipenv shell
# pipenv install flask
# pipenv install gunicorn
    # Gunicorn is a Python Web Server Gateway Interface (WSGI) HTTP server
# pipenv install flask-heroku
# pipenv install flask-cors  
    #turns off cors for this app
# pipenv install psycopg2
    # to work with the postgress
    # attach a cloudbase database to the app
# pipenv install flask-SQLAlchemy
    # help us work with datbases and let us work with shortcuts

from flask import flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_keroku import heroku

app = Flask(__name__)
CORS(app)
app.config[]"SQLALCHEMY_DATABASE_URI"] = 'postgres://zszzroydlztnin:136be58b2fc87e1200f08b667c22e6096b82615e8e610148eaa14d9bff5a1aa9@ec2-107-21-104-31.compute-1.amazonaws.com:5432/d9ee3eptph5vni'

heroku = Heroku(app)
db = SQLAlchemy(app)

class Book(db.Model):
    __tablename__ = 'books' #creating a table for all our information
    id = db.Column(db.Integer, primary_key=True)#each column has a different component from the info
    title = db.Column(db.String(120))#allows 120 characters
    author = db.Column(db.String)

    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def __repr__(self):
        return "<Title %r>" % self.title #the %r means that anything after the second % will get place there 
        # a different way of doing this is f"Title {self.title}

@app.route("/") #home route(will help us tell if our app is working)
def home():
    return"<h1>Hi from Flask</h1>"

@app.route("/book/input", methods=['POST'])
def books_input():
    if request.content_type == 'application/json':
        post_data = request.get_json()
        title = post_data.get('title')
        author = post_data.get('author')
        reg = book(title, author)
        db.session.add(reg)
        db.session.commit()
        return jsonify('Data Posted')
    return jsonify('Something went wrong') #functions as an else

@app.route('/books', methods=["GET"])
def return_books():
    all_books - deb.session.query(Book.id, Book.title, Book.author).all()
    return jsonify(all_books)

@app.route('/books/<id>', methods=['GET'])
def return_single_book(id):
    one_book = db.session.query(Book.id, Book.title, Book.author). filter(book.id == id)first()
    return jsonify(one_book)

@app.route('/delete/<id>', methods=['DELETE'])
def book_delete(id):
    if request.content_type == 'application/json':
        record = db.session.query(Book).get(id)
        db.session.delete(record)
        db.session.commit()
        return jsonify('completed Delete cation')
    return jsonify('Delete failed')

@app.route('/update_book/<id>', methods=['PUT'])
def book_update(id):
    if request.content_type == 'application/json':
        put_data = request.get_json()
        title = put_data.get('title')
        author = put_data.get('author')
        record = db.session.query(Book).get(id)
        record.title = title
        record.author = author
        db.session.commit()
        return jsonify('Completed Update')
    return jsonify('Failed Update')

if __name__ == '__main__':
    app.debug = True
    app.run()