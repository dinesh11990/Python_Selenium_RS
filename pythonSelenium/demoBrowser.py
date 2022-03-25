from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
#driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe")
#driver = webdriver.Ie(executable_path="C:\\IEDriverServer.exe")

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")
print(driver.title)
print(driver.current_url)
#driver.get("https://courses.rahulshettyacademy.com/courses")
#driver.minimize_window()
# driver.back()
# driver.refresh()
# driver.close()
driver.find_element_by_css_selector("input[name='name']").send_keys("Rahul")
driver.find_element_by_xpath("//input[@type='submit']").click()
print(driver.find_element_by_class_name("alert-success").text)


