from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options




PATH = "C:\\Users\\Kashif\\Music\\chromedriver\\chromedriver.exe" 
driver = webdriver.Chrome(PATH)

driver.get("https://www.youtube.com/shorts/s8wEGKkNNv0")
#driver.close()




#driver = webdriver.Firefox(executable_path='C:\\Users\\Kashif\\Music\\geckodriver-v0.26.0-win64')
#driver = webdriver.Firefox(firefox_binary=binary,executable_path="C:\\Users\\Kashif\\Music\\geckodriver\\geckodriver.exe")