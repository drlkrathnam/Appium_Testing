from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.webdriver import WebDriver
from applitools.selenium.eyes import Eyes
eyes = Eyes()
eyes.api_key = 'etG0RfHu0w6SXPrHpRDAwFOWA107Jvb2irbzR4VmCaPUw110'

desired_cap ={

    "platformName": "android",
    "appium:platformVersion": "7.1.1",
    "appium:deviceName": "OnePlus A5010",
    "appium:automationName": "appium",
    "appium:app": "C:\\Users\\MSNRaju\\Downloads\\app-release.apk",
    "appPackage": "com.vivifyhealthcare.lifeeazy",
    "appWaitActivity": "com.vivifyhealthcare.lifeeazy.MainActivity"


}
driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_cap)
# print('ok')


eyes.open(driver=driver, app_name='lifeeazy', test_name='My first Appium web Python test!')

driver.find_element('xpath',("//android.widget.TextView[@bounds='[444,226][548,419]']")).click()

driver.implicitly_wait("30")
driver.find_element('xpath','//android.view.View[@bounds="[384,958][576,1023]"]').click()

driver.find_element('xpath','//android.view.View[@content-desc="My Details"]').click()

driver.find_element('xpath','//android.widget.EditText[@bounds="[16,404][560,479]"]').click()
driver.find_element('xpath','//android.view.View[@content-desc="Address InfoTab 2 of 2"]').click()
driver.find_element('xpath','//android.widget.EditText[@bounds="[16,392][560,493]"]').click()
driver.find_element('xpath','//android.widget.EditText[@bounds="[16,392][560,493]"]').send_keys(Visakapatnam)
