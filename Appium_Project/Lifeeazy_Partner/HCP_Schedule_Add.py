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
driver.implicitly_wait(30)

driver.find_element('xpath','//android.view.View[@bounds="[0,0][576,1024]"]').click()

touch_action = TouchAction(driver)
touch_action.press(x=95, y=385).perform()

driver.find_element('xpath','//android.widget.Button[@bounds="[0,29][57,86]"]').click()
driver.find_element('xpath','//android.view.View[@content-desc="My Profile"]').click()

# Schedule Add
driver.find_element('xpath','//android.view.View[@content-desc="Schedule"]').click()
driver.find_element('xpath','//android.view.View[@content-desc="Create Schedule"]').click()
driver.find_element('xpath','//android.view.View[@bounds="[14,120][282,195]"]').click()
driver.find_element('xpath','//android.view.View[@content-desc="Teleconsultation"]').click()
driver.find_element('xpath','//android.view.View[@content-desc="Select Clinic"]').click()

for i in range(30):
  driver.swipe(291, 701, 540, 489, 100)

driver.find_element('xpath','//android.view.View[@content-desc="Mounika clinicals"]').click()
driver.find_element('xpath','//android.view.View[@bounds="[14,219][281,294]"]').click()
driver.find_element('xpath','//android.view.View[@content-desc="5, Wednesday, April 5, 2023"]').click()
driver.find_element('xpath','//android.widget.Button[@content-desc="OK"]').click()
driver.find_element('xpath','//android.view.View[@bounds="[295,219][562,294]"]').click()
driver.find_element('xpath','//android.view.View[@content-desc="8, Saturday, April 8, 2023"]').click()
driver.find_element('xpath','//android.widget.Button[@content-desc="OK"]').click()

driver.find_element('xpath','//android.view.View[@bounds="[14,318][282,393]"]').click()
driver.find_element('xpath','//android.widget.Button[@bounds="[104,792][161,850]"]').click()
driver.find_element('xpath','//android.widget.EditText[@bounds="[121,441][234,537]"]').click()

touch_action = TouchAction(driver)
touch_action.press(x=358, y=913).perform()
touch_action.press(x=501, y=936).perform()
touch_action.press(x=501, y=936).perform()
touch_action.press(x=358, y=913).perform()
touch_action.press(x=323, y=342).perform()
touch_action.press(x=501, y=936).perform()
touch_action.press(x=501, y=936).perform()
touch_action.press(x=357, y=770).perform()
touch_action.press(x=218, y=983).perform()

driver.find_element('xpath','//android.widget.RadioButton[@content-desc="AM"]').click()
driver.find_element('xpath','//android.widget.Button[@content-desc="OK"]').click()
driver.find_element('xpath','//android.view.View[@bounds="[294,318][562,393]"]').click()
driver.find_element('xpath','//android.widget.Button[@bounds="[104,792][161,850]"]').click()

touch_action = TouchAction(driver)
touch_action.press(x=191, y=345).perform()
touch_action.press(x=217, y=771).perform()
touch_action.press(x=499, y=941).perform()
touch_action.press(x=499, y=941).perform()
touch_action.press(x=75, y=765).perform()
touch_action.press(x=75, y=765).perform()
touch_action.press(x=321, y=341).perform()
touch_action.press(x=499, y=941).perform()
touch_action.press(x=499, y=941).perform()
touch_action.press(x=359, y=775).perform()
touch_action.press(x=217, y=984).perform()

driver.find_element('xpath','//android.widget.RadioButton[@content-desc="AM"]').click()
driver.find_element('xpath','//android.widget.Button[@content-desc="OK"]').click()

driver.find_element('xpath','//android.widget.EditText[@bounds="[14,444][562,492]"]').click()
driver.find_element('xpath','//android.widget.EditText[@bounds="[14,444][562,492]"]').send_keys('10')

driver.find_element('xpath','//android.widget.EditText[@bounds="[14,544][562,591]"]').click()
driver.find_element('xpath','//android.widget.EditText[@bounds="[14,544][562,591]"]').send_keys('200')

touch_action = TouchAction(driver)
touch_action.tap(x=499,y=1022).perform()
driver.find_element('xpath','//android.view.View[@content-desc="Submit"]').click()
