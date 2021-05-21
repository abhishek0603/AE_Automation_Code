# https://omni.annalect.com/
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver

caps = DesiredCapabilities.CHROME
caps['loggingPrefs'] = {'performance': 'ALL'}
driver = webdriver.Chrome(desired_capabilities=caps)

driver.get('https://omni.annalect.com/')

#login Field
driver.find_element_by_xpath(" ").send_keys("launch.demo@annalect.com")
#pass word field
driver.find_element_by_xpath(" ").send_keys("Broadc@st4206")
#Login Button click
driver.find_element_by_xpath("").click()
