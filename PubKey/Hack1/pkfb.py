from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# Logging in is just for testing
# Enter your own name, password, and profile name
# Not terribly robust, but I figured you have the FB graph API for logging in
# This is just to show that the public key field can be filled
usr = ""	# user name / email to log in 
pwrd = ""				# password
pk = ""

driver = webdriver.Firefox()
driver.get("https://www.facebook.com/")

# Opens FB, inputs credential, and signs in
assert "Facebook" in driver.title
eml = driver.find_element_by_id("email")
eml.send_keys(usr)
pas = driver.find_element_by_id("pass")
pas.send_keys(pwrd)
button = driver.find_element_by_id("loginbutton")
button.click()

# the below 3 blocks are just for navigation on FB
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "pagelet_welcome_box")))
prof = driver.find_element_by_xpath('//div[@class="clearfix"]')
prof.send_keys(Keys.NULL)
prof.click()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "fbTimelineHeadline")))
about = driver.find_element_by_link_text('About')
about.send_keys(Keys.NULL)
about.click()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "u_jsonp_3_2")))
nav = driver.find_element_by_xpath('//a[@data-testid="nav_contact_basic"]')
nav.send_keys(Keys.NULL)
nav.click()
#---------------

# opens the field for putting in the public key field 
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "_3hvd")))
link = driver.find_element_by_xpath('//a[@data-testid="add_public_key"]')
link.send_keys(Keys.NULL)
link.click()

# injects the public key to field
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "pgp_edit_textarea")))
pkfield = driver.find_element_by_id("pgp_edit_textarea")
pkfield.send_keys(Keys.NULL)
pkfield.send_keys(pk)

# clicks save
save = driver.find_element_by_xpath('//button[@name="__submit__"]')
save.send_keys(Keys.NULL)
save.click();
