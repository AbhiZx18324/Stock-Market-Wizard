import requests
from bs4 import BeautifulSoup
import jsonlines
from datetime import datetime
import time
import os

# Define the URL of the financial news website to scrape
news_url = 'https://finance.yahoo.com/topic/stock-market-news/'

# Define the path to the folder to store the scraped news data in JSON Lines format
folder_path = './MarketNews/'
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Function to scrape and update news data
def update_news_data(folder_path):
    # Scrape the news website
    response = requests.get(news_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract news articles
    news_articles = soup.find_all('div', class_='Ov(h) Pend(44px) Pstart(25px)')
    
    # Define JSON Lines file path
    json_file_path = os.path.join(folder_path, f'stock_market_news_{datetime.now().strftime("%Y%m%d%H%M%S")}.jsonl')
    
    with jsonlines.open(json_file_path, mode='w') as writer:
        for article in news_articles:
            # Extract headline from <h3> tag
            headline = article.find('h3').text.strip()
            
            # Extract content from <p> tag
            content = article.find('p').text.strip()
            
            # Extract source and publication time
            source_and_time = article.find('div', class_='C(#959595) Fz(11px) D(ib) Mb(6px)').text.strip()
            
            # Write the scraped data to the JSON Lines file
            writer.write({"doc" : f"Headline: {headline}\nContent: {content}\nSource: {source_and_time}"})

# Schedule the update_news_data function to run every hour
while True:
    update_news_data(folder_path)
    time.sleep(15)  # Sleep for 1 hour (3600 seconds) before the next update

