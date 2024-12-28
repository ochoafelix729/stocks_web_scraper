from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from typing import Any

# executable_path = 'Users/ochoa/Downloads/edgedriver_arm64'

driver = webdriver.Edge()
url = 'https://www.google.com/finance/markets/most-active'
driver.get(url)

# time.sleep(5)
# driver.quit()

# //*[@id="yDmH0d"]/c-wiz[2]/div/div[4]/div[3]/div[1]/div/div/ul/li[1]/a/div/div/div[1]/div[1]/div/div

stocks_path = '//*[@id="yDmH0d"]/c-wiz[2]/div/div[4]/div[3]/div[1]/div/div/ul/li'
stocks_data = driver.find_elements(By.XPATH, stocks_path)

# to-text function

def to_text(arr: list[Any]) -> list[str]:
    res = []
    for el in arr:
        el = el.text
        res.append(el)
    return res

stocks_data = to_text(stocks_data)
# print(stocks_data)

# #sorting data

tickers = []
stocks_names = []
values = []
percent_changes = []

for entry in stocks_data:
    parts = entry.split('\n')
    tickers.append(parts[0])
    stocks_names.append(parts[1])
    values.append(parts[2])
    percent_changes.append(parts[4])

print(tickers, stocks_names, values, percent_changes)



# print(tickers)


# for i in range(1, len(stocks)+1):
#     info_path = f"//*[@id='yDmH0d']/c-wiz[2]/div/div[4]/div[3]/div[1]/div/div/ul/li[{i}]/a/div/div/div[1]/div[1]/div/div"
#     info = driver.find_element(By.XPATH, ticker_path)
#     print(info.text)

# //*[@id="yDmH0d"]/c-wiz[2]/div/div[4]/div[3]/div[1]/div/div/ul/li[1]/a/div/div/div[1]/div[1]/div/div

# //*[@id="yDmH0d"]/c-wiz[2]/div/div[4]/div[3]/div[1]/div/div/ul/li[2]/a/div/div/div[1]/div[1]/div/div