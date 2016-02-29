from flask.ext.wtf import Form
from ..models import User
from wtforms import SelectField,SubmitField
class NameForm(Form):
#	group_id = SelectField(u'group',choices=[('1','C++'),('2','python'),('3','Plain text'),('4','rrr'),('5','ttt')])
	group_id = SelectField(u'group',coerce = int)
	def __init__(self,*args,**kwargs):
		super(NameForm,self).__init__(*args,**kwargs)
		self.group_id.choices = [(group_id.id,group_id.username) for group_id in User.query.order_by(User.username).all()]
	submit = SubmitField('Submit')
