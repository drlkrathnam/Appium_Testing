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
driver.find_element('xpath','//android.view.View[@content-desc="Next"]').click()
# driver.find_element('co','//android.view.View[@content-desc="Next"]').click()
# driver.tap(positions=[(57,255)])


# driver.find_element('xpath',("//android.widget.EditText[@index='3']")).send_keys("6309692221")
time.sleep(10)
driver.find_element('xpath','//android.view.View[@bounds="[30,227][546,285]"]').click()
touch_action = TouchAction(driver)
touch_action.tap(x=333, y=257).perform()
driver.is_keyboard_shown()
# driver.find_element('xpath',("//android.widget.EditText[@index='3']")).click()
driver.find_element('xpath',("//android.widget.EditText[@index='3']")).send_keys("530003")
# driver.implicitly_wait(10)
# driver.find_element('xpath','//android.view.View[@bounds="[30,227][546,285]"]').set_value("5")
# driver.find_element('xpath','//android.view.View[@index="3"]').click()
# driver.find_element('xpath','//android.view.View[@bounds="[30,227][546,285]"]').send_keys('5')

# driver.find_element('xpath','//android.view.View[@bounds="[147,375][429,671]"]').click()