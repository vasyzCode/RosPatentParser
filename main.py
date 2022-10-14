from bs4 import BeautifulSoup
import csv

from selenium.webdriver import Chrome

driver = Chrome("C://chromedriver.exe")

n = 1

none_page = 0

while True:
    driver.get(f"https://rospatent.gov.ru/ru/patent-attorneys/{n}")
    response = driver.page_source
    soup = BeautifulSoup(response, 'lxml')
    result = soup.find("dl", class_="attorney-info-table")
    if result:
        dd, dt = result.find_all('dd'), result.find_all('dt')
        none_page = 0
        to_write = []
        for dd in dd:
            to_write.append(dd.text.strip().replace("  ", ""))
        with open('result.csv', 'a', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter="|", quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow(to_write)

    else:
        if none_page > 10:
            break
        else:
            none_page += 1
    n += 1

driver.close()
