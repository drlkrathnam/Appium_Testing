import time
import self
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
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


# PROFESSIONAL DETAILS ADD

driver.find_element('xpath','//android.view.View[@content-desc="Professional"]').click()
driver.implicitly_wait(30)

driver.find_element('xpath','//android.view.View[@content-desc="Tele Consultation"]').click()
driver.find_element('xpath','//android.view.View[@content-desc="At Home"]').click()

driver.find_element('xpath','//android.widget.EditText[@bounds="[30,208][546,283]"]').click()
driver.find_element('xpath','//android.widget.EditText[@bounds="[30,208][546,283]"]').send_keys('65932')

driver.find_element('xpath','//android.widget.EditText[@bounds="[30,283][546,358]"]').click()
driver.find_element('xpath','//android.widget.EditText[@bounds="[30,283][546,358]"]').send_keys('3')

driver.find_element('xpath','//android.widget.EditText[@bounds="[30,358][546,433]"]').click()
driver.find_element('xpath','//android.widget.EditText[@bounds="[30,358][546,433]"]').send_keys('21421')

driver.find_element('xpath','//android.widget.EditText[@bounds="[30,433][546,507]"]').click()
driver.find_element('xpath','//android.widget.EditText[@bounds="[30,433][546,507]"]').send_keys('3')

driver.find_element('xpath','//android.widget.Button[@content-desc="General Physician"]').click()
driver.find_element('xpath','//android.view.View[@content-desc="Dermatologists"]').click()

driver.find_element('xpath','//android.widget.EditText[@bounds="[30,565][546,640]"]').click()
driver.find_element('xpath','//android.widget.EditText[@bounds="[30,565][546,640]"]').send_keys('Skin Specialist')

for i in range(1):
  touch_action = TouchAction(driver)
  touch_action.press(x=20,y=501).move_to(x=396,y=200).release().perform()
  time.sleep(3)

driver.find_element('xpath','//android.view.View[@content-desc="Add your signature"]').click()

driver.find_element('xpath','//android.view.View[@bounds="[0,0][576,957]"]').click()
driver.find_element('xpath','//android.view.View[@content-desc="Save"]').click()

driver.find_element('xpath','//android.view.View[@content-desc="ADD"]').click()

driver.find_element('xpath','//android.view.View[@bounds="[0,29][67,96]"]').click()
