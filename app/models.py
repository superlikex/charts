from .  import db
from datetime import datetime

class User(db.Model):
	__tablename = 'users'
	id = db.Column(db.Integer,primary_key=True)
	username = db.Column(db.String(64))

	def __repr__(self):
		return '<User %r>'% self.username
