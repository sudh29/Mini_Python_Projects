import requests
from bs4 import BeautifulSoup
import json

# URL of the website to scrape
url = "https://www.openai.com/blog/"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Parse the HTML content of the page using Beautiful Soup
soup = BeautifulSoup(response.content, "html.parser")
import pdb

pdb.set_trace()
# Find all the elements with class 'content-card'
content_cards = soup.find_all(class_="content-card")


# Find article titles and links within content cards
articles = []
for card in content_cards:
    title_element = card.find(class_="content-card-title")
    if title_element:
        title = title_element.get_text()
        link = title_element.a["href"]
        articles.append({"title": title, "link": link})
import pdb

pdb.set_trace()
# Define the output file name
output_file = "scraped_data.json"

# Store the scraped data in a JSON file
with open(output_file, "w") as f:
    json.dump(articles, f, indent=4)

print(f"Scraped data saved to {output_file}")
