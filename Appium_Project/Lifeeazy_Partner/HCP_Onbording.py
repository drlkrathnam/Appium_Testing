import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

desired_cap ={
  "platformName": "android",
  "appium:platformVersion": "7.1.2",
  "appium:deviceName": "google G011A",
  "appium:automationName": "appium"
}

driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_cap)

driver.find_element('xpath',"//android.widget.TextView[@text='Lifeeazy Partner']").click()
driver.implicitly_wait(30)

driver.find_element('xpath','//android.view.View[@content-desc="Skip & Get Start"]').click()

driver.implicitly_wait(30)
# NEW HCP REGISTER
driver.find_element('xpath','//android.view.View[@content-desc="Not SignedUp Yet ?  Register"]').click()

driver.find_element('xpath','//android.widget.EditText[@bounds="[160,211][546,268]"]').click()
driver.find_element('xpath','//android.widget.EditText[@bounds="[160,211][546,268]"]').send_keys('2086213307')

driver.find_element('xpath','//android.view.View[@content-desc="Next"]').click()
time.sleep(20)
# ENTER OTP


driver.find_element('xpath','//android.widget.EditText[@index="1"]').click()
driver.find_element('xpath','//android.widget.EditText[@index="1"]').send_keys('Bhavani')


driver.find_element('xpath','//android.widget.EditText[@bounds="[30,272][546,347]"]').click()
driver.find_element('xpath','//android.widget.EditText[@bounds="[30,272][546,347]"]').send_keys('Balireddy')

driver.find_element('xpath','//android.widget.EditText[@bounds="[30,347][546,422]"]').click()
driver.find_element('xpath','//android.widget.EditText[@bounds="[30,347][546,422]"]').send_keys('bmounika@vivifyhealthcare.com')

driver.find_element('xpath','//android.widget.EditText[@bounds="[30,422][546,496]"]').click()
driver.find_element('xpath','//android.widget.EditText[@bounds="[30,422][546,496]"]').send_keys('Bhavani')

driver.find_element('xpath','//android.widget.EditText[@bounds="[30,496][546,600]"]').click()
driver.find_element('xpath','//android.widget.EditText[@bounds="[30,496][546,600]"]').send_keys('Test@1234')

for i in range(2):
  touch_action = TouchAction(driver)
  touch_action.press(x=18,y=507).move_to(x=421,y=155).release().perform()
  time.sleep(5)

driver.find_element('xpath', '//android.widget.EditText[@bounds="[30,536][546,610]"]').click()
driver.find_element('xpath', '//android.widget.EditText[@bounds="[30,536][546,610]"]').send_keys('Test@1234')


driver.find_element('xpath','//android.view.View[@content-desc="Submit"]').click()
driver.find_element('xpath','//android.view.View[@content-desc="Go to Dashboard"]').click()
