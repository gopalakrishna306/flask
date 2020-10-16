from flask import Flask,render_template,request,redirect,url_for,abort
import werkzeug
from werkzeug import  secure_filename
from flask_mail import Mail ,Message

app=Flask(__name__)
mail = Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'gopalakrishna306@gmail.com'
app.config['MAIL_PASSWORD'] = '**************'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

@app.route('/home')
def home():
    name = 'gopalakrishna'
    return  render_template('home.html',{'name':name})

@app.route('/ssc')
def ssc():
    return  render_template('ssc.html')

@app.route('/b.tech')
def btech():
    return  render_template('btech.html')

@app.route('/mtech')
def mtech():
    return  'm.tech'


@app.route('/form')
def form():
    return  render_template('form.html')

@app.route('/resultview')
def resultview():
    return render_template('resultview.html')

@app.route('/result',methods=["GET","POST"])
def result():
    if request.method=='POST':
        data=request.form
        name=data['name']
        age=data['age']
        sex=data['sex']
        email=data['email']
        phone=data['phone']
        print("name :-{}\n age :-{}\n sex :-{}\n phone :-{}\n emai :-{}".format(name,age,sex,phone,email))
    else:
        return abort(401,'not admin')


    return  redirect(url_for('resultview'))


@app.route('/fileuploder')
def fileuploder():
    return  render_template('fileuploder.html')


@app.route('/filesaver', methods=['GET',"POST"])
def filesaver():
    if request.method=="POST":
        f=request.files['files']
        f.save(secure_filename(f.filename))
    return render_template('resultview.html')


# @app.route("/")
# def index():
#    msg = Message('Hello', sender = 'gopalakrishna255@gmail.com', recipients = ['gk9652@gmail.com'])
#    msg.body = "This is the email body"
#    mail.send(msg)
#    return "Sent"






if __name__=='__main__':
    app.run(debug=True)