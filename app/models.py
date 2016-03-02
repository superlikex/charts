#-*-coding:utf-8 -*-
from .  import db
from datetime import datetime

class User(db.Model):
	__tablename = 'users'
	id = db.Column(db.Integer,primary_key=True)
	username = db.Column(db.String(64))
	result   = db.Column(db.Integer, default = 0)
	ballot_time = db.Column(db.DateTime(),default=datetime.utcnow)

	@staticmethod
	def delete_users():
		users = User.query.all()
		for user in users:	
			db.session.delete(user)
		db.session.commit()
			
			
	@staticmethod
	def insert_users():
		users = {
			'李巅峰':0,
			'b':0,
			'c':0,
			'd':0,
			'e':0,
			'f':0,
			'g':0
	}
		for u in users:
			user = User.query.filter_by(username=u).first()
			if user is None:
				user = User(username=u)
			user.result = 0
			db.session.add(user)
		db.session.commit()
			 
	def __repr__(self):
		return '<User %r>'% self.username
