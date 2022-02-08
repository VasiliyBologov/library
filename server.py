import flask

app = flask.Flask(__name__)


@app.route('/')
def home_page():
    return flask.render_template('home_page.html')

@app.route('/add-book')
def add_book():
    return flask.render_template('add_book.html')

@app.route('/books')
def books():
    return flask.render_template('books.html')


if name == 'main':
    app.run()