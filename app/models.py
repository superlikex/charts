#-*-coding:utf-8 -*-
from .  import db
from datetime import datetime
class MQTT_LOG(db.Model):
    __tablename__='mqtt_log'
    id=db.Column(db.Integer,primary_key=True)
    payload = db.Column(db.String)
    topic   = db.Column(db.String)
    msgdate = db.Column(db.Date)
    msgtime = db.Column(db.Time)

    def __repr__(self):
        return '< %r>'%self.value

