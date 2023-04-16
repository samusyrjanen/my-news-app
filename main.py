from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()

api_key=os.getenv('API_KEY')

query = 'ukraina'
url = f'https://newsdata.io/api/1/news?apikey={api_key}&q={query}&domain=hs,is'

response = requests.get(url)
print(response)

if response.status_code == 200:
    data = json.loads(response.text)
    articles = data['results']
    for article in articles:
        print(article['title'])
        print(article['link'])
        print(article['pubDate'])
        print()
else:
    print(f"Error: {response.status_code}")