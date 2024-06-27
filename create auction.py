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

time.sleep(30)

driver.find_element(By.ID,"startPrice").send_keys("55000")
driver.find_element(By.ID,"decrementPrice").send_keys("1000")
driver.find_element(By.ID,"decrementPriceExtension").send_keys("5000")
driver.find_element(By.ID,"extendedWhen").send_keys("2")
driver.find_element(By.ID,"extendedBy").send_keys("5")
driver.find_element(By.XPATH,"//button[@id='submitBtn']").click()
driver.find_element(By.XPATH,"//button[normalize-space()='OK']").click()

time.sleep(3)
#Upload Document

time.sleep(10)

driver.find_element(By.ID,"description").send_keys("new doc")
driver.find_element(By.XPATH,"//button[@id='submitBtn']").click()
driver.find_element(By.XPATH,"//a[@class='ep-button xs-btn-block']").click()

# Add Account Details for Remittance
driver.find_element(By.ID,"leiNo").send_keys("12598745632587965482")
driver.find_element(By.ID,"submitBtn").click()
driver.find_element(By.NAME,"sentTo").click()

dropele = driver.find_element(By.NAME,"sentTo")
select = Select(dropele)
select.select_by_index(1)
driver.find_element(By.ID,"remarks").send_keys("property has been sent")
driver.find_element(By.ID,"submitBtn").click()
time.sleep(2)
driver.find_element(By.XPATH,"//button[normalize-space()='OK']").click()

#logout and login with checker
driver.find_element(By.XPATH,"//a[normalize-space()='Logout']").click()
driver.find_element(By.ID,"username").send_keys("vaidehi.checker")
driver.find_element(By.ID,"password").send_keys("Tender@123")
driver.find_element(By.ID,"loginBtn").click()

#change tab to auction
driver.find_element(By.ID,"auctionTab").click()

time.sleep(3)
handles = driver.window_handles
driver.switch_to.window(handles[-1])
driver.find_element(By.ID,"action").click()
driver.find_element(By.XPATH,"/html/body/div[3]/div/div[1]/div/div[3]/div/div[1]/div[2]/form/div/div[5]/div/div/select/option[2]").click()
driver.find_element(By.ID,"remarks").send_keys("auction approved")
driver.find_element(By.ID,"confirmed").click()
driver.find_element(By.ID,"submitBtn").click()
time.sleep(2)
driver.find_element(By.XPATH,"//button[normalize-space()='OK']").click()


time.sleep(5)