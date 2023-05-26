class CapitalOp:
    def capital_after_trade(init_capital, entryprice, closingprice, quantity):
        a= quantity
        b= entryprice
        c= closingprice
        d= init_capital

        buy_margin= a * b
        sell_margin= a * c
        diff= abs(buy_margin-sell_margin)    #short
        print(diff)
        if buy_margin <= sell_margin:
                final_capital= d + diff
        else:
            final_capital= d - diff
        
        return final_capital
        
if __name__=='__main__':
    print(CapitalOp.capital_after_trade(100, 2, 5, 50))

    