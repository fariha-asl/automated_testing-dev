from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.remote.webelement import WebElement
# from webdriver_manager.chrome import ChromeDriverManager


def login_test():
    global driver
    driver = webdriver.Chrome("/Users/aslmacbookair/chromedriver/chromedriver3")
    # driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.set_page_load_timeout(100)
    driver.get("https://stage.qorum.io/site/login")
    driver.maximize_window()
    driver.find_element_by_name("email").send_keys("saddam@gmail.com")
    driver.find_element_by_name("password").send_keys("12345678")
    driver.find_element_by_name("login-button").click()
    time.sleep(4)

def voucher_create():
    driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div/div[2]/div[1]/div/div/a/i").click()
    #Voucher Type
    driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div[1]/div/div[2]/div/div/button/div/div/div").click()
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div[1]/div/div[2]/div/div/div/div/ul/li[2]/a/span").click()
    time.sleep(2)

    #Customer name
    driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div[1]/div/div[3]/div/span/span[1]/span/span[1]/span").click()
    driver.find_element_by_xpath("/html/body/span/span/span[1]/input").send_keys("A")
    webElemList = []
    time.sleep(1)
    optionlist= driver.find_element_by_xpath("//*[@id=\"select2-voucher_to-results\"]")
    # for el in optionlist:
    #     webElemList.append(el)
    optionlist.find_element_by_xpath("/html/body/span/span/span[2]/ul/li[5]").click()
    print(len(webElemList))
    time.sleep(2)

    #date
    driver.find_element_by_id("kt_datepicker_2").send_keys("2021-06-15")
    time.sleep(2)

    #currency
    driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div/div[1]/div/div/button/div/div/div").click()
    driver.find_element_by_id("bs-select-2-1").click()
    time.sleep(1)
    # drp = Select(element)
    # drp.select_by_visible_text("BDT")
    # time.sleep(1)

    #File Upload
    driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div[2]/div/button/i").click()

    driver.find_element_by_id("filePreviewInput").send_keys("/Users/aslmacbookair/Downloads/fariha-hossain.pdf")
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div[2]/div/div/div/div/div[3]/button[1]").click()
    time.sleep(2)

    #Reference
    driver.find_element_by_id("voucher-reference_no").send_keys("T21899")

    #Item Add
    driver.find_element_by_name("VoucherItem[0][description]").send_keys("lunch for all employee")
    time.sleep(1)
    driver.find_element_by_id("voucheritem-0-quantity").send_keys("35")
    time.sleep(1)
    driver.find_element_by_id("voucheritem-0-unit_price").send_keys("300")
    time.sleep(1)

    driver.find_element_by_id("select2-voucheritem-0-chart_of_account_id-container").click()
    driver.find_element_by_xpath("/html/body/span/span/span[1]/input").send_keys("of")
    webElemList = []
    time.sleep(1)
    optionlist = driver.find_element_by_xpath("/html/body/span/span/span[1]/input")

    optionlist.find_element_by_xpath("/html/body/span/span/span[2]/ul/li[1]").click()

    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[2]/div/div/form/div[2]/button").click()
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[2]/div/div/form/div[2]/div/button[2]").click()
    time.sleep(4)


def logout_test():
    driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div/div[2]/div[3]/div[1]/div/span[2]").click()
    time.sleep(3)
    driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div/div[2]/div[3]/div[2]/div[3]/div[2]/a").click()
    time.sleep(3)
    driver.quit()

if __name__ == "__main__":

    login_test()
    voucher_create()
    logout_test()
