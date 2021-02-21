from flask import Flask
from datetime import datetime
from flask import request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
from token_activate import getAccountTransaction
from flask_cors import CORS, cross_origin

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
@cross_origin()
@app.route('/')
def homepage():
   
    return """
    nice
    """

@cross_origin()
@app.route('/get')
def get():
    response = jsonify({"hello": "world"})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@cross_origin()
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
        response = jsonify({"success" : "true"})
        response.headers.add("Access-Control-Allow-Origin", "*")
        return response
    except Exception as e:
	    return(str(e))

@cross_origin()
@app.route("/getCustomerInfoByCustomerNumber/<customer_number>")
def getCustomerInfoByCustomerNumber(customer_number):
    try:
        customers=Customer.query.filter_by(customer_number)
        response = jsonify([e.serialize for e in customers])
        response.headers.add("Access-Control-Allow-Origin", "*")
        return response
    except Exception as e:
	    return(str(e))

@cross_origin()
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
        response = jsonify({"success" : "true"})
        response.headers.add("Access-Control-Allow-Origin", "*")
        return response
    except Exception as e:
	    return(str(e))

@cross_origin()
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
        response = jsonify({"success" : "true"})
        response.headers.add("Access-Control-Allow-Origin", "*")
        return response
    except Exception as e:
	    return(str(e))

@cross_origin()
@app.route("/getallcustomers")
def get_all_customers():
    try:
        customers=Customer.query.all()
        response = jsonify([e.serialize() for e in customers])
        response.headers.add("Access-Control-Allow-Origin", "*")
        return response
    except Exception as e:
	    return(str(e))

@cross_origin()
@app.route("/getGroupRequestsByCustomerId/<customer_id>")
def get_group_requests(customer_id):
    try:
        requests=Request.query.filter_by(customer_id=customer_id)
        response = jsonify([e.serialize() for e in requests])
        response.headers.add("Access-Control-Allow-Origin", "*")
        return response
    except Exception as e:
	    return(str(e))

@cross_origin()
@app.route("/getTransactions/<account_id>")
def get_transactions_of_account(account_id):
    response = jsonify(getAccountTransaction(account_id))
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response
@cross_origin()
@app.route("/getPaymentsByRequest/<request_id>")
def get_payments_by_request(request_id):
    try:
        requests=Payment.query.filter_by(request_id=request_id)
        response = jsonify([e.serialize() for e in requests])
        response.headers.add("Access-Control-Allow-Origin", "*")
        return response
    except Exception as e:
	    return(str(e))

if __name__ == '__main__':
    app.run(ssl_context='adhoc')

