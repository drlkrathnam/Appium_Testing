import time
import self
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver import Keys

desired_cap ={
  "platformName": "android",
  "appium:platformVersion": "7.1.2",
  "appium:deviceName": "google G011A",
  "appium:automationName": "appium",
  "appium:wdaConnectionTimeout": "950000"

}
driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_cap)
driver.find_element('xpath',"//android.widget.TextView[@bounds='[444,226][548,419]']").click()
driver.implicitly_wait(30)
driver.find_element('xpath',("//android.view.View[@content-desc=' Skip & Get Start']")).click()
driver.implicitly_wait(30)
driver.find_element('xpath',("//android.widget.EditText[@index='3']")).click()
driver.find_element('xpath',("//android.widget.EditText[@index='3']")).send_keys("6309692221")

touch_action = TouchAction(driver)
touch_action.press(x=501, y=984).release().perform()

driver.find_element('xpath','//android.view.View[@content-desc="Next"]').click()
time.sleep(5)

driver.find_element('xpath','//android.view.View[@bounds="[30,227][546,285]"]').click()
touch_action = TouchAction(driver)
touch_action.tap(x=333, y=257).perform()
time.sleep(3)

touch_action.tap(x=259, y=708).perform()
touch_action.tap(x=144, y=708).perform()
touch_action.tap(x=542, y=708).perform()
touch_action.tap(x=542, y=708).perform()
touch_action.tap(x=542, y=708).perform()
touch_action.tap(x=144, y=708).perform()

driver.implicitly_wait(3)
driver.find_element('xpath','//android.view.View[@bounds="[147,375][429,671]"]').click()
touch_action.tap(x=286, y=649).perform()