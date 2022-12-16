from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import keys



driver=webdriver.Chrome("C:/Users/Muna/PycharmProjects/webdriver/chromedriver.exe")

driver.set_page_load_timeout(90)
driver.get("https://demo.zeuz.ai/web/level/one/actions/save_text")
driver.maximize_window()

test=driver.find_element_by_id("randomText").copy_text()
driver.find_element_by_id("enter_text").send_keys(test)
driver.find_element_by_id("verify_id").click()








