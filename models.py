from app import db

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
            'id': self.id, 
            'customer_id': self.customer_id,
            'account_number': self.account_number,
            'customer_number': self.customer_number
        }