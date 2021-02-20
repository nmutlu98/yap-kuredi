from flask import Flask
from flask_restful import Resource, Api
from flask import jsonify
from flask import render_template

app = Flask(__name__)
api = Api(app)

@app.route('/')
def home():
    return render_template("index.html")
@app.route('/home')
def contact():
    return jsonify({'name':'Necla',
                    'address':'India'})

if __name__ == '__main__':
    app.run(debug=True)
