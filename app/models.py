from app.database import db

class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    balance = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Account {self.name} - Balance: {self.balance}>'

class Transfer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    source_account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    target_account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Transfer {self.source_account_id} -> {self.target_account_id}: ${self.amount}>'
