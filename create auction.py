import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.implicitly_wait(7)
driver.maximize_window()
driver.get("https://uat.ebkray.in/")

#logout and login for maker ( create auction )
driver.find_element(By.XPATH,"//span[normalize-space()='Login']").click()
driver.find_element(By.ID,"username").send_keys("shreya")
driver.find_element(By.ID,"password").send_keys("Tender@123")
driver.find_element(By.ID,"loginBtn").click()

#click on property
driver.find_element(By.XPATH,"//div[normalize-space()='Property']").click()
driver.find_element(By.XPATH,"//a[normalize-space()='Search Property']").click()
driver.find_element(By.XPATH,"//a[normalize-space()='Approved']").click()
#manually need to select property
driver.find_element(By.XPATH,"//li[@class='TabbedPanelsTab']//a[contains(text(),'Auction')]").click()
driver.find_element(By.LINK_TEXT,"Create").click()
driver.find_element(By.XPATH,"//button[normalize-space()='OK']").click()

#create auction notice
driver.find_element(By.ID,"authorizedOfficerName").send_keys("hardik mandaviaya")
driver.find_element(By.ID,"contactDetails").send_keys("1234567891")
#select dates manually
time.sleep(35)
driver.find_element(By.ID,"startPrice").send_keys("55000")
driver.find_element(By.ID,"decrementPrice").send_keys("1000")
driver.find_element(By.ID,"decrementPriceExtension").send_keys("5000")
driver.find_element(By.ID,"extendedWhen").send_keys("2")
driver.find_element(By.ID,"extendedBy").send_keys("5")
driver.find_element(By.XPATH,"//button[@id='submitBtn']").click()
driver.find_element(By.XPATH,"//button[normalize-space()='OK']").click()

driver.find_element(By.ID,"description").send_keys("")
driver.find_element(By.XPATH,"//a[@class='ep-button xs-btn-block']").click()

time.sleep(35)