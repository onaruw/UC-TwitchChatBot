import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import time

options = uc.ChromeOptions()

#chrome profile here if you have one
profile = "C:\\Users\\Pc\\AppData\\Local\\Google\\Chrome\\User Data\\Default"
options.add_argument(f"user-data-dir={profile}")

driver = uc.Chrome(options=options, use_subprocess=True)

#username here 
username = " "
driver.get(f"https://www.twitch.tv/{username}")

time.sleep(5)

chatButton = driver.find_element(By.XPATH, "//*[@id='offline-channel-main-content']/div[2]/div[2]/div[1]/div/ul/li[5]/a")
chatButton.click()
time.sleep(2)

textButton = driver.find_element(By.CLASS_NAME, "chat-wysiwyg-input__editor")
textButton.click()
time.sleep(2)

textBox = driver.find_element(By.CLASS_NAME, "chat-wysiwyg-input__editor.focus-visible")

#replace 10 with how many times you want to send a message
for x in range(10):
        #replace 0.1 with how many delay you want (seconds)
        time.sleep(0.1)
        #replace x with what do you want to write
        textBox.send_keys(x)
        textBox.send_keys(Keys.ENTER)

time.sleep(10)


