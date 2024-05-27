# pip install selenium
# pip install webdriver_manager

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


Link = r"D:\avinav\Backend\Voice.html"

# chrome_options = Options()
# user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
# chrome_options.add_argument(f"user-agent={user_agent}")
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--use-fake-ui-for-media-stream")
chrome_options.add_argument("--use-fake-device-for-media-stream")
chrome_options.add_argument("--headless=new")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get(Link)


def SpeechRecognitionModel():
    driver.find_element(by=By.ID, value="start").click()
    print("Listening...")
    while True:
        Text = driver.find_element(by=By.ID, value="output").text
        if Text:
            driver.find_element(by=By.ID, value="end").click()
            return Text

        else:
            sleep(0.333)


while True:
    Text = SpeechRecognitionModel()
    print(Text)
