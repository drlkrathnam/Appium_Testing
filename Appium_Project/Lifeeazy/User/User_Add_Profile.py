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

driver.find_element('xpath',("//android.widget.TextView[@bounds='[444,226][548,419]']")).click()

driver.implicitly_wait(30)

driver.find_element('xpath','//android.view.View[@bounds="[384,958][576,1023]"]').click()

driver.find_element('xpath','//android.view.View[@content-desc="My Details"]').click()

# ERROR MESSAGE
driver.find_element('xpath','//android.view.View[@bounds="[108,375][468,671]"]').click()

touch_action = TouchAction(driver)
touch_action.tap(x=286,y=649).perform()
touch_action.press(x=286,y=649).perform()
# touch_action.long_press(x=286,y=649).perform()

driver.find_element('xpath','//android.view.View[@bounds="[228,120][348,239]"]').click()
driver.find_element('xpath','//android.view.View[@content-desc="Gallery"]').click()
driver.find_element('xpath','//android.widget.ImageView[@bounds="[17,101][191,275]"]').click()
time.sleep(10)

driver.find_element('xpath','//android.widget.EditText[@bounds="[16,404][560,479]"]').click()
driver.find_element('xpath','//android.widget.EditText[@bounds="[16,404][560,479]"]').send_keys("Abhisheak")

driver.find_element('xpath','//android.widget.EditText[@bounds="[16,479][560,553]"]').click()
driver.find_element('xpath','//android.widget.EditText[@bounds="[16,479][560,553]"]').send_keys("Kumar")

driver.find_element('xpath','//android.widget.EditText[@bounds="[16,553][560,628]"]').click()
driver.find_element('xpath','//android.widget.EditText[@bounds="[16,553][560,628]"]').send_keys("rohitharathnam@gmail.com")

driver.find_element('xpath','//android.widget.Button[@content-desc="Mr."]').click()
driver.find_element('xpath','//android.view.View[@content-desc="Master"]').click()

driver.find_element('xpath','//android.widget.Button[@content-desc="Male"]').click()
driver.find_element('xpath','//android.view.View[@content-desc="Male"]').click()

driver.find_element('xpath','//android.view.View[@bounds="[503,753][560,810]"]').click()
driver.find_element('xpath','//android.widget.Button[@content-desc="Select year"]').click()

touch_action = TouchAction(driver)
touch_action.press(x=289, y=442).move_to(x=338, y=476).release().perform()

driver.find_element('xpath','//android.widget.Button[@content-desc="2008"]').click()

driver.find_element('xpath','//android.widget.Button[@bounds="[452,317][510,374]"]').click()
driver.find_element('xpath','//android.widget.Button[@bounds="[452,317][510,374]"]').click()
driver.find_element('xpath','//android.widget.Button[@bounds="[452,317][510,374]"]').click()

driver.find_element('xpath','//android.view.View[@bounds="[319,577][381,627]"]').click()
driver.find_element('xpath','//android.widget.Button[@content-desc="OK"]').click()
driver.find_element('xpath','//android.widget.Button[@content-desc="Martial Status"]').click()
driver.find_element('xpath','//android.view.View[@content-desc="Married"]').click()
driver.find_element('xpath','//android.widget.Button[@content-desc="Blood Group"]').click()
driver.find_element('xpath','//android.view.View[@content-desc="O+"]').click()
driver.find_element('xpath','//android.view.View[@content-desc="Add"]').click()
driver.find_element('xpath','//android.view.View[@bounds="[131,375][445,671]"]').click()
touch_action.tap(x=286, y=649).perform()


