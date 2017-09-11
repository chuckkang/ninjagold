from flask import Flask, render_template, request, redirect, session
import random
from datetime import datetime
from flask import Markup
app = Flask(__name__)
app.secret_key = " this is the secret key"

@app.route('/', methods=['POST', 'GET'])
def index():
      if (session.get('started') == '' and request.method=='GET'):
        session['totalgold'] = 0
        session['activity'] = ''
        session['started'] = 'start'
        nav=''
      else:
        nav='return'
            
      return render_template("index.html", nav=nav)

@app.route('/process_money', methods=['POST'])
def processrequest():
    nav = request.form['building']
    if (nav == 'farm'):
        #create a random number
        rnd = random.randrange(10, 20)
        session['totalgold'] += rnd
        session['activity'] += "Entered farm and received " + str(rnd) + " coins of Gold. " + str(datetime.now()) + "\n"

    elif (nav == 'cave'):
        rnd = random.randrange(5, 10)
        session['totalgold'] += rnd
        session['activity'] += "Entered cave and received " + str(rnd) + " coins of Gold. " + str(datetime.now()) + "\n"
    elif (nav == 'house'):
        rnd = random.randrange(2,5)
        session['totalgold'] += rnd
        session['activity'] += "Entered house and received " + str(rnd) + " coins of Gold. " + str(datetime.now()) + "\n"
    elif (nav == 'casino'):
        rnd = random.randrange(-50,50)
        session['totalgold'] += rnd
        session['activity'] += Markup("<font color='red'>Entered casino and received " + str(rnd) + " coins of Gold. " + str(datetime.now()) + "</font>\n") 

    return redirect ('/' )

@app.route('/reset')
def reset():
    session['totalgold']=0
    session['activity']= ''
    session['started']=''
    return redirect('/')

app.run(debug=True) # run our server