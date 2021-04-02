using Python to capture web page title, description, web img

require
```
pip install selenium
pip install beautifulsoup4
pip install lxml
pip install webdriver_manager
pip install fake_useragent
```


usage ex:
```
    python main.py https://www.google.com/
```
response:
```
{"url": "https://www.google.com/", "title": "Google", "description": null, "img": "https://www.google.com/images/hpp/Chrome_Owned_96x96.png"}
```
