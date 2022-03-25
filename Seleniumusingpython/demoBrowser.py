from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")
print(driver.title)
print(driver.current_url)


#driver.get("https://www.france24.com/en/")
#driver.minimize_window()
#driver.back()
#driver.refresh()
#driver.close()

#driver.find_element_by_name("name").send_keys("dinesh")
driver.find_element_by_css_selector("input[name='name']").send_keys("dinesh")
driver.find_element_by_xpath("//input[@type='submit']").click()

#While picking the class, you have select one particular class
#print(driver.find_element_by_class_name("alert-success").text)

#By using the CSS (its not working)
#print(driver.find_elements_by_css_selector("[class*='alert-success']").text)

#By using the Xpath
#print(driver.find_element_by_xpath("//*[contains(@class,'alert-success')]").text)
