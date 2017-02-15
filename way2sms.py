from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('http://site23.way2sms.com/content/index.html')

userid = driver.find_element_by_xpath("//input[@id='username']")    
userid.send_keys('YOUR MOBILE NUMBER')
time.sleep(1)

password = driver.find_element_by_xpath("//input[@id='password']")    
password.send_keys('YOUR PASSWORD')
time.sleep(1)

login=driver.find_element_by_xpath("//input[@id='loginBTN']")
login.click()

but=driver.find_element_by_xpath("//input[@class='button br3']")
but.click()

send_win=driver.find_element_by_xpath("//li[@id='sendSMS']//a")
send_win.click()

driver.switch_to.frame(driver.find_element_by_name("frame"))

target_mob=driver.find_element_by_xpath("//input[@id='mobile']")
target_mob.send_keys('RECIEVER MOBILE NUMBER')

target_msg=driver.find_element_by_xpath("//textarea[@id='message']")
target_msg.send_keys("ENTER YOUR MESSAGE")

send_button=driver.find_element_by_xpath("//input[@class='button br2up']")
send_button.click()
