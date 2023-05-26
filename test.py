def history():
    import mysql.connector as msql
    conn= msql.connect(host='localhost', user='tanmayxd', password= '8181', database= 'papertrading')
    fetcher= conn.cursor()
    fetcher.execute('select * from tradelog')
    fetched_history= fetcher.fetchall()

    for trade in fetched_history:
        print(trade)

def listdata():
    import mysql.connector as msql
    conn= msql.connect(host='localhost', user='tanmayxd', password= '8181', database= 'papertrading')
    fetcher= conn.cursor()
    fetcher.execute('select * from tradelog')
    fetched_history= fetcher.fetchmany()

    headings= ('Trade ID', 'Date', 'Exchange', 'Instrument', 'Order Type', 'Position', 'Quantity', 'Lots', 'Entry Price', 'Expected Target', 'Expected Stoploss', 'Product', 'Order State', 'Exit Price', 'Closing Capital', 'Comment')

    for trade in fetched_history:
    
        print(trade)
listdata()

