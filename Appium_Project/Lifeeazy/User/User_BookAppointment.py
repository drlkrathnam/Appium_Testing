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

driver.find_element('xpath','//android.view.View[@content-desc="In-clinic"]').click()

driver.find_element('xpath','//android.view.View[@content-desc="Teleconsultation"]').click()

driver.find_element('xpath','//android.view.View[@content-desc="Add"]').click()

driver.find_element('xpath','//android.widget.EditText[@index="1"]').click()
driver.find_element('xpath','//android.widget.EditText[@index="1"]').send_keys("Fever")

driver.find_element('xpath','//android.widget.EditText[@index="2"]').click()
driver.find_element('xpath','//android.widget.EditText[@index="2"]').send_keys("Low Fever")

driver.find_element('xpath','//android.view.View[@content-desc="Add"]').click()

dt = '6'
day = 'Thursday'

driver.find_element('xpath',f'//android.view.View[@content-desc="6, {day}, April {dt}, 2023"]').click()

# TOUCH ACTION METHOD
for i in range(4):
    touch_action = TouchAction(driver)
    touch_action.press(x=134,y=1004).move_to(x=362,y=152).release().perform()
    time.sleep(2)

driver.find_element('xpath','//android.view.View[@content-desc="2: 00 PM"]').click()
for i in range(1):
  driver.swipe(291, 701, 540, 489, 100)

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
driver.find_element('xpath','//android.view.View[@bounds="[141,375][435,671]"]').click()
touch_action = TouchAction(driver)
touch_action.press(x=288,y=649).release().perform()








