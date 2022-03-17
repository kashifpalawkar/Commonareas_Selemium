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
import LoginTest.Login_test as Login_Test


dff2 = pd.DataFrame()
row = 0
# get current directory
baseurl = 'https://www.phptravels.net/login'
path = os.getcwd()
excelFile = path + '\\TestData\\testdata.xlsx'
df3 = pd.read_excel(excelFile)
for index,row in df3.iterrows():
        executeValue = str(df3.loc[index,'Execute'])
        if (executeValue.lower() == "Yes".lower()):
            parameters = df3.loc[index,:]
            funcName = parameters['FunctionName'] 
            print(funcName)
            if (funcName == 'LoginTest'):
                loginfunc = Login_Test.Login(parameters,baseurl)
                login_call = loginfunc.loginToApp()
                print(login_call)
        elif(executeValue.lower() == "No".lower()):
            parameters = df3.loc[index,:]
            #funcName = parameters['FunctionName']
            #Execute = parameters['Execute']
            #TestCase = parameters['TestCase']
            #Parameter1 = parameters['Parameter1']
            noRunxl = pd.DataFrame()
            #noRunxl.loc[rrow,'Testcase'] = TestCase
            dff2 = dff2.append(parameters, ignore_index=False)
            print(dff2)
            ResultexcelFile = path + '\\TestData\\Results.xlsx'
            dff2.to_excel(ResultexcelFile)
        
            
            

driver = webdriver.Chrome()


driver.get(baseurl)
sleep(120)
driver.close()
driver.quit()

#options = webdriver.ChromeOptions()
#options.add_experimental_option('excludeSwitches', ['enable-logging'])
#driver = webdriver.Chrome(options=options)

#driver = webdriver.Firefox(executable_path='C:\\Users\\Kashif\\Music\\geckodriver-v0.26.0-win64')
#driver = webdriver.Firefox(firefox_binary=binary,executable_path="C:\\Users\\Kashif\\Music\\geckodriver\\geckodriver.exe")
