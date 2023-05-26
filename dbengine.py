# config
HOST= 'localhost'
USER= 'tanmayxd'
PSWD= '8181'

def newuser(id, fname, email, uname, pswd, capital, broker, exp):
    import mysql.connector as msql
    conn= msql.connect(host= HOST, user= USER, password= PSWD, database= 'papertrading')
    cursor= conn.cursor()

    cursor.execute(f"INSERT INTO USER(id, full_name, email, username, password, capital, broker, experience) VALUES('{id}', '{fname}', '{email}', '{uname}', '{pswd}', '{capital}', '{broker}', '{exp}')")
    conn.commit()
    conn.close();



def loginauth(uname, pswd):
    import mysql.connector as msql
    conn= msql.connect(host=HOST, user=USER, password=PSWD, database= 'papertrading')
    cursor= conn.cursor()

    cursor.execute(f"SELECT * FROM USER WHERE username='{uname}' and password='{pswd}'")
    verifyvar= cursor.fetchall()
    if verifyvar:
        return True
    else:
        return False
    
def get_rep(userid):
    import mysql.connector as msql
    conn= msql.connect(host= HOST, user= USER, password= PSWD, database='papertrading')
    cursor= conn.cursor()

    cursor.execute(f"SELECT reputation_score FROM USER WHERE id='{userid}'")
    rp= cursor.fetchall()
    for i in rp:
        return i[0] #

def get_username(uid):
    import mysql.connector as msql
    conn= msql.connect(host= HOST, user= USER, password= PSWD, database='papertrading')
    cursor= conn.cursor()

    cursor.execute(f"SELECT username FROM USER WHERE id='{uid}'")
    user_name= cursor.fetchall()
    for i in user_name:
        return i[0] #
        
def get_uid(username):
    import mysql.connector as msql
    conn= msql.connect(host= HOST, user= USER, password= PSWD, database='papertrading')
    cursor= conn.cursor()

    cursor.execute(f"SELECT id FROM USER WHERE username='{username}'")
    user_id= cursor.fetchall()
    for i in user_id:
        return i[0] #

def get_capital(uid):
    import mysql.connector as msql
    conn= msql.connect(host= HOST, user= USER, password= PSWD, database='papertrading')
    cursor= conn.cursor()

    cursor.execute(f"SELECT capital FROM USER WHERE id='{uid}'")
    capital= cursor.fetchall()
    for i in capital:
        return i[0] #

def update_capital(id, new_capital):
    import mysql.connector as msql
    conn= msql.connect(host= HOST, user= USER, password= PSWD, database='papertrading')
    cursor= conn.cursor()
    cursor.execute(f"UPDATE user SET capital='{new_capital}' WHERE id='{id}'")
    conn.commit()
    conn.close()

class Dashboard:
    def __init__(self, userid, username, date, exchange, instrument, tradetype, positiontype, quantity, lotsize, entrypoint, target, stoploss, product, orderstate, exitpoint, closing, comment):
        self.userid= userid
        self.username= username
        self.date= date
        self.exchange= exchange
        self.instrument= instrument
        self.tradetype= tradetype
        self.positiontype= positiontype
        self.quantity= quantity
        self.lotsize= lotsize
        self.entrypoint= entrypoint
        self.target= target
        self.stoploss= stoploss
        self.product= product
        self.orderstate= orderstate
        self.exitpoint= exitpoint
        self.closing= closing
        self.comment= comment

    def record(self):
        import mysql.connector as msql
        conn= msql.connect(host= HOST, user= USER, password= PSWD, database='papertrading')
        cursor= conn.cursor()

        cursor.execute(f"INSERT INTO tradelog(id, trade_date, exchange, instrument, tradetype, positiontype, quantity, lotsize, entrypoint, target, stoploss, product, orderstate, exitpoint, closing, comment) VALUES('{self.userid}', '{self.date}', '{self.exchange}', '{self.instrument}', '{self.tradetype}', '{self.positiontype}', '{self.quantity}', '{self.lotsize}', '{self.entrypoint}', '{self.target}', '{self.stoploss}', '{self.product}', '{self.orderstate}', '{self.exitpoint}', '{self.closing}', '{self.comment}')")
        conn.commit()
        conn.close()

class DataScrapper:
    def __init__(self, userid, username, date, exchange, instrument, tradetype, positiontype, quantity, lotsize, entrypoint, target, stoploss, product, orderstate, exitpoint, closing, comment):
        self.userid= userid
        self.username= username
        self.date= date
        self.exchange= exchange
        self.instrument= instrument
        self.tradetype= tradetype
        self.positiontype= positiontype
        self.quantity= quantity
        self.lotsize= lotsize
        self.entrypoint= entrypoint
        self.target= target
        self.stoploss= stoploss
        self.product= product
        self.orderstate= orderstate
        self.exitpoint= exitpoint
        self.closing= closing
        self.comment= comment



if __name__ == '__main__':
    print(get_capital('QCF1BFZSBI'))