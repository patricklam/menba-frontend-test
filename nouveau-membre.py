from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from _credentials import password

# Create a new instance of the Firefox driver
driver = webdriver.Firefox()

mail_address = 'sensenearridebicycle@gmail.com'

# https://gist.github.com/ikegami-yukino/51b247080976cb41fe93
UA = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:25.0) Gecko/20100101 Firefox/25.0'
PHANTOMJS_ARG = {'phantomjs.page.settings.userAgent': UA}

try:
    url = 'https://www.google.com/accounts/Login?hl=en&continue=https://www.google.ca/'
    driver.get(url)

    driver.find_element_by_id("Email").send_keys(mail_address)
    driver.find_element_by_id("next").click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "Passwd")));
    driver.find_element_by_id("Passwd").send_keys(password)
    driver.find_element_by_id("signIn").click()

    # go to the google home page
    driver.get("http://test.menba.ca")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "dropDownUserClubs")))

    userClubs = driver.find_element_by_id("dropDownUserClubs")
    userClubs.click()
    userClubs.send_keys(Keys.ARROW_DOWN)
    userClubs.send_keys(Keys.ARROW_DOWN)

    club0 = driver.find_element_by_id("club-0")
    club0.click()

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "nouveauButton")))
    nouveauMembre = driver.find_element_by_id("nouveauButton")
    nouveauMembre.click()

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "identite")))
    # XXX make sure this actually loads that page

finally:
    driver.quit()
