from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import requests
import csv

fh = open("gofundme_scraped.csv", "w")
url = "https://www.gofundme.com/s?q=syria"

driver = webdriver.Firefox('/path/to/geckodriver')
driver.get(url)
while True:
    try:
        show_more_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "StateResults_button__DIGoI"))
        )
        show_more_button.click()
    except:
        break

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

#get links from the list
my_elements = soup.find_all(class_='FullStateListCard_card__HNpFF')
for element in my_elements:
    for link in element.find_all('a', href=True):
        response = requests.get("https://www.gofundme.com/" + link['href'])
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        try:
            title = soup.find(class_="mb0 p-campaign-title").get_text()
        except AttributeError:
            title = soup.find(class_="mb0 p-campaign-title")
        try:
            donation = soup.find(class_="m-progress-meter-heading").get_text()
        except AttributeError:
            donation = soup.find(class_="m-progress-meter-heading")
        try:
            description = soup.find(class_="p-campaign-description").get_text()
        except AttributeError:
            description = soup.find(class_="p-campaign-description")
        try:
            organizer = soup.find(class_="weight-900").get_text()
        except AttributeError:
            organizer = soup.find(class_="weight-900")
        csvwriter = csv.writer(fh)
        f_out = [title, description, organizer, donation]
        csvwriter.writerow(f_out)

driver.quit()



