import requests
from bs4 import BeautifulSoup
import nltk
import ssl
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter




try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download()




ssl._create_default_https_context = ssl._create_unverified_context

# Function to scrape text from a URL
def scrape_text(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup.get_text()
    else:
        raise Exception('Failed to retrieve the webpage')

# Function to parse text and extract keywords
def extract_keywords(text):
    
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word.lower() not in stop_words]
    frequency = Counter(filtered_tokens)
    return frequency.most_common(10)

# URL of the webpage you want to scrape
url = 'https://apps.ualberta.ca/directory/person/mrs'

# Scrape text and extract keywords
try:
    text = scrape_text(url)
    keywords = extract_keywords(text)
    print(keywords)
except Exception as e:
    print(e)
