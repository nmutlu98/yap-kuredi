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

class Payment(db.Model):
    __tablename__ = 'transactions'

    id = db.Column(db.Integer, primary_key=True)
    request_id = db.Column(db.Integer)
    sender_name = db.Column(db.String())
    amount = db.Column(db.Integer)

    def __init__(self, id, request_id, sender_name, amount):
        self.id = id
        self.request_id = request_id
        self.sender_name = sender_name
        self.amount = amount

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def serialize(self):
        return {
            'id': self.id,
            'request_id': self.request_id,
            'sender_name': self.sender_name,
            'amount': self.amount
        }

class Request(db.Model):
    __tablename__ = 'transfer_requests'

    customer_id = db.Column(db.Integer)
    amount = db.Column(db.Integer)
    id = db.Column(db.Integer, primary_key=True)
    people_list = db.Column(db.String())

    def __init__(self, customer_id, amount, id, people_list):
        self.customer_id = customer_id
        self.amount = amount
        self.id = id
        self.people_list = people_list

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def serialize(self):
        return {
            'customer_id': self.customer_id,
            'amount' : self.amount,
            'id' : self.id,
            'people_list': self.people_list
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

@app.route("/addPayment")
def add_payment():
    id = request.args.get('id')
    request_id = request.args.get('requestId')
    sender_name = request.args.get('senderName')
    amount = request.args.get('amount')
    
    try:
        payment=Payment(
            id=id,
            request_id=request_id,
            sender_name=sender_name,
            amount=amount
        )
        db.session.add(payment)
        db.session.commit()
        return "Added"
    except Exception as e:
	    return(str(e))

@app.route("/addRequest")
def add_request():
    customer_id = request.args.get('customerId')
    amount = request.args.get('amount')
    id = request.args.get('id')
    people_list = request.args.get('people_list')
    
    try:
        req=Request(
            customer_id=customer_id,
            amount=amount,
            id=id,
            people_list=people_list
        )
        db.session.add(req)
        db.session.commit()
        return "Added"
    except Exception as e:
	    return(str(e))

@app.route("/getallcustomers")
def get_all_customers():
    try:
        customers=Customer.query.all()
        return  jsonify([e.serialize() for e in customers])
    except Exception as e:
	    return(str(e))

@app.route("/getGroupRequestsByCustomerId/<customer_id>")
def get_group_requests(customer_id):
    try:
        requests=Request.query.filter_by(customer_id=customer_id)
        return  jsonify([e.serialize() for e in requests])
    except Exception as e:
	    return(str(e))

@app.route("/getPaymentsByRequest/<request_id>")
def get_payments_by_request(request_id):
    try:
        requests=Payment.query.filter_by(request_id=request_id)
        return  jsonify([e.serialize() for e in requests])
    except Exception as e:
	    return(str(e))

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

