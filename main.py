from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()

"""
API needs to have
- free
- full text content
- publish date range is wide enough
"""
api_key=os.getenv('API_KEY')

query = 'ukraine'
url = f'https://newsdata.io/api/1/news?apikey={api_key}&q={query}&language=en'

response = requests.get(url)
print(response)

if response.status_code == 200:
    data = json.loads(response.text)
    articles = data['results']
    for article in articles:
        print(article['title'])
        print(article['country'])
        print(article['pubDate'])
        print()
    print(articles[0]['content'])
else:
    print(f"Error: {response.status_code}")