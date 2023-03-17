import time

from appium import webdriver

desired_cap ={
    "platformName": "android",
    "appium:platformVersion": "7.1.2",
    "appium:deviceName": "G011A",
    "appium:automationName": "appium"
}

driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_cap)

driver.find_element('xpath',"//android.widget.TextView[@bounds='[444,226][548,419]']").click()
driver.implicitly_wait(30)
driver.find_element('xpath','//android.view.View[@content-desc="Vitals"]').click()
time.sleep(5)
driver.find_element('xpath','//android.view.View[@bounds="[288,957][576,1024]"]').click()
driver.implicitly_wait(30)
driver.find_element('xpath','//android.view.View[@content-desc="Venkata Rathnam Dare"]').click()
driver.implicitly_wait(30)
driver.find_element('xpath','//android.view.View[@bounds="[23,704][553,759]"]').click()
driver.implicitly_wait(30)

# Add Weight
driver.find_element('xpath','//android.view.View[@bounds="[29,196][288,351]"]').click()
driver.implicitly_wait(30)
driver.find_element('xpath','//android.view.View[@content-desc="Add Weight"]').click()
driver.implicitly_wait(30)
driver.find_element('xpath','//android.widget.EditText[@bounds="[288,114][564,171]"]').click()
driver.implicitly_wait(30)
driver.find_element('xpath','//android.widget.EditText[@bounds="[288,114][564,171]"]').send_keys('111')
driver.implicitly_wait(30)
driver.find_element('xpath','//android.view.View[@content-desc="Add"]').click()
time.sleep(10)

# Add Height
driver.find_element('xpath','//android.view.View[@content-desc="Family"]').click()
driver.implicitly_wait(30)
driver.find_element('xpath','//android.view.View[@content-desc="Venkata Rathnam Dare"]').click()
driver.implicitly_wait(30)
driver.find_element('xpath','//android.view.View[@content-desc="Vijay Bhargav"]').click()
driver.implicitly_wait(30)

driver.find_element('xpath','//android.view.View[@bounds="[288,196][547,351]"]').click()
driver.implicitly_wait(30)
driver.find_element('xpath','//android.view.View[@content-desc="Add Height"]').click()
driver.implicitly_wait(30)
driver.find_element('xpath','//android.widget.EditText[@index="1"]').click()
driver.implicitly_wait(30)
driver.find_element('xpath','//android.widget.EditText[@index="1"]').send_keys('111')
driver.implicitly_wait(30)
driver.find_element('xpath','//android.view.View[@content-desc="Add"]').click()
time.sleep(10)

# Add BMI
driver.find_element('xpath','//android.view.View[@content-desc="Family"]').click()
driver.implicitly_wait(30)
driver.find_element('xpath','//android.view.View[@content-desc="Venkata Rathnam Dare"]').click()
driver.implicitly_wait(30)
driver.find_element('xpath','//android.view.View[@content-desc="Vijay Bhargav"]').click()
driver.implicitly_wait(30)

driver.find_element('xpath','//android.view.View[@index="4"]').click()
driver.implicitly_wait(30)
driver.find_element('xpath','//android.view.View[@content-desc="Add BMI"]').click()
driver.implicitly_wait(30)
driver.find_element('xpath','//android.widget.EditText[@bounds="[300,114][564,171]"]').click()
driver.implicitly_wait(30)
driver.find_element('xpath','//android.widget.EditText[@bounds="[300,114][564,171]"]').send_keys('111')
driver.implicitly_wait(30)
driver.find_element('xpath','//android.view.View[@content-desc="Add"]').click()
time.sleep(10)

# Add Temperature
driver.find_element('xpath','//android.view.View[@content-desc="Family"]').click()
driver.implicitly_wait(30)
driver.find_element('xpath','//android.view.View[@content-desc="Venkata Rathnam Dare"]').click()
driver.implicitly_wait(30)
driver.find_element('xpath','//android.view.View[@content-desc="Vijay Bhargav"]').click()
driver.implicitly_wait(30)

