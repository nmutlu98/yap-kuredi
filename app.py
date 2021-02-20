from flask import Flask
from flask_restful import Resource, Api
from flask import jsonify

app = Flask(__name__)
api = Api(app)

@app.route('/')
def home():
    return jsonify({'name':'Jimit',
                    'address':'India'})
@app.route('/home')
def contact():
    return jsonify({'name':'Necla',
                    'address':'India'})

if __name__ == '__main__':
    app.run(debug=True)
