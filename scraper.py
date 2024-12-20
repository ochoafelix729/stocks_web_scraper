import os
from openai import OpenAI
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import requests
import sqlite3

class Scraper():

    def __init__(self):
        """
        constructor
        """

        # load environmnent variables
        load_dotenv()
        self.api_key = os.getenv('OPENAI_API_KEY')

        #connect to openai
        self.openai = OpenAI()
        
        self.model = 'gpt-4o-mini'


    def fetch(self, url):
        """
        fetches the HTML content of the given URL
        """

        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.text
    
        except requests.exceptions.RequestException as e:
            print(f"Error fecthing the URL: {e}")
            return None

    
    def extract(self, html):
        """
        extracts the meaningful text from HTML
        """

        try:
            soup = BeautifulSoup(html, 'html.parser')

            # clean up text
            for trash in soup(['script', 'sytle']):
                trash.extract()
            text = soup.get_text(separator='\n')
            lines = [line.strip() for line in text.splitlines() if line.strip()]
            return '\n'.join(lines)
        
        except Exception as e:
            print(f"Error parsing HTML: {e}")
            return None

    def messages(self, text):
        """
        creates messages (list of objects)
        """

        return [
            {'role': 'system', 'content': 'You are a helpful assistant for summarizing stock changes in text.'},
            {'role': 'user', 'content': f"Summarize the stock changes in this text. Focus only on the changes in different stocks (give me the numbers). Avoid any unnessecary details that are unrelated to stocks. \n\n {text}. "}
        ]


    def summarize(self, text):
        """
        summarize text content
        """
        
        try:
            response = self.openai.chat.completions.create(
                model = self.model,
                messages = self.messages(text)
            )

            return response.choices[0].message.content
        
        except Exception as e:
            print(f"Error trying to summarize text: {e}")
            return None

    def scrape(self, url):
        """
        final product - web scraper
        """

        html = self.fetch(url)
        if not html:
            print("Failed fetch function.")
            return None
        
        text = self.extract(html)
        if not text:
            print("Failed extract function.")
            return None
        
        summary = self.summarize(text)
        if not summary:
            print("Failed summarize function.")
            return None

        return summary

    def insert_to_database(self, scrape, url):
        if not func:
            print("Failed to insert data into database.")

        # will fill in actual code later
        return scrape(url)