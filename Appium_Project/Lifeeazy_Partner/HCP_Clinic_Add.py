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

driver.find_element('xpath','//android.widget.Button[@bounds="[0,29][57,86]"]').click()
driver.find_element('xpath','//android.view.View[@content-desc="My Profile"]').click()

#Clinic Add

driver.find_element('xpath','//android.view.View[@content-desc="Clinic"]').click()
driver.find_element('xpath','//android.widget.EditText[@bounds="[24,96][552,171]"]').click()
driver.find_element('xpath','//android.widget.EditText[@bounds="[24,96][552,171]"]').send_keys('Mounica clinicals')

driver.find_element('xpath','//android.widget.EditText[@bounds="[24,171][552,245]"]').click()
driver.find_element('xpath','//android.widget.EditText[@bounds="[24,171][552,245]"]').send_keys('Hanumanthavaka, visakhapatanam')

touch_action = TouchAction(driver)
touch_action.press(x=532, y=981).perform()

driver.implicitly_wait(30)
driver.find_element('xpath','//android.view.View[@bounds="[0,29][67,96]"]').click()
