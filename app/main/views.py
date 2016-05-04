from flask import render_template,session,redirect,url_for,flash
import random
from datetime import datetime

from .. import db
from . import main
from .forms import NameForm
from ..models import User


@main.route('/',methods=['GET','POST'])
def index():
#	user = User.query.get(id)
#	form = NameForm(request.Post,obj=user)
	form = NameForm()
#	user = User.query.get(id)
#	form.group_id.choices= [(g.id,g.username) for g in User]
#	form.group_id.choices += [(g.id,g.username) for g in User]
	if form.validate_on_submit():
		session['group_id'] = form.group_id.data
		return redirect(url_for('.result',group_id = session.get('group_id')))
	history = User.query.order_by(User.ballot_time.desc()).all()
#	history = User.query.order_by(User.ballot_time.desc()).filter(id>2)
#	history = User.query.filter(id>2)
	return render_template('index.html',form = form,history=history)

@main.route('/result',methods=['GET','POST'])
def result():
	group_id = session.get('group_id')
	group = User.query.get_or_404(group_id)
	if group.result == 0:
		a = random.randint(1,7)
		while User.query.filter_by(result=a).first():
			a = random.randint(1,7)
		group.result = a #a , 0
		group.ballot_time = datetime.utcnow()
		db.session.add(group)
		db.session.commit()
		flash("Succeed.")
	else:
        flash("Your group have had balloted!")
	return render_template('result.html',group_id =3)
