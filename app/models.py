from .  import db
from datetime import datetime

class User(db.Model):
	__tablename = 'users'
	id = db.Column(db.Integer,primary_key=True)
	username = db.Column(db.String(64))
	result   = db.Column(db.Integer, default = 0)
	ballot_time = db.Column(db.DateTime(),default=datetime.utcnow)
	

	def __repr__(self):
		return '<User %r>'% self.username
