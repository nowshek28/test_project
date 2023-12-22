#this file will scrap the data from the trading website as per the user choice
#and store it in a csv format.

import pandas as pd
import requests
import matplotlib.pyplot as plt
from graph_plotting import plot_data

# for authorization got to request header
header = {
    'Accept':'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'en,ja;q=0.9,en-GB;q=0.8,en-US;q=0.7',
    'Cookie':'defaultLang=en; _ga=GA1.1.187066459.1703058750; _ga_QJZ4447QD3=GS1.1.1703058791.1.1.1703058843.0.0.0; nsit=_87ga4RGYFKIIyG5mOmvEWtM; ak_bmsc=01554C627E91C30A42E13225FEB5A89B~000000000000000000000000000000~YAAQRnItF2Oa1WiMAQAAqkVzjxbk6xjAtdFI22wqLxGZ6mxFQuWGzQ5sKpyaR8ycfRcn2B0JpF5z7l4+5KxTiUpnHNf05lpv2fddChI/Tn6AGjlLRxDnA4RGhRtNMIvcmno4J0r9La8yElJaAW+y5qlHMDYwL9M5aY8kf3nnLapJqhrSwpNmshGwVyGTn8DybrA7khY1MnNxpnIyVeSd94TJsvB2HKnBMM1zmrMxyBYdbRh7F8cNZhCGsKypHbxETwubeiql6a4Gj1ZMJCBscNQszy3hgn/74djHbRxeY0D5LrK8POD/eJfXI4Sdqu7VpzCg/1QMBRRn3A5WEUjzjsW88O6PotERFbEmRAFuIUmbgP5JtmzTiWPJ0WaG9FYm2pYTiMPusY4pVjlSTxy2rbcfs9VgP1IbdW4v790F8UizttIdZlL5IlMJLNhOUaIDnEl60R/BGWJeIma7wrmnMScH38uOQu/NGn++apSrome+05OzbahE0qzYOJhcufy6PQY/; AKA_A2=A; nseQuoteSymbols=[{"symbol":"RELIANCE","identifier":null,"type":"equity"}]; nseappid=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhcGkubnNlIiwiYXVkIjoiYXBpLm5zZSIsImlhdCI6MTcwMzIxMzc5MSwiZXhwIjoxNzAzMjIwOTkxfQ.UU5lqcpY7uJsEcN0duqqwMi3uNUGgy-gEEmI_LsNO-g; RT="z=1&dm=nseindia.com&si=d4942c46-8c61-4e50-b121-17e3f4345dff&ss=lqg1hi6u&sl=2&se=8c&tt=8iv&bcn=%2F%2F684d0d46.akstat.io%2F"; _ga_87M7PJ3R97=GS1.1.1703213744.2.1.1703213792.0.0.0; bm_sv=FA1277DA913A829D63BAC512B50818F9~YAAQRnItF7ef1WiMAQAA0f9zjxbo6iCq2uXJTmdZDurqy15UJHA0kM6nn8eyJj9Kxf832bG2FQXj5HJ64gsnN2tfke2CgbZEdLRhb1x7DRTyDwHNREwW0XIjUabLIOj3gozk5UrQNUdfQ/wfE6Z+EilPIMOSFdjjBDUaMLzX64ZTsVad2kqJh5mPbcZMCw3Wb5hciEFux9vYJj/ebpmaqpzrK4hLZaYBlHJOVs7wox/tgusqgC2j5sFHqoqLsIyamaCA~1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
    'X-Requested-With':'XMLHttpRequest'
}

response = requests.get(url = "https://www.nseindia.com/api/chart-databyindex?index=RELIANCEEQN",
                        headers = header)
print(response)
Data = pd.DataFrame(response.json()['grapthData'])   #epoch timestamp
print(Data)
Data.columns = ['timestamp','price']

Data['timestamp'] = pd.to_datetime(Data['timestamp'],format="hh:mm")
print(Data)