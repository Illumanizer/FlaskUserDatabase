# from crypt import methods
import email
from textwrap import indent
from flask import Flask, render_template, request,redirect
from flask_sqlalchemy import SQLAlchemy
from flask import render_template
from sqlalchemy import create_engine
# from dateTime import dateTime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost/flasksql'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False


db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80),  nullable=False)
    email = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(300), nullable=False)
    # date_created=db.Column(db.dateTime,default=dateTime.utcnow)
    
    def __repr__(self):
        return '<User %r>' % self.username

@app.route('/',methods=['GET','POST'])
def landing():
    if request.method=='POST':   
        user=User(username=request.form['username'],email=request.form['email'],password=request.form['password'])
        db.session.add(user)
        db.session.commit()       
    allUsers=User.query.all()
    return render_template("index.html", allUsers=allUsers)


@app.route('/delete/<int:id>')
def deletePage(id):
    user=User.query.filter_by(id=id).first()
    db.session.delete(user)
    db.session.commit()
    # return "this is delete page"
    return redirect("/")

@app.route('/update/<int:id>',methods=['GET','POST'])
def updatePage(id):
    if request.method=='POST': 
        username=request.form['username']
        email=request.form['email']
        password=request.form['password']
        user=User.query.filter_by(id=id).first()  
        user.username=username
        user.email=email
        user.passowrd=password 
        user=User(user)
        db.session.add(user)
        db.session.commit()  
        return redirect("/")
    user=User.query.filter_by(id=id).first()   
    return render_template("update.html",User=user)

if __name__ =="__main__":
    app.run(debug=True) 