from datetime import time

from appium import webdriver

desired_cap ={
    "platformName": "android",
    "appium:platformVersion": "7.1.2",
    "appium:deviceName": "SM-G935FD",
    "appium:automationName": "appium",
    "appium:newCommandTimeout": "180000"
}

driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_cap)

driver.find_element('xpath',"//android.widget.TextView[@bounds='[444,226][548,419]']").click()
driver.implicitly_wait(30)
driver.find_element('xpath','//android.view.View[@content-desc="Vitals"]').click()

# Add Weight
driver.find_element('xpath','//android.view.View[@bounds="[29,148][288,304]"]').click()
driver.find_element('xpath','//android.view.View[@content-desc="Add Weight"]').click()
driver.find_element('xpath','//android.widget.EditText[@bounds="[288,114][564,171]"]').click()
driver.find_element('xpath','//android.widget.EditText[@bounds="[288,114][564,171]"]').send_keys('55')
driver.find_element('xpath','//android.view.View[@content-desc="Add"]').click()
driver.implicitly_wait(350)

# Add Height
driver.find_element('xpath','//android.view.View[@bounds="[288,148][547,304]"]').click()

driver.find_element('xpath','//android.view.View[@content-desc="Add Height"]').click()
driver.find_element('xpath','//android.widget.EditText[@index="1"]').click()
driver.find_element('xpath','//android.widget.EditText[@index="1"]').send_keys('55')
driver.find_element('xpath','//android.view.View[@content-desc="Add"]').click()
driver.implicitly_wait(450)

# Add BMI
driver.find_element('xpath','//android.view.View[@bounds="[29,304][288,459]"]').click()

driver.find_element('xpath','//android.view.View[@content-desc="Add BMI"]').click()
driver.find_element('xpath','//android.widget.EditText[@bounds="[300,114][564,171]"]').click()
driver.find_element('xpath','//android.widget.EditText[@bounds="[300,114][564,171]"]').send_keys('15')
driver.find_element('xpath','//android.view.View[@content-desc="Add"]').click()
driver.implicitly_wait(350)

# Add Temperature
driver.find_element('xpath','//android.view.View[@bounds="[288,304][547,459]"]').click()

driver.find_element('xpath','//android.view.View[@content-desc="Add Temperature"]').click()
driver.find_element('xpath','//android.widget.EditText[@bounds="[300,114][564,171]"]').click()
driver.find_element('xpath','//android.widget.EditText[@bounds="[300,114][564,171]"]').send_keys('75')
driver.find_element('xpath','//android.view.View[@content-desc="Add"]').click()
driver.implicitly_wait(450)

# Add Spo2
driver.find_element('xpath','//android.view.View[@bounds="[29,459][288,614]"]').click()

driver.find_element('xpath','//android.view.View[@content-desc="Add Spo2"]').click()
driver.find_element('xpath','//android.widget.EditText[@bounds="[300,114][564,171]"]').click()
driver.find_element('xpath','//android.widget.EditText[@bounds="[300,114][564,171]"]').send_keys('85')
driver.find_element('xpath','//android.view.View[@content-desc="Add"]').click()
driver.implicitly_wait(350)

# Add BP
driver.find_element('xpath','//android.view.View[@bounds="[288,459][547,614]"]').click()

driver.find_element('xpath','//android.view.View[@content-desc="Add BP"]').click()
driver.find_element('xpath','//android.widget.EditText[@bounds="[408,115][467,172]"]').click()
driver.find_element('xpath','//android.widget.EditText[@bounds="[408,115][467,172]"]').send_keys('120')
driver.find_element('xpath','//android.widget.EditText[@bounds="[482,115][541,172]"]').send_keys('53')
driver.find_element('xpath','//android.view.View[@content-desc="Add"]').click()
driver.implicitly_wait(350)

# Add Pulse
driver.find_element('xpath','//android.view.View[@bounds="[29,614][288,769]"]').click()

driver.find_element('xpath','//android.view.View[@content-desc="Add Pulse"]').click()
driver.find_element('xpath','//android.widget.EditText[@bounds="[300,114][564,171]"]').click()
driver.find_element('xpath','//android.widget.EditText[@bounds="[300,114][564,171]"]').send_keys('84')
driver.find_element('xpath','//android.view.View[@content-desc="Add"]').click()

