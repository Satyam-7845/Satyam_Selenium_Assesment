# # 1
#
# import time
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option('detach', True)
# driver = webdriver.Chrome(opts)
#
# time.sleep(1)
# driver.get("https://demowebshop.tricentis.com/")
#
# time.sleep(1)
# driver.find_element('xpath', "(//a[contains(text(),'Books')])[1]").click()
# time.sleep(1)
# driver.find_element('xpath', "//a[text()='Computing and Internet']").click()
# time.sleep(1)
# driver.find_element('id', 'add-to-cart-button-13').click()
# time.sleep(1)
# driver.find_element('xpath', "//a[text()='Shopping cart']").click()
# time.sleep(1)
# product = driver.find_element("xpath", "//td[@class='product']")
# print("Product in cart:", product.text)

# #######################################################################
#
# # 2
#
# import time
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option('detach', True)
# driver = webdriver.Chrome(opts)
#
# time.sleep(1)
# driver.get("https://demowebshop.tricentis.com/")
#
# time.sleep(1)
# driver.find_element('xpath', "(//a[contains(text(),'Electronics')])[3]").click()
# time.sleep(1)
# driver.find_element('xpath', "(//a[contains(text(),'Cell phones')])[3]").click()
# time.sleep(1)

# #######################################################################
#
# # 3
#
# import time
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option('detach', True)
# driver = webdriver.Chrome(opts)
#
# time.sleep(1)
# driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
#
# time.sleep(1)
# driver.find_element('xpath', '//button[text()="Start"]').click()
# time.sleep(5)
# text = driver.find_element("xpath", "//h4").text
# print("Text displayed:", text)

# #######################################################################
#
# # 4
#
# import time
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option('detach', True)
# driver = webdriver.Chrome(opts)
#
# time.sleep(1)
# driver.get("https://the-internet.herokuapp.com/dynamic_controls")
#
# time.sleep(1)
# driver.find_element('xpath', '//button[text()="Remove"]').click()
# time.sleep(5)
# driver.find_element('xpath', '//button[text()="Add"]').click()
# time.sleep(1)

# #######################################################################
#
# # 5
#
# import time
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option('detach', True)
# driver = webdriver.Chrome(opts)
#
# time.sleep(1)
# driver.get("https://demoqa.com/select-menu")
# time.sleep(2)
#
# driver.find_element("xpath", "//div[@id='withOptGroup']").click()
# time.sleep(2)
#
# driver.find_element("xpath", "//div[text()='Group 2, option 1']").click()
# time.sleep(2)
#
# value = driver.find_element("xpath", "//div[contains(@class,'singleValue')]").text
#
# print("Selected value:", value)


# ##########################################################################
#
# # 7
#
# import time
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option('detach', True)
#
# driver = webdriver.Chrome(opts)
# ac = ActionChains(driver)
#
# driver.get("https://demoqa.com/menu/")
# time.sleep(1)
#
# item2 = driver.find_element('xpath', '//a[text()="Main Item 2"]')
# ac.move_to_element(item2).perform()
# time.sleep(2)
#
# subsub = driver.find_element('xpath', '//a[text()="SUB SUB LIST >>"]')
# ac.move_to_element(subsub).perform()
# time.sleep(2)
#
# driver.find_element('xpath', '//a[text()="Sub Sub Item 1"]').click()
# time.sleep(2)

# ###########################################################################
# # # # 8
#
# import time
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option('detach', True)
# driver = webdriver.Chrome(opts)
# ac = ActionChains(driver)
#
# time.sleep(1)
# driver.get("https://demoqa.com/droppable")
# time.sleep(3)
#
# drag = driver.find_element("xpath", "//div[@id='draggable']")
# drop = driver.find_element("xpath", "//div[@id='droppable']")
#
# action = ActionChains(driver)
#
# action.click_and_hold(drag).move_to_element(drop).release().perform()
#
# time.sleep(2)
#
# result = driver.find_element("xpath", "//div[@id='droppable']").text
# print(result)


# ##########################################################################
# #
# # # 9
#
# import time
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option('detach', True)
#
# driver = webdriver.Chrome(opts)
# driver.get("https://the-internet.herokuapp.com/upload")
#
# time.sleep(1)
# file1 = r'C:\Users\satya\PycharmProjects\Selenium_Project\Day_3\p1.py'
# driver.find_element('xpath', '//input[@id="file-upload"]').send_keys(file1)
# time.sleep(1)
# driver.find_element('id', 'file-submit').click()
# time.sleep(1)
#
# value = driver.find_element("xpath", "//div[contains(@class,'panel text-center')]").text
# print("Uploaded file:", value)

# ##########################################################################
# #
# # # 10
# import time
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
#
# opts.add_experimental_option('detach', True)
# driver = webdriver.Chrome(opts)
# driver.get("https://the-internet.herokuapp.com/download")
# time.sleep(2)
# driver.find_element('xpath', '//a[text()="test.txt"]').click()
# # it will get downloaded in default download folder

##########################################################################
# #
# # # 11
# #
# import time
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option('detach', True)
# driver = webdriver.Chrome(opts)
#
# time.sleep(1)
# driver.get("https://demowebshop.tricentis.com/")
#
# time.sleep(1)
# driver.find_element('xpath', "(//a[contains(text(),'Books')])[1]").click()
# time.sleep(1)
# driver.find_element('xpath', "//a[text()='Computing and Internet']").click()
# time.sleep(1)
# driver.find_element('id', 'add-to-cart-button-13').click()
# time.sleep(1)
# driver.find_element('xpath', "(//a[contains(text(),'Books')])[1]").click()
# time.sleep(1)
# driver.find_element('xpath', "//a[text()='Fiction']").click()
# time.sleep(1)
# driver.find_element('id', 'add-to-cart-button-45').click()
# time.sleep(1)
# driver.find_element('xpath', "//a[text()='Shopping cart']").click()
# time.sleep(1)
# product = driver.find_element("xpath", "//span[@class='cart-qty']")
# print("Product in cart:", product.text)

















