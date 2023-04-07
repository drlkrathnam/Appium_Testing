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
driver.find_element('xpath','//android.view.View[@content-desc="CertifiedHCP"]').click()

driver.find_element('xpath','//android.view.View[@bounds="[74,376][502,670]"]').click()

touch_action = TouchAction(driver)
touch_action.tap(x=286, y=649).perform()

driver.find_element('xpath','//android.widget.Button[@bounds="[0,29][57,86]"]').click()
driver.find_element('xpath','//android.view.View[@content-desc="My Profile"]').click()

# Personal Information Add

driver.find_element('xpath','//android.view.View[@content-desc="Personal Information"]').click()
driver.find_element('xpath','//android.view.View[@bounds="[228,120][348,239]"]').click()
driver.find_element('xpath','//android.view.View[@content-desc="Gallery"]').click()
driver.find_element('xpath','//android.widget.RelativeLayout[@bounds="[17,275][191,347]"]').click()

driver.find_element('xpath','//android.view.View[@bounds="[489,620][546,677]"]').click()
driver.find_element('xpath','//android.widget.EditText[@bounds="[57,46][566,103]"]').send_keys('vivify healthcare private limited')
driver.find_element('xpath','//android.view.View[@bounds="[0,132][576,214]"]').click()
driver.find_element('xpath','//android.widget.EditText[@bounds="[30,774][546,849]"]').click()

for i in range(1):
  touch_action = TouchAction(driver)
  touch_action.press(x=16,y=556).move_to(x=412,y=127).release().perform()
  time.sleep(3)

touch_action = TouchAction(driver)
touch_action.press(x=501,y=913).perform()
touch_action.press(x=216,y=842).perform()
touch_action.press(x=360,y=774).perform()
touch_action.press(x=218,y=984).perform()
touch_action.press(x=218,y=984).perform()
touch_action.press(x=218,y=984).perform()
touch_action.press(x=360,y=774).perform()
touch_action.press(x=503,y=992).perform()

driver.find_element('xpath','//android.view.View[@content-desc="ADD PROFILE"]').click()
driver.find_element('xpath','//android.widget.Button[@content-desc="Back"]').click()




















