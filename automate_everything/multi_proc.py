import time
import requests
from bs4 import BeautifulSoup
from multiprocessing import Process
from multiprocessing import Pool
from stocklist import stock_list
# file_path = "e:/nse_stocks_list.csv"


def get_stock_data(stock_symbol: str):
    try:
        stock_url = f"https://www1.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol={stock_symbol}&illiquid=0&smeFlag=0&itpFlag=0"
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.1462.54 Safari/537.36'}
        response = requests.get(stock_url, headers=headers)

        soup = BeautifulSoup(response.text, 'html.parser')
        data_array = soup.find(id='responseDiv').getText().strip().split(":")
        for data in data_array:
            if 'lastPrice' in data:
                index = data_array.index(data)+1
                latestPrice = data_array[index].split('"')[1]
                lp = float(latestPrice.replace(',', ''))
                print(f"{stock_symbol}: {lp}")
    except Exception as e:
        print(f"Could not get the data for {stock_symbol} \n {e}")


if __name__ == '__main__':
    # stock_list = []
    # procs = []
    start_time = time.perf_counter()
    # with open(file_path, 'r') as f:
    #     for data in f:
    #         stock_symbols = data.split(',')[0]
    #         stock_list.append(stock_symbols)

    pool = Pool(processes=60)
    # for stock in stock_list:
    # print(stock)
    start_time = time.perf_counter()
    pool.map(get_stock_data, stock_list)
    end_time = time.perf_counter()-start_time
    print(end_time)
    input("Enter to exit")
