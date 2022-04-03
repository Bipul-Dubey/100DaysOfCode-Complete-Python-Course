import requests
import smtplib

Stock_Name="TSLA"
Compandy_Name="Tesla Inc"

Stock_Endpoint="https://www.alphavantage.co/query"
News_Endpoint="https://newsapi.org/v2/everything"
Stock_Api_key="3UGC2S36F89D3KRK"
News_Api_Key="2ae25b4272704d19a12c1e96fd52b846"

stock_params={
    "function":"TIME_SERIES_DAILY",
    "symbol":Stock_Name,
    "apikey":Stock_Api_key
}

news_params={
    "apiKey":News_Api_Key,
    "qinTitle":Compandy_Name
}

sender_email="smtpcheck9@gmail.com"
sender_pass="Smtp@1111"
receiver_email="raj12kumar21@yahoo.com"

response=requests.get(url=Stock_Endpoint,params=stock_params)
response.raise_for_status()
data=response.json()["Time Series (Daily)"]
data_list=[value for (key,value) in data.items()]
yesterday_data=data_list[0]
yesterday_closing_price=yesterday_data["4. close"]      # yesterday data

day_before_yesterday_data=data_list[1]
day_before_yesterday_closing_price=day_before_yesterday_data["4. close"]

# print(day_before_yesterday_closing_price,yesterday_closing_price)

difference=abs(float(yesterday_closing_price)-float(day_before_yesterday_closing_price))
differ_percent=(difference/float(yesterday_closing_price))*100


if differ_percent>0.5:
    news_response=requests.get(url=News_Endpoint,params=news_params)
    news_response.raise_for_status()
    articles=news_response.json()["articles"]
    three_article=articles[:3]

    formatted_articles=[f"Headline: {article['title']}. \nBrief: {article['description']}" for article in three_article]

    for article in formatted_articles:
        print(article)