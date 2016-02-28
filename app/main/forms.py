from flask.ext.wtf import Form
from ..models import User
from wtforms import SelectField,SubmitField
class NameForm(Form):
	group_id = SelectField(u'group',choices=[('1','C++'),('2','python'),('3','Plain text')])
#	group_id = SelectField(u'group',choices=[User.query.all()])
	submit = SubmitField('Submit')
