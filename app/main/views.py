from flask import render_template,session,redirect,url_for

from . import main
from .forms import NameForm
from ..models import User


@main.route('/',methods=['GET','POST'])
def index():
#	user = User.query.get(id)
#	form = NameForm(request.Post,obj=user)
	form = NameForm()
#	form.group_id.choices += [(g.id,g.username) for g in User]
	if form.validate_on_submit():	
		session['group_id'] = form.group_id.data
		
		return redirect(url_for('.result',group_id = session.get('group_id')))
	return render_template('index.html',form = form)

@main.route('/result',methods=['GET','POST'])
def result():
	return render_template('result.html',group_id = session.get('group_id'))
