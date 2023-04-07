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
driver.find_element('xpath','//android.view.View[@content-desc="Appointments"]').click()
driver.implicitly_wait(30)
driver.find_element('xpath','//android.widget.Button[@bounds="[498,98][556,148]"]').click()
driver.implicitly_wait(30)
driver.find_element('xpath','//android.widget.Button[@bounds="[355,165][556,222]"]').click()
driver.implicitly_wait(30)
driver.find_element('xpath','(//android.view.View[@content-desc="Accept"])[1]').click()
driver.implicitly_wait(30)
driver.find_element('xpath','//android.widget.Button[@bounds="[498,98][556,148]"]').click()
driver.find_element('xpath','//android.widget.Button[@bounds="[355,222][556,280]"]').click()

for i in range(2):
  touch_action = TouchAction(driver)
  touch_action.press(x=202,y=963).move_to(x=342,y=317).release().perform()
  time.sleep(5)

driver.find_element('xpath','(//android.view.View[@content-desc="View Details"])[3]').click()
driver.find_element('xpath','//android.view.View[@bounds="[483,863][549,929]"]').click()
driver.implicitly_wait(30)
driver.find_element('xpath','//android.widget.Button[@bounds="[235,889][341,967]"]').click()
driver.implicitly_wait(30)

driver.find_element('xpath','//android.view.View[@content-desc="Appointments"]').click()
driver.find_element('xpath','//android.widget.Button[@bounds="[498,98][556,148]"]').click()
driver.find_element('xpath','//android.widget.Button[@bounds="[355,222][556,280]"]').click()

for i in range(2):
  touch_action = TouchAction(driver)
  touch_action.press(x=202,y=963).move_to(x=342,y=317).release().perform()
  time.sleep(5)

driver.find_element('xpath','(//android.view.View[@content-desc="View Details"])[3]').click()

driver.find_element('xpath','//android.view.View[@content-desc="Add Prescription"]').click()
driver.find_element('xpath','//android.view.View[@bounds="[18,165][558,235]"]').click()
driver.find_element('xpath','//android.view.View[@content-desc="31, Friday, March 31, 2023"]').click()
driver.find_element('xpath','//android.widget.Button[@content-desc="OK"]').click()

driver.find_element('xpath','//android.widget.EditText[@bounds="[38,393][538,463]"]').click()
driver.find_element('xpath','//android.widget.EditText[@bounds="[38,393][538,463]"]').send_keys('CROCEN')

driver.find_element('xpath','//android.widget.EditText[@bounds="[38,463][538,533]"]').click()
driver.find_element('xpath','//android.widget.EditText[@bounds="[38,463][538,533]"]').send_keys('9')

driver.find_element('xpath','//android.widget.EditText[@bounds="[38,533][538,603]"]').click()
driver.find_element('xpath','//android.widget.EditText[@bounds="[38,533][538,603]"]').send_keys('Twice')
for i in range(1):
  touch_action = TouchAction(driver)
  touch_action.press(x=21, y=610).move_to(x=420, y=185).perform()

driver.find_element('xpath','//android.widget.EditText[@bounds="[38,386][538,456]"]').click()
driver.find_element('xpath','//android.widget.EditText[@bounds="[38,386][538,456]"]').send_keys('500 mg')

driver.find_element('xpath','//android.widget.EditText[@bounds="[38,456][538,526]"]').click()
driver.find_element('xpath','//android.widget.EditText[@bounds="[38,456][538,526]"]').send_keys('Oral')

driver.find_element('xpath','//android.widget.EditText[@bounds="[38,526][538,596]"]').click()
driver.find_element('xpath','//android.widget.EditText[@bounds="[38,526][538,596]"]').send_keys('Take medice after breakfast and lunch')
driver.find_element('xpath','//android.view.View[@content-desc="Prescribe"]').click()

