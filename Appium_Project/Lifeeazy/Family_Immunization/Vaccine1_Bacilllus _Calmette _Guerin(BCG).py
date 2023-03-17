import time

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

# Vaccination--1 Bacilllus Calmette Guerin(BCG)

driver.find_element('xpath',("//android.view.View[@bounds='[288,769][552,909]']")).click()

time.sleep(5)
driver.find_element('xpath','//android.view.View[@bounds="[288,957][576,1024]"]').click()
driver.implicitly_wait(30)
driver.find_element('xpath','//android.view.View[@content-desc="sri    Lalitha"]').click()
driver.implicitly_wait(30)
driver.find_element('xpath','//android.view.View[@content-desc="Kiran Kumar"]').click()
driver.implicitly_wait(30)
driver.find_element('xpath',("//android.view.View[@bounds='[0,184][576,361]']")).click()
touch = TouchAction(driver)
touch.tap(x=526, y=218).perform()
driver.find_element('xpath',"//android.view.View[@bounds='[18,255][558,332]']").click()
driver.find_element('xpath','//android.widget.Button[@content-desc="Select year"]').click()
touch.press(x=289, y=442).move_to(x=338, y=476).release().perform()
driver.find_element('xpath','//android.widget.Button[@content-desc="1998"]').click()
driver.find_element('xpath','//android.widget.Button[@bounds="[452,317][510,374]"]').click()
driver.find_element('xpath','//android.widget.Button[@bounds="[452,317][510,374]"]').click()
driver.find_element('xpath','//android.widget.Button[@bounds="[452,317][510,374]"]').click()
driver.find_element('xpath','//android.widget.Button[@bounds="[452,317][510,374]"]').click()
driver.find_element('xpath','//android.widget.Button[@bounds="[452,317][510,374]"]').click()
driver.find_element('xpath','//android.widget.Button[@bounds="[452,317][510,374]"]').click()
driver.find_element('xpath','//android.widget.Button[@bounds="[452,317][510,374]"]').click()
driver.find_element('xpath','//android.widget.Button[@bounds="[452,317][510,374]"]').click()
driver.find_element('xpath','//android.view.View[@bounds="[381,527][443,577]"]').click()
driver.find_element('xpath','//android.widget.Button[@content-desc="OK"]').click()
driver.find_element('xpath',"//android.view.View[@bounds='[48,550][558,826]']").click()
touch.press(x=300, y=790).perform()
driver.implicitly_wait(30)
driver.find_element('xpath','//android.view.View[@content-desc="Gallery"]').click()
driver.implicitly_wait(30)
driver.find_element('xpath',("//android.widget.RelativeLayout[@bounds='[201,275][375,347]']")).click()
driver.implicitly_wait(30)
driver.find_element('xpath',("//android.view.View[@content-desc='Submit']")).click()
driver.find_element('xpath',('//android.view.View[@bounds="[147,375][429,671]"]')).click()
touch.tap(x=286, y=649).perform()
