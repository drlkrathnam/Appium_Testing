from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.webdriver import WebDriver
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
driver.find_element('xpath','//android.view.View[@bounds="[288,335][576,392]"]').click()
driver.find_element('xpath','//android.view.View[@bounds="[503,414][560,471]"]').click()
driver.find_element('xpath','//android.widget.EditText[@bounds="[57,46][566,103]"]').send_keys('Vivify healthcare private limited')
driver.find_element('xpath','//android.view.View[@bounds="[0,132][576,214]"]').click()

driver.find_element('xpath','//android.widget.EditText[@bounds="[16,717][560,821]"]').click()

touch_action = TouchAction(driver)
touch_action.press(x=219, y=843).release().perform()
touch_action.press(x=357, y=774).release().perform()
touch_action.press(x=216, y=983).release().perform()
touch_action.press(x=216, y=983).release().perform()
touch_action.press(x=216, y=983).release().perform()
touch_action.press(x=357, y=774).release().perform()
touch_action.press(x=501, y=986).release().perform()

touch_action.press(x=73, y=774).release().perform()
touch_action.press(x=216, y=774).release().perform()
touch_action.press(x=362, y=774).release().perform()
touch_action.press(x=77, y=843).release().perform()
touch_action.press(x=216, y=843).release().perform()
touch_action.press(x=360, y=843).release().perform()
touch_action.press(x=75, y=911).release().perform()
touch_action.press(x=218, y=915).release().perform()
touch_action.press(x=357, y=915).release().perform()
touch_action.press(x=503, y=984).release().perform()

driver.find_element('xpath','//android.view.View[@bounds="[131,375][445,671]"]').click()
touch_action.tap(x=286, y=649).perform()