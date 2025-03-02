import requests
import yfinance as yf
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
news_api="455d69e6464e47db85d14903bb14210a"
response=requests.get(url=f"https://newsapi.org/v2/everything?q=Tesla stock&from=2025-02-29&sortBy=popularity&apiKey={news_api}")
data=response.json()
def get_stock_change(symbol):
    stock=yf.Ticker(symbol)
    #history
    hist=stock.history(period="3d")
    print(hist)
    if len(hist)<3 :
        print("no enough data")
        return False

    day_before_closing=hist["Close"].iloc[-3]
    yesterday_closing=hist["Close"].iloc[-2]
    change=abs(day_before_closing-yesterday_closing)
    five_percent_yesterday=yesterday_closing*0.05
    if change < five_percent_yesterday:
        print("get news")
        return True
    else:
        print("no significant change in stock prize")
        return False
get_news=get_stock_change("TSLA")#return True or False
if get_news:



## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price. 



## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator



## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.



#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

