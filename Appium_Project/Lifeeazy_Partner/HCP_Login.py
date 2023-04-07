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

driver.find_element('xpath','//android.widget.EditText[@bounds="[30,258][546,332]"]').click()
driver.find_element('xpath','//android.widget.EditText[@bounds="[30,258][546,332]"]').send_keys('9390026223')

driver.find_element('xpath','//android.widget.EditText[@bounds="[30,332][546,407]"]').click()
driver.find_element('xpath','//android.widget.EditText[@bounds="[30,332][546,407]"]').send_keys('Test@1234')

touch_action = TouchAction(driver)
touch_action.tap(x=530,y=981).perform()

driver.find_element('xpath','//android.view.View[@content-desc="CertifiedHCP"]').click()
