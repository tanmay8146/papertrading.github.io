# import pandas as pd
# import numpy as np
import dbengine as dbhandler

class Analytics:   
    def capital_chart(uid, capital):
        #  TODO: takes chart data and plots a graph of capital cash flow 
        import matplotlib.pyplot as plt
        import numpy as np

        capital_list= [capital]
        for x in len(capital_list):
            i= dbhandler.get_capital(uid)
            capital_list.append(i)
            x+=1
        plt.plot(capital_list,'ro')
        plt.show()
        plt.savefig('chart.jpg')


    def win_loss_ratio(data):
        # TODO: calculates risk-to-reward ratio and shows output(ratio) on the frontend 
        pass

class Reward:
    def reputation_score(score):
        # TODO: get current reputation score and increment accordding to trading actions
        pass

