import XLUtils
from selenium import webdriver
import time

#for incognito mood these 3 lines of code
#chrome_option = webdriver.ChromeOptions()
#chrome_option.add_argument("--incognito")

#driver=webdriver.Chrome("/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/chromedriver",chrome_options=chrome_option)

#def login_test():
driver = webdriver.Chrome("C:/Users/Muna/PycharmProjects/webdriver/chromedriver.exe")
driver.set_page_load_timeout(60)
driver.get("https://stage.qorum.io/site/login")
driver.maximize_window()

path="C:/Users/Muna/OneDrive/Desktop/Sheet1.xlsx"


rows = XLUtils.getRowCount(path,'Sheet1')

for r in range(2,rows+1):
    username=XLUtils.readData(path, 'Sheet1', r, 1)
    password=XLUtils.readData(path, 'Sheet1', r, 2)

    driver.find_element_by_name("email").send_keys(username)
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_name("login-button").click()
    time.sleep(4)


    try:
        if driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div/div[1]/div[1]/a/img[1]"):
            print("Login Qorum passed")
            XLUtils.writeData(path, 'Sheet1', r, 3, "passed")
            driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div/div[2]/div[3]/div[1]/div/span[2]").click()
            time.sleep(3)
            driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div/div[2]/div[3]/div[2]/div[3]/div[2]/a").click()
            time.sleep(3)
    except:
        # print('login failed')

    # if driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/form/div[2]/div/p'):
        print("Login Qorum Failed")
        XLUtils.writeData(path, 'Sheet1', r, 3, "Failed")
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("password").clear()



driver.quit()

#login_test()


