from datetime import datetime
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10)

driver.get('https://www.irctc.co.in/nget/train-search')
driver.maximize_window()
from_field = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="origin"]/span/input')))
from_field.send_keys('BRC')
from_field.send_keys(Keys.TAB)
# TO Destination
to_field = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="destination"]/span/input')))
to_field.send_keys('BZA')
to_field.send_keys(Keys.TAB)

# DATE
date_field = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="jDate"]/span/input')))
date_field.send_keys(datetime.strptime('16/03/2024', '%d/%m/%Y').strftime('%d/%m/%Y'))
date_field.send_keys(Keys.TAB)
wait.until(EC.invisibility_of_element_located((By.XPATH, '//*[@id="ui-datepicker-div"]')))
class_field = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="journeyClass"]/div/div[2]/span')))

# Click the class field
try:
    class_field.click()
except ElementClickInterceptedException:
    # If the click is intercepted, use JavaScript to click on the element
    driver.execute_script("arguments[0].click();", class_field)

# Wait
class1_field = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="journeyClass"]/div/div[4]/div/ul/p-dropdownitem[8]/li')))
# Click the class option
class1_field.click()
# Wait

find_field = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="journeyQuota"]/div/div[4]/div/ul/p-dropdownitem[6]/li/span')))
try:
    find_field.click()
except ElementClickInterceptedException:
    # If the click is intercepted, use JavaScript to click on the element
    driver.execute_script("arguments[0].click();", find_field)
    find_field.send_keys(Keys.TAB)

# Wait
search_field = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="divMain"]/div/app-main-page/div/div/div[1]/div[2]/div[1]/app-jp-input/div/form/div[5]/div[1]/button')))

# Click the search button
search_field.click()

# Wait for the passenger field to be visible and clickable
passenger_field = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="numberOfPassengers"]/div/label')))

# Click the passenger field
passenger_field.click()

# Wait for the passenger options to be visible and clickable
select_three = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="numberOfPassengers"]/div/div[4]/div/ul/li[4]')))

# Click the passenger option
select_three.click()

# Wait for the class field 1 to be visible and clickable
class_field1 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ui-accordiontab-0-content"]/div/div/form/div[1]/div[3]/p-dropdown/div/label')))

# Click the class field 1
class_field1.click()

# Wait for the class options 1 to be visible and clickable
class1_field1 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ui-accordiontab-0-content"]/div/div/form/div[1]/div[3]/p-dropdown/div/div[4]/div/ul/li[5]/span')))

# Click the class option 1
class1_field1.click()

# Wait for the modify search button to be visible and clickable
modify_search = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ui-accordiontab-0-content"]/div/div/form/div[1]/div[6]/button')))

# Click the modify search button
modify_search.click()

# Wait
check_avail = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="check-availability"]')))

# check availability button if necessary
driver.execute_script("arguments[0].scrollIntoView();", check_avail)

# Check availability button
check_avail.click()

# Wait
book_now = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ui-panel-0-content"]/div/div/div/table/tbody/tr/td[2]/div/div[3]/button')))

# Book now button
book_now.click()

# Wait
agree = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="divMain"]/div/app-train-list/div/p-confirmdialog[1]/div/div[3]/p-footer/div/button[2]/span[2]')))

# Click
agree.click()

# Wait
ok1_field = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="divMain"]/div/app-train-list/div/p-confirmdialog[2]/div/div[3]/p-footer/div/button[2]/span[2]')))

# OK1 button
ok1_field.click()

# Wait
username_field = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="userId"]')))

# Username
username_field.send_keys('username')

# Wait
password_field = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="pwd"]')))

# Send the password value
password_field.send_keys('password')

# Wait
captcha = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="nlpAnswer"]')))

# Send the captcha value
captcha.send_keys('your_captcha_value')

# Wait
sign_in = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="login_header_disable"]/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/button')))

# Click
sign_in.click()

# Quit the driver
driver.quit()
