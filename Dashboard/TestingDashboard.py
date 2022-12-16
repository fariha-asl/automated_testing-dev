import click as click
from selenium import webdriver
import time


def login_test():
    #global driver
    driver = webdriver.Chrome("/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/chromedriver")

    # driver = webdriver.Firefox("/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/geckodriver")
    driver.set_page_load_timeout(90)
    driver.get("https://stage.qorum.io/site/login")
    driver.maximize_window()
    driver.find_element_by_name("email").send_keys("fariha@asl.aero")
    driver.find_element_by_name("password").send_keys("12345678")
    driver.find_element_by_name("login-button").click()
    time.sleep(4)


def dashboard_testing():
    driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div[1]/div[1]/div/div/a/div").click()
    time.sleep(3)
    driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div/div[1]/div[2]/div/ul/li[2]/a/span[1]").click()
    # Bar Chart
    driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div[2]/div/div/div[1]/div[2]/div/a/i").click()
    driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div[2]/div/div/div[1]/div[2]/div/div/ul/li[4]/a/span[2]").click()
    time.sleep(5)
    #Pi Chart
    driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div/a/i").click()
    driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div/div/ul/li[4]/a/span[2]").click()
    driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[2]/div/div[2]/div[2]/div/div[1]/div[2]/div/a/i").click()
    driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[2]/div/div[2]/div[2]/div/div[1]/div[2]/div/div/ul/li[4]/a/span[2]").click()
    time.sleep(5)
    #lolipop Chart
    driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[2]/div/div[3]/div/div/div[1]/div[2]/div/a/i").click()
    driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[2]/div/div[3]/div/div/div[1]/div[2]/div/div/ul/li[4]/a/span[2]").click()
    time.sleep(4)
    #Approved
    driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div[1]/div[2]/div/div/a/p").click()
    time.sleep(3)
    driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div/div[1]/div[2]/div/ul/li[2]/a/span[1]").click()

    #Reject
    driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div[1]/div[3]/div/div/a/p").click()
    time.sleep(3)
    driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div/div[1]/div[2]/div/ul/li[2]/a/span[1]").click()

    #All
    driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div[1]/div[4]/div/div/a/div").click()
    time.sleep(3)
    driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div/div[1]/div[2]/div/ul/li[2]/a/span[1]").click()


def logout_test():
    driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div/div[2]/div[3]/div[1]/div/span[2]").click()
    time.sleep(3)
    driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div/div[2]/div[3]/div[2]/div[3]/div[2]/a").click()
    time.sleep(3)
    driver.quit()


login_test()
dashboard_testing()
logout_test()


