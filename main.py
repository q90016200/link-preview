import argparse
# import requests
import time
import json

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


parser = argparse.ArgumentParser()
parser.add_argument("arg1")
args = parser.parse_args()
# print(f"第 1 個引數：{args.arg1:^10}，type={type(args.arg1)}")
url = args.arg1
# print("網址為:", url)


# response = requests.get(args.arg1) # 裡面擺請求的目標網址
# print(response)

# 根據真實世界的統計隨機產生一個 User-Agent 字串。
ua = UserAgent()
user_agent = ua.random

# selenium 打開 chrome
# 後面的 executable_path 為你 chromedriver 的路徑(相對路徑)
# driver = webdriver.Chrome(executable_path="./chromedriver")
opts = Options()
opts.add_argument(f'user-agent={user_agent}')
opts.add_argument('--headless')  # 無頭chrome
opts.add_argument('--disable-gpu')
browser = webdriver.Chrome(
    executable_path=ChromeDriverManager().install(), chrome_options=opts)
browser.get(url)

# time.sleep(3)  # 強制等待 5 秒

# print(browser.title)

# 獲得頁面資訊
pageSource = browser.page_source
# print(pageSource)


# title = browser.title
# 關閉瀏覽器視窗
browser.close()

# 建立爬取對象
soup = BeautifulSoup(pageSource, 'lxml')

# 輸出排版後的 HTML 程式碼
# print(soup.prettify())


# 抓取網頁 title

pTitle = soup.find("meta", property="og:title")
if not pTitle:
    pTitle = soup.find("title")
    if pTitle:
        title = pTitle.getText()
else:
    title = pTitle.get("content", None)

# 抓出描述
description = soup.find("meta", property="og:description")
if not description:
    fD = description = soup.find('meta', {'name': 'description'})
    if fD:
        description = fD.get("content", None)
else:
    description = description.get("content", None)

# meta = soup.find_all("meta")
# for tag in soup.find_all("meta"):
#     if tag.get("name", None) == "description":
#         print(tag.get("content", None))
# print(meta)


# 抓出圖片(預設抓取 meta, 若無取得 <img> 第一張)
img = soup.find("meta", property="og:image")
if not img:
    img = soup.find("img")
    if img:
        img = img.get("src")
else:
    img = img.get("content", None)

# 排除相對位置的圖片
if img:
    if img.find("http") == -1:
        img = None

# 印出結果
parseData = {}
parseData["url"] = url
parseData["title"] = title
parseData["description"] = description
parseData["img"] = img

# print(parseData)
print(json.dumps(parseData, ensure_ascii=False))




