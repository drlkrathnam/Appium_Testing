import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


desired_cap ={
    "platformName": "android",
    "appium:platformVersion": "7.1.2",
    "appium:deviceName": "SM-G935FD",
    "appium:automationName": "appium"

}

driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_cap)

driver.find_element('xpath',"//android.widget.TextView[@bounds='[444,226][548,419]']").click()
driver.implicitly_wait(30)

el1 = driver.find_element('xpath','//android.view.View[@content-desc="Tele Consultation"]')
el1.click()

for i in range(4):
    touch_action = TouchAction(driver)
    touch_action.press(x=182,y=820).move_to(x=401,y=253).release().perform()
    time.sleep(3)

driver.implicitly_wait(30)

driver.find_element('xpath','(//android.view.View[@content-desc="Book"])[4]').click()
driver.implicitly_wait("50")
driver.find_element('xpath','//android.view.View[@content-desc="Venkata Rathnam Dare"]').click()
driver.implicitly_wait("50")
driver.find_element('xpath','//android.view.View[@content-desc="Vijay Bhargav"]').click()
driver.implicitly_wait("50")

driver.find_element('xpath','//android.view.View[@content-desc="Teleconsultation"]').click()
driver.implicitly_wait("50")

driver.find_element('xpath','//android.view.View[@content-desc="Home"]').click()
driver.implicitly_wait("50")

driver.find_element('xpath','//android.view.View[@content-desc="Add"]').click()
driver.implicitly_wait("50")

driver.find_element('xpath','//android.widget.EditText[@index="1"]').click()
driver.implicitly_wait("50")
driver.find_element('xpath','//android.widget.EditText[@index="1"]').send_keys("Fever")
driver.implicitly_wait("50")

driver.find_element('xpath','//android.widget.EditText[@index="2"]').click()
driver.implicitly_wait("50")
driver.find_element('xpath','//android.widget.EditText[@index="2"]').send_keys("Low Fever")
driver.implicitly_wait("50")

driver.find_element('xpath','//android.view.View[@content-desc="Add"]').click()
driver.implicitly_wait("50")

# driver.find_element('xpath','//android.widget.Button[@bounds="[484,565][541,622]"]').click()
# driver.implicitly_wait("50")


dt = '1'
day = 'Wednesday'

driver.find_element('xpath',f'//android.view.View[@content-desc="1, {day}, March {dt}, 2023"]').click()
driver.implicitly_wait("50")

# TOUCH ACTION METHOD
for i in range(4):
    touch_action = TouchAction(driver)
    touch_action.press(x=134,y=1004).move_to(x=362,y=152).release().perform()
    time.sleep(3)

driver.find_element('xpath','//android.view.View[@content-desc="9: 00 PM"]').click()
driver.implicitly_wait("50")

driver.find_element('xpath','//android.view.View[@content-desc="Confirm"]').click()
driver.implicitly_wait("50")
driver.find_element('xpath','//android.view.View[@content-desc="PAY"]').click()
driver.implicitly_wait("50")
driver.find_element('xpath','//android.view.View[@bounds="[59,315][518,391]"]').click()
driver.implicitly_wait("50")
driver.find_element('xpath','//android.view.View[@bounds="[266,190][306,249]"]').click()
driver.implicitly_wait("50")
driver.find_element('xpath','//android.widget.Button[@resource-id="redesign-v15-cta"]').click()
driver.implicitly_wait("50")
driver.find_element('xpath','//android.widget.Button[@text="Success"]').click()
driver.implicitly_wait("50")
el2 = driver.find_element('xpath','//android.view.View[@content-desc="Message Appointment Successfully CreatedDone"]')
el2.click()

# touch_action = TouchAction(driver)
# touch_action.press(x=289,y=646).release().perform()








