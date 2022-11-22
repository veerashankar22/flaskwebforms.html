from flask import Flask,render_template,request

from flask_wtf import Form
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

AI=Flask(__name__)
AI.config['SECRET_KEY']='csrftoken'
class NameForm(Form):
    name=StringField(validators=[DataRequired()])
    submit=SubmitField()

@AI.route('/webforms',methods=['GET','POST'])
def webforms():
    form=NameForm()
    if request.method=='POST':
        form=NameForm(request.form)
        if form.validate(): 
            print(form.name.data)
            return 'success'
    return render_template('webforms.html',form=form)


if __name__=='__main__':
    AI.run(debug=True)