from concurrent.futures import process
import pathlib
import time
import requests
from bs4 import BeautifulSoup
from multiprocessing import Process

file_path = "e:/nse_stocks_list.csv"


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
                latest_price = data_array[index].split('"')[1]
                lp = float(latest_price.replace(',', ''))
                print(f"{stock_symbol}: {lp}")
    except Exception as e:
        print(f"Could not get the data for {stock_symbol} \n {e}")
# with open(file_path, 'r') as f:
#     for data in f:
#         stock_symbols = data.split(',')[0]
#         print(stock_symbols)


if __name__ == '__main__':
    stock_list = []
    procs = []
    start_time = time.perf_counter()
    with open(file_path, 'r') as f:
        for data in f:
            stock_symbols = data.split(',')[0]
            stock_list.append(stock_symbols)
            # print(stock_symbols)

    # while True:
    for stock in stock_list:
        # get_stock_data(stock)
        p = Process(target=get_stock_data, args=(stock,))
        p.start()
        procs.append(p)
    # Making the program wait for 1 second before it runs again.
    # time.sleep(3)
    # print(procs)
    for p1 in procs:
        p1.join()
    time_taken = time.perf_counter()-start_time
    print(time_taken)


# procs = []
#    with open(file_name, "r") as f:
#         next(f)
#         for line in f:
#             # scp_to_server(line)
#             p = Process(
#                 target=scp_to_server,
#                 args=(line, cmd, source_path, dest_path),
#             )
#             p.start()
#             procs.append(p)
#     for p1 in procs:
#         p1.join()
