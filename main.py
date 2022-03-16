from importlib.resources import path
from inspect import Parameter
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from time import sleep
from datetime import timedelta
import pandas as pd
import xlwt
import os


# get current directory
path = os.getcwd()
excelFile = path + '\\TestData\\testdata.xlsx'
df3 = pd.read_excel(excelFile)

for index,row in df3.iterrows():
        executeValue = str(df3.loc[index,'Execute'])
        if (executeValue.lower() == "Yes".lower()):
            parameters = df3.loc[index,:]
            funcName = parameters['FunctionName'] 
            print(funcName)
            

driver = webdriver.Chrome()

#options = webdriver.ChromeOptions()
#options.add_experimental_option('excludeSwitches', ['enable-logging'])
#driver = webdriver.Chrome(options=options)
driver.get("https://tm.ca-test.com")
sleep(5)
driver.close()
driver.quit()








#driver = webdriver.Firefox(executable_path='C:\\Users\\Kashif\\Music\\geckodriver-v0.26.0-win64')
#driver = webdriver.Firefox(firefox_binary=binary,executable_path="C:\\Users\\Kashif\\Music\\geckodriver\\geckodriver.exe")
