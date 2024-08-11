import requests
from bs4 import BeautifulSoup
import json
url = 'https://www.womansday.com/relationships/dating-marriage/a41055149/best-pickup-lines/'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

# Initialize store titles and text
data = {}

# Find all li elements for titles
gettitle = soup.find_all('li', class_='css-32630i emt9r7s3')
for title in gettitle:
    a_tag = title.find('a')
    if a_tag:
        title_text = a_tag.text
        data[title_text] = []

# Extract pickup lines based on categories
# Best Pickup Line
best_pickup_line = soup.find('ul', class_='css-1r2vahp emevuu60', attrs={'data-node-id': '10'})
if best_pickup_line:
    one_items = best_pickup_line.find_all('li')
    for li in one_items:
        bestpickup_line = li.text
        data.setdefault('Best Pickup Lines', []).append(bestpickup_line)

# Funny Pickup Line
funny_pickup_line = soup.find('ul', class_='css-1r2vahp emevuu60', attrs={'data-node-id': '16'})
if funny_pickup_line:
    two_items = funny_pickup_line.find_all('li')
    for li in two_items:
        funnypickup_line = li.text
        data.setdefault('Funny Pickup Lines', []).append(funnypickup_line)

# Cheesy Pickup Lines
cheesy_pickup_line = soup.find('ul', class_='css-1r2vahp emevuu60', attrs={'data-node-id': '21'})
if cheesy_pickup_line:
    three_items = cheesy_pickup_line.find_all('li')
    for li in three_items:
        cheesypickup_line = li.text
        data.setdefault('Cheesy Pickup Lines', []).append(cheesypickup_line)

# Cute Pickup Lines
cute_pickup_line = soup.find('ul', class_='css-1r2vahp emevuu60', attrs={'data-node-id': '26'})
if cute_pickup_line:
    four_items = cute_pickup_line.find_all('li')
    for li in four_items:
        cutepickup_line = li.text
        data.setdefault('Cute Pickup Lines', []).append(cutepickup_line)

# Flirty Pickup Lines
flirty_pickup_line = soup.find('ul', class_='css-1r2vahp emevuu60', attrs={'data-node-id': '30'})
if flirty_pickup_line:
    five_items = flirty_pickup_line.find_all('li')
    for li in five_items:
        flirtypickup_line = li.text
        data.setdefault('Flirty Pickup Lines', []).append(flirtypickup_line)

# Pickup Lines for Girls
girls_pickup_line = soup.find('ul', class_='css-1r2vahp emevuu60', attrs={'data-node-id': '35'})
if girls_pickup_line:
    six_items = girls_pickup_line.find_all('li')
    for li in six_items:
        girlspickup_line = li.text
        data.setdefault('Pickup Lines for Girls ', []).append(girlspickup_line)

# Pickup Lines for Guys
guys_pickup_line = soup.find('ul', class_='css-1r2vahp emevuu60', attrs={'data-node-id': '40'})
if guys_pickup_line:
    seven_items = guys_pickup_line.find_all('li')
    for li in seven_items:
        guyspickup_line = li.text
        data.setdefault('Pickup Lines for Guys ', []).append(guyspickup_line)

# Convert to JSON format
output_json = json.dumps(data, indent=4)

# Save JSON file
with open('information.json', 'w') as file:
    file.write(output_json)

print("Saved data successfully")
