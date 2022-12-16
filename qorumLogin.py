from selenium import webdriver
import time

driver=webdriver.Chrome("C:/Users/Muna/PycharmProjects/webdriver/chromedriver.exe")

driver.set_page_load_timeout(90)

driver.get("https://stage.qorum.io/site/login")
driver.maximize_window()

driver.find_element_by_name("email").send_keys("fariha@asl.aero")
driver.find_element_by_name("password").send_keys("12345678")
driver.find_element_by_name("login-button").click()
time.sleep(4)

driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div/div[2]/div[3]/div[1]/div/span[2]").click()
time.sleep(3)
driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div/div[2]/div[3]/div[2]/div[3]/div[2]/a").click()
time.sleep(3)
driver.quit()