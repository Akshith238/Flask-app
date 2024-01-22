from flask import render_template,redirect,url_for
from application import app,db
from application import models,forms

@app.route('/')
def index():
    db.create_all()
    return render_template('base.html')

@app.route('/users')
def getUsers():
    users = models.User.query.order_by(models.User.id).all()
    return render_template('index.html',users=users)

@app.route('/register',methods=['GET','POST'])
def registerUsers():
    form=forms.UserForm()
    if form.validate_on_submit():
        new_user = models.User(name=form.name.data, email=form.email.data, role=form.role.data)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('getUsers'))
    errors=form.errors
    return render_template('register.html',form=form,errors=errors)