driver.find_element('xpath','//android.view.View[@index="5"]').click()
driver.implicitly_wait(30)
driver.find_element('xpath','//android.view.View[@content-desc="Add Temperature"]').click()
driver.implicitly_wait(30)
driver.find_element('xpath','//android.widget.EditText[@bounds="[300,114][564,171]"]').click()
driver.implicitly_wait(30)
driver.find_element('xpath','//android.widget.EditText[@bounds="[300,114][564,171]"]').send_keys('111')
driver.implicitly_wait(30)
driver.find_element('xpath','//android.view.View[@content-desc="Add"]').click()
time.sleep(10)

# Add Spo2
driver.find_element('xpath','//android.view.View[@content-desc="Family"]').click()
driver.implicitly_wait(30)
driver.find_element('xpath','//android.view.View[@content-desc="Venkata Rathnam Dare"]').click()
driver.implicitly_wait(30)
driver.find_element('xpath','//android.view.View[@content-desc="Vijay Bhargav"]').click()
driver.implicitly_wait(30)

driver.find_element('xpath','//android.view.View[@index="6"]').click()
driver.implicitly_wait(30)
driver.find_element('xpath','//android.view.View[@content-desc="Add Spo2"]').click()
driver.implicitly_wait(30)
driver.find_element('xpath','//android.widget.EditText[@bounds="[300,114][564,171]"]').click()
driver.implicitly_wait(30)
driver.find_element('xpath','//android.widget.EditText[@bounds="[300,114][564,171]"]').send_keys('111')
driver.implicitly_wait(30)
driver.find_element('xpath','//android.view.View[@content-desc="Add"]').click()
time.sleep(10)

# Add BP
driver.find_element('xpath','//android.view.View[@content-desc="Family"]').click()
driver.implicitly_wait(30)
driver.find_element('xpath','//android.view.View[@content-desc="Venkata Rathnam Dare"]').click()
driver.implicitly_wait(30)
driver.find_element('xpath','//android.view.View[@content-desc="Vijay Bhargav"]').click()
driver.implicitly_wait(30)

driver.find_element('xpath','//android.view.View[@index="7"]').click()
driver.implicitly_wait(30)
driver.find_element('xpath','//android.view.View[@content-desc="Add BP"]').click()
driver.implicitly_wait(30)
driver.find_element('xpath','//android.widget.EditText[@bounds="[408,115][467,172]"]').click()
driver.implicitly_wait(30)
driver.find_element('xpath','//android.widget.EditText[@bounds="[408,115][467,172]"]').send_keys('111')
driver.implicitly_wait(30)
driver.find_element('xpath','//android.widget.EditText[@bounds="[482,115][541,172]"]').send_keys('11')
driver.implicitly_wait(30)
driver.find_element('xpath','//android.view.View[@content-desc="Add"]').click()
time.sleep(10)

# Add Pulse
driver.find_element('xpath','//android.view.View[@content-desc="Family"]').click()
driver.implicitly_wait(30)
driver.find_element('xpath','//android.view.View[@content-desc="Venkata Rathnam Dare"]').click()
driver.implicitly_wait(30)
driver.find_element('xpath','//android.view.View[@content-desc="Vijay Bhargav"]').click()
driver.implicitly_wait(30)

driver.find_element('xpath','//android.view.View[@index="8"]').click()
driver.implicitly_wait(30)
driver.find_element('xpath','//android.view.View[@content-desc="Add Pulse"]').click()
driver.implicitly_wait(30)
driver.find_element('xpath','//android.widget.EditText[@bounds="[300,114][564,171]"]').click()
driver.implicitly_wait(30)
driver.find_element('xpath','//android.widget.EditText[@bounds="[300,114][564,171]"]').send_keys('111')
driver.implicitly_wait(30)
driver.find_element('xpath','//android.view.View[@content-desc="Add"]').click()
time.sleep(10)

driver.find_element('xpath','//android.view.View[@content-desc="Family"]').click()
driver.implicitly_wait(30)
driver.find_element('xpath','//android.view.View[@content-desc="Venkata Rathnam Dare"]').click()
driver.implicitly_wait(30)
driver.find_element('xpath','//android.view.View[@content-desc="Vijay Bhargav"]').click()

