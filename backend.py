from flask import Flask, render_template, request
from flask import url_for, redirect, session

import dbengine as dbhandler
from functions import createid_randomizer, secret_key
from analytics_engine import Analytics

mainApp= Flask('papertrading')
mainApp.secret_key= secret_key()
print(f'connecting with secret key {secret_key()} powered by fernet')

@mainApp.before_request
def state_timeout():
    from datetime import timedelta
    session.permanent = True
    mainApp.permanent_session_lifetime = timedelta(minutes=60)
    print('default session timeout is set to 60 minutes!')

@mainApp.route('/')
def landing_page():
    return render_template('landing.html')

@mainApp.route('/signup', methods=['GET', 'POST'])
def signup():
    msg= 'successfully redirected to sign up page'
    if request.method == 'POST':
        uid= createid_randomizer()
        name= request.form['fullname']
        email= request.form['email']
        uname= request.form['username']
        pw= request.form['password']
        cap= request.form['initcap']
        broker= request.form['broker']
        exp= request.form['experience']
        dbhandler.newuser(uid, name, email, uname, pw, cap, broker, exp)
        with open('test_registration', 'a') as reg:
            reg.write(f"Name: {name}, Username: {uname}, Password: {pw}, Capital amount: inr.{cap}, Broker: {broker}, Experience: {exp} year(s)")
        msg= f'registered successfully with userid {uid}'
    return render_template('signup.html', msg= msg)

@mainApp.route('/login', methods= ['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username']= request.form['username']
        session['password']= request.form['password']
        if dbhandler.loginauth(session['username'], session['password']):
            global username
            username= session['username']
            return redirect(url_for('dashboard'))
        else:
            username= ''
            return redirect(url_for('prompt'))

    return render_template('login.html')

@mainApp.route('/dashboard', methods= ['POST', 'GET'])
def dashboard():
    try:
        session_user= session['username']
        db= dbhandler.Dashboard
        session_uid= dbhandler.get_uid(session_user)
        in_capital= dbhandler.get_capital(session_uid)
        
        if request.method == 'POST':
            
            trade_date= request.form['date']
            trade_exchange= request.form['exchange']
            trade_instrument= request.form['instrument']
            trade_tradetype= request.form['tradetype']
            trade_positiontype= request.form['positiontype']
            trade_quantity= int(request.form['quantity'])
            trade_lotsize= int(request.form['lotsize'])
            trade_entrypoint= int(request.form['entrypoint'])
            trade_target= int(request.form['target'])
            trade_stoploss= int(request.form['stoploss'])
            trade_product= request.form['product']
            trade_orderstate= request.form['orderstate']
            trade_exitpoint= int(request.form['exitpoint'])
            trade_comment= request.form['comment']

            if request.method == 'POST':
                print('capital= %s at line 62'%in_capital)
                from operations import CapitalOp as calculator
                after_trade_capital= calculator.capital_after_trade(init_capital=in_capital, entryprice= trade_entrypoint, closingprice= trade_exitpoint, quantity= trade_quantity)  
                print('capital after calculations= %s'%after_trade_capital) 
                capital= after_trade_capital
                closing= capital
                print('closing= %s'%closing)
                dbhandler.update_capital(session_uid, capital)

                obj= db(session_uid, session_user, trade_date, trade_exchange, trade_instrument, trade_tradetype, trade_positiontype, trade_quantity, trade_lotsize, trade_entrypoint, trade_target, trade_stoploss, trade_product, trade_orderstate, trade_exitpoint, closing, trade_comment)
                obj.record()
        in_capital= dbhandler.get_capital(session_uid)
            
        return render_template('dashboard.html', user= session_user, uid= session_uid, capital= in_capital)
    except KeyError:
        return redirect(url_for('prompt'))
   
@mainApp.route('/tradelog')
def history():
    try:
        import mysql.connector as msql
        import pandas as pd

        session_user= session['username']
        session_uid= dbhandler.get_uid(session_user)
        session_user= session_uid
        conn= msql.connect(host='localhost', user='tanmayxd', password= '8181', database= 'papertrading')
        fetcher= conn.cursor()
        fetcher.execute(f"select * from tradelog where id= '{session_user}'")
        fetched_history= fetcher.fetchall()

        headings= ('Trade ID', 'Date', 'Exchange', 'Instrument', 'Order Type', 'Position', 'Quantity', 'Lots', 'Entry Price', 'Expected Target', 'Expected Stoploss', 'Product', 'Order State', 'Exit Price', 'Closing Capital', 'Comment')

        df= pd.DataFrame()
        for x in fetched_history:
            df2= pd.DataFrame(list(x)).T
            df= pd.concat([df, df2])
        df.to_html('templates/history.html')
        
    except KeyError:
        return redirect(url_for('prompt'))
    return render_template('history.html', headings= headings)


@mainApp.route('/about')
def about():
    return render_template('about.html')

@mainApp.route('/index')
def index():
    return render_template('index.html')

@mainApp.route('/prompt')
def prompt():
    return redirect(url_for('login'))

@mainApp.route('/logout', methods=['GET', 'POST'])
def logout():
    session.pop('username', None)
    return redirect(url_for('landing_page'))

if __name__ == '__main__':
    mainApp.run(debug= True)