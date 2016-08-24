#-*-coding:utf-8-*-
from flask import render_template,session,redirect,url_for,flash,jsonify
import random
from datetime import datetime

from .. import db
from . import main
from ..models import MQTT_LOG


@main.route('/',methods=['GET'])
def index():
 #   test = ORP.query.all()

    return render_template('index.html')

#@main.route('/test',methods=['GET','POST'])
#def test():
#    test = ORP.query.all()
#    return render_template('test.html',test =test)

@main.route('/orp',methods=['GET','POST'])
def orp():
    data = MQTT_LOG.query.filter_by(topic='orp').order_by("id desc").limit(100)#.all()
    return render_template('orp.html',data = data)

@main.route('/orp_temp',methods=['GET','POST'])
def orp_temp():
    data = MQTT_LOG.query.filter_by(topic='orp_temp').order_by("id desc").limit(100)
    return render_template('orp_temp.html',data = data)

@main.route('/ph',methods=['GET','POST'])
def ph():
    data = MQTT_LOG.query.filter_by(topic='ph').order_by("id desc").limit(100)
    return render_template('ph.html',data = data)

#@main.route('/ajax',methods=['GET','POST'])
#def ajax():
   # te = Test.query.all()

  #  return render_template('ajax.html',tt=te[0].id)
