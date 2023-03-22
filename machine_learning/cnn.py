from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Open Firefox browser
browser = webdriver.Firefox()

# Load CNN website
browser.get("http://data.stats.gov.cn/easyquery.htm?cn=B01")

# Search for news for today
gdp_result = browser.find_element(By.CLASS_NAME,"zbExp")

# search_box.send_keys("news today")
# search_box.send_keys(Keys.RETURN)

# # Wait for search results to load
wait = WebDriverWait(browser, 10)
# wait.until(EC.presence_of_element_located((By.CLASS_NAME, "cnn-search__result-headline-text")))

# # Retrieve all headlines from search results
# headlines = browser.find_elements("name","cnn-search__result-headline-text")
# for headline in headlines:
#     print(headline.text)
print(gdp_result)
# Close the browser
browser.quit()
