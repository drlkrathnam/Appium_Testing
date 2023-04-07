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

# EDUCATIONAL DETAILS ADD

driver.find_element('xpath','//android.view.View[@content-desc="Educational"]').click()
driver.implicitly_wait(10)

driver.find_element('xpath','//android.widget.EditText[@bounds="[30,96][546,171]"]').click()
driver.find_element('xpath','//android.widget.EditText[@bounds="[30,96][546,171]"]').send_keys('MBBS')

driver.find_element('xpath','//android.widget.EditText[@bounds="[30,171][546,245]"]').click()
driver.find_element('xpath','//android.widget.EditText[@bounds="[30,171][546,245]"]').send_keys('AU')

driver.find_element('xpath','//android.widget.EditText[@bounds="[30,245][546,320]"]').click()
driver.find_element('xpath','//android.widget.EditText[@bounds="[30,245][546,320]"]').send_keys('2020')

driver.find_element('xpath','//android.widget.EditText[@bounds="[30,320][546,395]"]').click()
driver.find_element('xpath','//android.widget.EditText[@bounds="[30,320][546,395]"]').send_keys('VISAKHAPATANAM')

driver.find_element('xpath','//android.view.View[@content-desc="ADD"]').click()

driver.find_element('xpath','//android.view.View[@bounds="[0,29][67,96]"]').click()



