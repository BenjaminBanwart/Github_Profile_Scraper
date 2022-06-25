#import requests and beautifulsoup
import requests
from bs4 import BeautifulSoup as bs

#prompt user to input username and save it to a variable that is used in a saved url variable
github_user = input('Input Github User: ')
url = f"https://github.com/{github_user}"

#configure scrape
scraping = requests.get(url)
soup_return = bs(scraping.content, 'html.parser')

#finds the specified element that is provided in the find() method here
profile_image = soup_return.find('img', {'alt': 'Avatar'}) ['src']
print(profile_image)
