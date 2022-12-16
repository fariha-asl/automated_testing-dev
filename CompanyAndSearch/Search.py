from selenium import webdriver
import time


def login_test():
    global driver
    driver = webdriver.Chrome("/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/chromedriver")

    # driver = webdriver.Firefox("/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/geckodriver")
    driver.set_page_load_timeout(60)
    driver.get("https://stage.qorum.io/site/login")
    driver.maximize_window()
    driver.find_element_by_name("email").send_keys("fariha@asl.aero")
    driver.find_element_by_name("password").send_keys("12345678")
    driver.find_element_by_name("login-button").click()
    time.sleep(4)

def search_test():
    driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div/div[2]/div[2]/div[1]/div/span").click()
    time.sleep(3)
    driver.find_element_by_id("qorum-search").send_keys("voucher0012")
    time.sleep(4)
    driver.find_element_by_id("qorum-search").clear()
    time.sleep(3)
    driver.find_element_by_id("qorum-search").send_keys("5000")
    time.sleep(4)
    driver.find_element_by_id("qorum-search").clear()
    time.sleep(3)
    driver.find_element_by_id("qorum-search").send_keys("Asl staff")
    time.sleep(4)
    driver.find_element_by_id("qorum-search").clear()
    time.sleep(3)
    driver.find_element_by_id("qorum-search").send_keys("saddam")
    time.sleep(4)
    driver.find_element_by_id("qorum-search").clear()
    time.sleep(3)
    driver.find_element_by_id("qorum-search").send_keys("3 Jan 2021")
    time.sleep(4)
    driver.find_element_by_id("qorum-search").clear()
    time.sleep(3)





def logout_test():
    driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div/div[2]/div[3]/div[1]/div/span[2]").click()
    time.sleep(3)
    driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div/div[2]/div[3]/div[2]/div[3]/div[2]/a").click()
    time.sleep(3)
    driver.quit()


login_test()
search_test()
logout_test()