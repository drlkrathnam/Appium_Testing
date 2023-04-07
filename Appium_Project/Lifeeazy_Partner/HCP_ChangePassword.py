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
driver.find_element('xpath','//android.view.View[@bounds="[0,0][576,1024]"]').click()

touch_action = TouchAction(driver)
touch_action.press(x=95, y=385).perform()

driver.find_element('xpath','//android.widget.Button[@bounds="[0,29][57,86]"]').click()
driver.find_element('xpath','//android.view.View[@content-desc="Change Password"]').click()
driver.find_element('xpath','//android.widget.EditText[@bounds="[168,216][546,273]"]').click()
driver.find_element('xpath','//android.widget.EditText[@bounds="[168,216][546,273]"]').send_keys('9390026223')

touch_action=TouchAction(driver)
touch_action.tap(x=501,y=984).perform()

driver.find_element('xpath','//android.view.View[@content-desc="Next"]').click()

# ENTER OTP

driver.find_element('xpath','//android.widget.EditText[@bounds="[30,206][546,309]"]').click()
driver.find_element('xpath','//android.widget.EditText[@bounds="[30,206][546,309]"]').send_keys('Test@1234')

driver.find_element('xpath','//android.widget.EditText[@bounds="[30,309][546,384]"]').click()
driver.find_element('xpath','//android.widget.EditText[@bounds="[30,309][546,384]"]').send_keys('Test@1234')
touch_action.tap(x=528,y=983).perform()
driver.find_element('xpath','//android.view.View[@bounds="[147,399][429,647]"]').click()
touch_action.tap(x=288,y=625).perform()
