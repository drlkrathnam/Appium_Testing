from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

desired_cap ={
  "platformName": "android",
  "appium:platformVersion": "7.1.2",
  "appium:deviceName": "google G011A",
  "appium:automationName": "appium"
}

driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_cap)

driver.find_element('xpath',"//android.widget.TextView[@text='Lifeeazy Partner']").click()
driver.implicitly_wait(30)
driver.find_element('xpath','//android.view.View[@content-desc="CertifiedHCP"]').click()
driver.implicitly_wait(30)
driver.find_element('xpath','//android.view.View[@bounds="[0,0][576,1024]"]').click()

touch_action = TouchAction(driver)
touch_action.press(x=95, y=385).perform()

driver.find_element('xpath','//android.widget.Button[@bounds="[0,29][57,86]"]').click()

driver.find_element('xpath','//android.view.View[@content-desc="Bank Details"]').click()
driver.find_element('xpath',"//android.widget.EditText[@bounds='[18,127][558,202]']").click()
driver.find_element('xpath',"//android.widget.EditText[@bounds='[18,127][558,202]']").send_keys('12345678912')

driver.find_element('xpath',"//android.widget.EditText[@bounds='[18,202][558,277]']").click()
driver.find_element('xpath',"//android.widget.EditText[@bounds='[18,202][558,277]']").send_keys('12345678912')

driver.find_element('xpath',"//android.widget.EditText[@bounds='[18,277][558,351]']").click()
driver.find_element('xpath',"//android.widget.EditText[@bounds='[18,277][558,351]']").send_keys('SBI')

driver.find_element('xpath',"//android.widget.EditText[@bounds='[18,351][558,426]']").click()
driver.find_element('xpath',"//android.widget.EditText[@bounds='[18,351][558,426]']").send_keys('SBIN0018886')

driver.find_element('xpath',"//android.widget.EditText[@bounds='[18,426][558,501]']").click()
driver.find_element('xpath',"//android.widget.EditText[@bounds='[18,426][558,501]']").send_keys('SBI')

driver.find_element('xpath',"//android.widget.EditText[@bounds='[18,501][558,576]']").click()
driver.find_element('xpath',"//android.widget.EditText[@bounds='[18,501][558,576]']").send_keys('BNZPM2504G')

touch_action = TouchAction(driver)
touch_action.tap(x=530, y=984).perform()

driver.find_element('xpath','//android.view.View[@content-desc="Upload Documents"]').click()
driver.find_element('xpath','//android.view.View[@content-desc="Gallery"]').click()
driver.find_element('xpath',"//android.widget.RelativeLayout[@bounds='[17,275][191,347]']").click()

driver.find_element('xpath',"//android.widget.EditText[@bounds='[18,711][558,814]']").click()

touch_action = TouchAction(driver)
touch_action.tap(x=398, y=909).perform()
touch_action.tap(x=485, y=769).perform()

driver.find_element('xpath','//android.view.View[@content-desc="ADD"]').click()



