from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.maximize_window()
driver.get("https://login.salesforce.com/?locale=eu")
driver.find_element_by_css_selector("#username").send_keys("krishna")
driver.find_element_by_css_selector(".password").send_keys("kumar")
driver.find_element_by_css_selector(".password").clear()
driver.find_element_by_link_text("Forgot Your Password?").click()

#genenerating based on tagname
#//tagname[tagname[text()='xxx']

driver.find_element_by_xpath("a[text()='Cancel']").click()
print(driver.find_element_by_xpath("//form[@name='login']/div[1]/label").text)
print(driver.find_element_by_css_selector("form[name='login'] label:nth-child(3)").text)
