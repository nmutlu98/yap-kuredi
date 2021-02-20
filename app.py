from flask import Flask
from datetime import datetime
from flask import jsonify

app = Flask(__name__)


@app.route('/')
def homepage():
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")

    return """
    <h1>Hello heroku</h1>
    <p>It is currently {time}.</p>

    <img src="http://loremflickr.com/600/400" />
    """.format(time=the_time)


@app.route('/get')
def get():
    return jsonify({"hello": "world"})

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

