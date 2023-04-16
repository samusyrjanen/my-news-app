from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()
#newsdata_key=os.getenv('NEWSDATA.IO_API_KEY')
newsapi_key=os.getenv('NEWSAPI.ORG_API_KEY')

query = 'ukraina'
#newsdata_url = f'https://newsdata.io/api/1/news?apikey={newsdata_key}&q={query}&domain=hs,is'
newsapi_url = f'https://newsapi.org/v2/everything?q={query}&domains=yle.fi&apiKey={newsapi_key}'

response = requests.get(newsapi_url)

if response.status_code == 200:
    data = json.loads(response.text)
    for article in data['articles']:
        print(article['source'])
        print(article['title'])
        print(article['url'])
        print(article['publishedAt'])
        print()
    print(len(data['articles']))
    print(data['totalResults'])

    # articles = data['results']#newsdata
    # print(articles)
    # for article in articles:
    #     print(article['title'])
    #     print(article['link'])
    #     print(article['pubDate'])
    #     print()
else:
    print(f"Error: {response.status_code}")