from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("https://www.worldometers.info/gdp/china-gdp/")

show_rows_button = driver.find_element("xpath","//button[@class='btn-success'][text()='Show rows']")
if show_rows_button.is_displayed():
    show_rows_button.click()
time.sleep(1)

table = driver.find_element("xpath","//table[@id='main_table_countries_today']")
rows = table.find_elements_by_tag_name("tr")
for row in rows:
    cells = row.find_elements_by_tag_name("td")
    if cells:
        year_str = cells[0].text
        if year_str.isdigit() and int(year_str) in range(2000, 2021):
            year = int(year_str)
            gdp = cells[1].text
            print(f"Year {year}: {gdp}")

driver.quit()
