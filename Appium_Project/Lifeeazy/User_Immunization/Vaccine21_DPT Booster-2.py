from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

desired_cap ={
    "platformName": "android",
    "appium:platformVersion": "7.1.2",
    "appium:deviceName": "google G011A",
    "appium:automationName": "appium",
    "appium:wdaConnectionTimeout": "950000"
}

driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_cap)
driver.find_element('xpath',("//android.widget.TextView[@bounds='[444,226][548,419]']")).click()
driver.implicitly_wait(30)

# Vaccination--21 DPT Booster-2

driver.find_element('xpath',"//android.view.View[@bounds='[288,769][552,909]']").click()
driver.implicitly_wait(10)
for i in range(6):
    touch = TouchAction(driver)
    # touch.press(x=127, y=874).move_to(x=373, y=217).release().perform()
    touch.press(x=175, y=909).move_to(x=348, y=241).release().perform()


driver.find_element('xpath',"//android.view.View[@bounds='[0,604][576,780]']").click()

touch = TouchAction(driver)
touch.tap(x=526, y=635).perform()

driver.find_element('xpath',"//android.view.View[@bounds='[18,255][558,332]']").click()
driver.find_element('xpath','//android.widget.Button[@content-desc="Select year"]').click()
touch.press(x=216, y=687).move_to(x=344, y=430).release().perform()
driver.find_element('xpath','//android.widget.Button[@content-desc="2013"]').click()
driver.find_element('xpath','//android.widget.Button[@bounds="[452,317][510,374]"]').click()
driver.find_element('xpath','//android.widget.Button[@bounds="[452,317][510,374]"]').click()
driver.find_element('xpath','//android.widget.Button[@bounds="[452,317][510,374]"]').click()
driver.find_element('xpath','//android.widget.Button[@bounds="[452,317][510,374]"]').click()
driver.find_element('xpath','//android.widget.Button[@bounds="[452,317][510,374]"]').click()
driver.find_element('xpath','//android.widget.Button[@bounds="[452,317][510,374]"]').click()
driver.find_element('xpath','//android.view.View[@bounds="[71,577][133,627]"]').click()
driver.find_element('xpath','//android.widget.Button[@content-desc="OK"]').click()
driver.find_element('xpath',"//android.view.View[@bounds='[48,550][558,826]']").click()
touch.press(x=301, y=795).perform()
driver.implicitly_wait(30)
driver.find_element('xpath','//android.view.View[@content-desc="Gallery"]').click()
driver.implicitly_wait(30)
driver.find_element('xpath',"//android.widget.RelativeLayout[@bounds='[17,275][191,347]']").click()
driver.implicitly_wait(30)
driver.find_element('xpath',("//android.view.View[@content-desc='Submit']")).click()
driver.find_element('xpath','//android.view.View[@bounds="[147,375][429,671]"]').click()
touch.tap(x=286, y=649).perform()
