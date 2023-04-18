from requests_html import HTMLSession
import pandas as pd

# Define URL to scrape
url = 'http://www.tcmdoc.cn/ShuJuKu/ZhongYao/1.thtml'

# Create a new HTML session
session = HTMLSession()

# Send an HTTP GET request to the URL and render the content
r = session.get(url)
r.html.render(script=True,sleep=1000)

# Find the element that matches the CSS selector
info = r.html.find('#PanelContent > p:nth-of-type(2)', first=True)

print(info.text)
# Check if the info element exists and contains text
if info and info.text:
    # If it does, append the text to the result list
    result = [info.text]
else:
    # Otherwise, print an error message
    print('Error: Could not find element or element contains no text')

# Do something with the result list here
...
