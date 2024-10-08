import RF_Algo_Backtest
import RF_Algo_Live
import VWAP_Algo_Backtest
import VWAP_Algo_Live_Manually_Execute
import login
import pyfiglet

#call the login module to log into Robinhood
login.main()

#Define the tickers of interest
stock_ticker = ["TSLA","AAPL"]

#Define the time periods of interest
# options - 5minute”, “10minute”, “hour”, “day”
time_period = ["day","hour"]

#Define the time period shorter than the time period of interest
# options - 5minute”, “10minute”, “hour”, “day”
shorter_time_period = ["5minute","5minute"]
#span
span = ["year","3month"]

def printing_method_name(text):
    text = pyfiglet.figlet_format(text)
    return text

    

if __name__ == '__main__':
    
  for i in range(len(stock_ticker)):
      for j in range(len(time_period)):

        print(printing_method_name("Random Forest Backtest for "+stock_ticker[i]+" and interval "+time_period[j]))    
        method ="Random Forest"
        RF_Algo_Backtest.main(stock_ticker[i],time_period[j],method,span[j])
        print(printing_method_name("Random Forest trading decision for "+stock_ticker[i]+" and interval "+time_period[j]))
        RF_Algo_Live.main(stock_ticker[i],time_period[j],method,span[j],shorter_time_period[j])
        method ="VWAP"
        print(printing_method_name("VWAP  backtest result for "+stock_ticker[i]+" and interval "+time_period[j]))
        VWAP_Algo_Backtest.main( stock_ticker[i],time_period[j],method,span[j])
        print(printing_method_name("VWAP trading decision for "+stock_ticker[i]+" and interval "+time_period[j]))
        VWAP_Algo_Live_Manually_Execute.main( stock_ticker[i],time_period[j],method,span[j])
    

