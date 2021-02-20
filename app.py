from flask import Flask
from datetime import datetime
from flask import request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os





app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)



class Customer(db.Model):
    __tablename__ = 'customers'

    customer_id = db.Column(db.Integer, primary_key=True)
    account_number = db.Column(db.String())
    customer_number = db.Column(db.String())

    def __init__(self, customer_id, account_number, customer_number):
        self.customer_id = customer_id
        self.account_number = account_number
        self.customer_number = customer_number

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def serialize(self):
        return {
            'customer_id': self.customer_id,
            'account_number': self.account_number,
            'customer_number': self.customer_number
        }

@app.route('/')
def homepage():
   
    return """
    nice
    """


@app.route('/get')
def get():
    return jsonify({"hello": "world"})

@app.route("/addCustomer")
def add_customer():
    id = request.args.get('customerId')
    account_number = request.args.get('accountNumber')
    customer_number = request.args.get('customerNumber')
    
    try:
        customer=Customer(
            customer_id=id,
            account_number=account_number,
            customer_number=customer_number
        )
        db.session.add(customer)
        db.session.commit()
        return "Added"
    except Exception as e:
	    return(str(e))

@app.route("/getall")
def get_all():
    try:
        customers=Customer.query.all()
        return  jsonify([e.serialize() for e in customers])
    except Exception as e:
	    return(str(e))
if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

