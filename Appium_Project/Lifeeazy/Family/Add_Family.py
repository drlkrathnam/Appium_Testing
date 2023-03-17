import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


desired_cap ={

    "platformName": "android",
    "appium:platformVersion": "7.1.2",
    "appium:deviceName": "G011A",
    "appium:automationName": "appium"
}
driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_cap)

driver.find_element('xpath',"//android.widget.TextView[@bounds='[444,226][548,419]']").click()

driver.implicitly_wait(30)

driver.find_element('xpath','//android.view.View[@bounds="[384,958][576,1023]"]').click()

driver.find_element('xpath','//android.view.View[@content-desc="Family Members"]').click()

driver.find_element('xpath','//android.view.View[@content-desc="Add"]').click()

driver.find_element('xpath','//android.view.View[@bounds="[228,120][348,239]"]').click()
driver.find_element('xpath','//android.view.View[@content-desc="Gallery"]').click()
driver.find_element('xpath','//android.widget.ImageView[@resource-id="com.android.documentsui:id/icon_thumb"]').click()
time.sleep(5)
# touch_action = TouchAction(driver)
# touch_action.tap(x=277, y=565).perform()
# driver.implicitly_wait(10)
# touch_action.tap(x=108, y=197).perform()

driver.find_element('xpath','//android.widget.Button[@content-desc="Mr."]').click()

driver.find_element('xpath','//android.view.View[@content-desc="Mr."]').click()

driver.find_element('xpath','//android.widget.EditText[@bounds="[30,366][546,441]"]').click()

driver.find_element('xpath','//android.widget.EditText[@bounds="[30,366][546,441]"]').send_keys("ram")

driver.find_element('xpath','//android.widget.EditText[@bounds="[30,441][546,516]"]').click()

driver.find_element('xpath','//android.widget.EditText[@bounds="[30,441][546,516]"]').send_keys("krishna")

driver.find_element('xpath','//android.widget.Button[@content-desc="Male"]').click()
driver.find_element('xpath','//android.view.View[@content-desc="Female"]').click()

driver.find_element('xpath','//android.view.View[@bounds="[30,574][546,649]"]').click()

driver.find_element('xpath','//android.widget.Button[@content-desc="Select year"]').click()

# TOUCH ACTION METHOD
for i in range(3):
    touch_action = TouchAction(driver)
    touch_action.press(x=220,y=400).move_to(x=229,y=701).release().perform()
    time.sleep(3)

driver.find_element('xpath','//android.widget.Button[@content-desc="1980"]').click()
driver.find_element('xpath','//android.widget.Button[@bounds="[452,317][510,374]"]').click()
driver.find_element('xpath','//android.widget.Button[@bounds="[452,317][510,374]"]').click()
driver.find_element('xpath','//android.widget.Button[@bounds="[452,317][510,374]"]').click()

driver.find_element('xpath','//android.view.View[@content-desc="24, Thursday, April 24, 1980"]').click()
driver.find_element('xpath','//android.widget.Button[@content-desc="OK"]').click()

driver.find_element('xpath','//android.widget.Button[@content-desc="Martial Status"]').click()

driver.find_element('xpath','//android.view.View[@content-desc="Married"]').click()
driver.find_element('xpath','//android.widget.Button[@content-desc="Blood Group"]').click()
driver.find_element('xpath','//android.view.View[@content-desc="O+"]').click()

driver.find_element('xpath','//android.widget.EditText[@bounds="[30,764][546,839]"]').click()
driver.find_element('xpath','//android.widget.EditText[@bounds="[30,764][546,839]"]').send_keys("Fother")
driver.find_element('xpath','//android.widget.Button[@content-desc="ADULT"]').click()
driver.find_element('xpath','//android.view.View[@content-desc="ADULT"]').click()

driver.find_element('xpath','//android.widget.Switch[@bounds="[476,897][546,954]"]').click()
touch_action = TouchAction(driver)
touch_action.press(x=230, y=930).move_to(x=360, y=470).release().perform()

driver.find_element('xpath','//android.view.View[@content-desc="Add"]').click()

# driver.find_element('xpath','//android.view.View[@content-desc="Message Member Successfully added Done"]').click()

touch_action.press(x=288, y=651).perform()



