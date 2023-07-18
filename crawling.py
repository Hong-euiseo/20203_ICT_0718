from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from urllib import request

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

# 1. browser open
browser = webdriver.Chrome(options=chrome_options)
browser.get("https://google.com/")

# 2. search
box = browser.find_element(
    By.XPATH,
    "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea",
)
box.clear()
box.send_keys("cat" + "\n")

# 3. go to image
image_button = browser.find_element(
    By.XPATH,
    "/html/body/div[7]/div/div[5]/div/div/div[1]/div[1]/div/a[1]",
)
image_button.click()

# 4. download images
for i in range(5):
    lis = browser.find_element(
        By.XPATH,
        f"/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div/div[1]/div[1]/span/div[1]/div[1]/div[{i+1}]/a[1]/div[1]/img",
    )
    final = lis.get_attribute("src")
    request.urlretrieve(final, f"./crawling/image_{i+1}.jpg")
