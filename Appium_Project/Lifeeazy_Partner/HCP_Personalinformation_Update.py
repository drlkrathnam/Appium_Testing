import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


desired_cap ={
  "platformName": "android",
  "appium:platformVersion": "7.1.2",
  "appium:deviceName": "google G011A",
  "appium:automationName": "appium"
}

driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_cap)

driver.find_element('xpath',"//android.widget.TextView[@text='Lifeeazy Partner']").click()
driver.implicitly_wait(30)
driver.find_element('xpath','//android.view.View[@content-desc="CertifiedHCP"]').click()

driver.find_element('xpath','//android.view.View[@bounds="[0,0][576,1024]"]').click()

touch_action = TouchAction(driver)
touch_action.tap(x=157, y=481).perform()

driver.find_element('xpath','//android.widget.Button[@bounds="[0,29][57,86]"]').click()
driver.find_element('xpath','//android.view.View[@content-desc="My Profile"]').click()

# Personal Information Add

driver.find_element('xpath','//android.view.View[@content-desc="Personal Information"]').click()
driver.find_element('xpath','//android.widget.ImageView[@bounds="[228,120][348,239]"]').click()
driver.find_element('xpath','//android.view.View[@content-desc="Gallery"]').click()
driver.find_element('xpath','//android.widget.RelativeLayout[@bounds="[17,275][191,341]"]').click()
driver.find_element('xpath','//android.widget.EditText[@bounds="[30,299][546,367]"]').click()
driver.find_element('xpath','//android.widget.EditText[@bounds="[30,299][546,367]"]').clear()
driver.find_element('xpath','//android.widget.EditText[@bounds="[30,299][546,367]"]').send_keys('MounikaB')

driver.find_element('xpath','//android.widget.EditText[@bounds="[30,367][546,436]"]').click()
driver.find_element('xpath','//android.widget.EditText[@bounds="[30,367][546,436]"]').clear()
driver.find_element('xpath','//android.widget.EditText[@bounds="[30,367][546,436]"]').send_keys('Balireddy')

driver.find_element('xpath','//android.widget.EditText[@bounds="[30,436][546,505]"]').click()
driver.find_element('xpath','//android.widget.EditText[@bounds="[30,436][546,505]"]').clear()
driver.find_element('xpath','//android.widget.EditText[@bounds="[30,436][546,505]"]').send_keys('bmounika@vivifyhealthcare.com')

for i in range(1):
  driver.swipe(253, 594, 421, 160, 100)

driver.find_element('xpath','//android.view.View[@bounds="[489,163][546,220]"]').click()
driver.find_element('xpath','//android.widget.EditText[@bounds="[57,46][566,103]"]').send_keys('Vijayawada')
driver.find_element('xpath','//android.view.View[@content-desc="Vijayawada, Andhra Pradesh, India"]').click()

driver.find_element('xpath','//android.widget.EditText[@bounds="[30,306][546,375]"]').click()
driver.find_element('xpath','//android.widget.EditText[@bounds="[30,306][546,375]"]').clear()
driver.find_element('xpath','//android.widget.EditText[@bounds="[30,306][546,375]"]').send_keys('520075')

driver.find_element('xpath','//android.view.View[@content-desc="UPDATE PROFILE"]').click()
driver.close()




















