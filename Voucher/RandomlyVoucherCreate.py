from selenium import webdriver
import time
from RandomFunctionGenerate import CustomerName,ReferenceNo,RandomItem
from selenium.webdriver.remote.webelement import WebElement



def login_test():
    global driver
    driver = webdriver.Chrome("/Users/webdriver/chromedriver2")
    #driver = webdriver.Firefox(executable_path="/Users/aslmacbookair/chromedriver/gecko")
    # driver = webdriver.Edge(executable_path="/Users/aslmacbookair/chromedriver/edge")
    # driver = webdriver.Safari()
    # so when using safari,firefox use "executable_path"
    # and file er nam e space use koreben nah either underscore or rename the file

    driver.set_page_load_timeout(100)
    driver.get("https://stage.qorum.io/site/login")
    driver.maximize_window()
    driver.find_element_by_name("email").send_keys("morshed@gmail.com")
    driver.find_element_by_name("password").send_keys("12345678")
    driver.find_element_by_name("login-button").click()
    time.sleep(4)



def voucher_create():
    driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div/div[2]/div[1]/div/div/a/i").click()
    time.sleep(5)
    #Voucher Type
    driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div[1]/div/div[2]/div/div/button/div/div/div").click()
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div[1]/div/div[2]/div/div/div/div/ul/li[2]/a/span").click()
    time.sleep(2)
    # Customer name
    customer_name = CustomerName.customer_gen()
    driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div[1]/div/div[3]/div/span/span[1]/span/span[1]/span").click()
    driver.find_element_by_xpath("/html/body/span/span/span[1]/input").send_keys(customer_name)
    webElemList = []
    time.sleep(1)
    # optionlist = driver.find_element_by_xpath("//*[@id=\"select2-voucher_to-results\"]")
    driver.find_element_by_xpath("/html/body/span/span/span[2]/ul/li/span/em").click()
    print(len(webElemList))
    time.sleep(2)

     # date
    driver.find_element_by_id("kt_datepicker_2").send_keys("2021-12-21")
    time.sleep(2)

    # currency
    driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div/div[1]/div/div/button/div/div/div").click()
    driver.find_element_by_id("bs-select-2-1").click()
    time.sleep(1)

    # File Upload
    driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div[2]/div/button/i").click()

    driver.find_element_by_id("filePreviewInput").send_keys("/Users/aslsmbp/Downloads/FinalPdf.pdf")
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div[2]/div/div/div/div/div[3]/button[1]").click()
    time.sleep(2)

    # Reference
    ref_name=ReferenceNo.reference_gen()
    driver.find_element_by_id("voucher-reference_no").send_keys(ref_name)

      # item add

    item_name=RandomItem.item_gen()
    driver.find_element_by_name("VoucherItem[0][description]").send_keys(item_name)
    time.sleep(1)


    qty_name=RandomItem.qty_gen()
    driver.find_element_by_id("voucheritem-0-quantity").send_keys(qty_name)
    time.sleep(1)

    price_name=RandomItem.price_gen()
    driver.find_element_by_id("voucheritem-0-unit_price").send_keys(price_name)
    time.sleep(1)
    print('err',driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[2]/div/div/form/div[1]/div/div[4]/div/div/div/table/tbody[1]/tr/td[3]/div/p").text)
    print('err',driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[2]/div/div/form/div[1]/div/div[4]/div/div/div/table/tbody[2]/tr[2]/td[7]/p").text)

    file = open('voucher.txt', 'w+')
    item=item_name[0:5]
    qty=qty_name[0:3]
    price=price_name[0:3]
    print(type(qty_name))
    All_value = item+"..." + qty+"..."+ price+"..."
    print("all_value: ", All_value)
    file.write(All_value + '\t\n')
    file.close()


    driver.find_element_by_id("select2-voucheritem-0-chart_of_account_id-container").click()
    driver.find_element_by_xpath("/html/body/span/span/span[1]/input").send_keys("of")
    webElemList = []
    time.sleep(1)
    optionlist = driver.find_element_by_xpath("/html/body/span/span/span[1]/input")

    optionlist.find_element_by_xpath("/html/body/span/span/span[2]/ul/li[3]").click()

    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[2]/div/div/form/div[2]/button").click()
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[2]/div/div/form/div[2]/div/button[2]").click()
    time.sleep(4)




login_test()
voucher_create()

