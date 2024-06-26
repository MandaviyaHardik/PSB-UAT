import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome()
driver.implicitly_wait(7)
driver.maximize_window()
driver.get("https://uat.ebkray.in/")

#login
driver.find_element(By.XPATH,"//span[normalize-space()='Login']").click()
driver.find_element(By.ID,"username").send_keys("shreya")
driver.find_element(By.ID,"password").send_keys("Tender@123")
driver.find_element(By.ID,"loginBtn").click()

#create property button
driver.find_element(By.XPATH,"//div[normalize-space()='Property']").click()
driver.find_element(By.XPATH,"//a[normalize-space()='Create Property']").click()

#create property page
driver.find_element(By.ID,"propertyUniqueId").send_keys(698899811)
driver.find_element(By.ID,"propertyTypeId").click()
driver.find_element(By.XPATH,"/html/body/div[3]/div/div/div[1]/div[3]/div/div[2]/form/div[1]/div[1]/div[2]/div[2]/div/select/option[2]").click()
driver.find_element(By.ID,"propertySubTypeId").click()
driver.find_element(By.XPATH,"/html/body/div[3]/div/div/div[1]/div[3]/div/div[2]/form/div[1]/div[1]/div[2]/div[3]/div/select/option[2]").click()
driver.find_element(By.ID,"propertyTitleDeedTypeId").click()
driver.find_element(By.XPATH,"/html/body/div[3]/div/div/div[1]/div[3]/div/div[2]/form/div[1]/div[1]/div[2]/div[5]/div/select/option[2]").click()
driver.find_element(By.NAME,"borrowerName").send_keys("hardik")
driver.find_element(By.ID,"borrowerAddress").send_keys("Sarkhej - Gandhinagar Hwy, Thaltej, Ahmedabad, Gujarat 380054")
driver.find_element(By.ID,"isCoBorrowerAvailable").click()
cobro = driver.find_element(By.ID,"isCoBorrowerAvailable")
select = Select(cobro)
select.select_by_index(1)
driver.find_element(By.NAME,"propertyDetailCoBorrowerDataBean[0].coBorrowerName").send_keys("hardik")
driver.find_element(By.NAME,"propertyDetailCoBorrowerDataBean[0].coBorrowerAddress").send_keys("jamnagar")
driver.find_element(By.ID,"propertyOwnershipTypeId").click()
driver.find_element(By.XPATH,"/html/body/div[3]/div/div/div[1]/div[3]/div/div[2]/form/div[1]/div[1]/div[4]/div[5]/div/select/option[3]").click()
driver.find_element(By.ID,"address").send_keys("Sarkhej - Gandhinagar Hwy, Thaltej, Ahmedabad, Gujarat 380054")
driver.find_element(By.ID,"stateID").click()
idstate = driver.find_element(By.ID,"stateID")
select = Select(idstate)
select.select_by_index(11)
driver.find_element(By.ID,"districtID").click()
idistrict = driver.find_element(By.ID,"districtID")
select = Select(idistrict)
select.select_by_index(1)
driver.find_element(By.ID,"cityID").click()
idcity = driver.find_element(By.ID,"cityID")
select = Select(idcity)
select.select_by_index(1)
driver.find_element(By.XPATH,"/html/body/div[3]/div/div/div[1]/div[3]/div/div[2]/form/div[1]/div[1]/div[4]/div[10]/div/select/option[2]").click()
driver.find_element(By.ID,"pincode").send_keys("361559")
driver.find_element(By.ID,"propertyPossessionTypeId").click()
driver.find_element(By.XPATH,"/html/body/div[3]/div/div/div[1]/div[3]/div/div[2]/form/div[1]/div[1]/div[4]/div[12]/div/select/option[2]").click()
driver.find_element(By.ID,"propertyPrice").send_keys("9900000")
driver.find_element(By.ID,"submitBtn").click()

#time.sleep(5)
driver.find_element(By.XPATH,"/html/body/div[7]/div/div/div[2]/button[2]").click()
driver.find_element(By.XPATH,"/html/body/div[3]/div/div/div[1]/div[3]/div/div/form/div[2]/div/div/button[1]").click()
driver.find_element(By.NAME,"isMainImage").click()
driver.find_element(By.XPATH,"/html/body/div[3]/div/div/div[1]/div[3]/div/div/form/div[1]/div[1]/div[2]/div/div/div/select/option[2]").click()
#time.sleep(6)
s = driver.find_element(By.NAME,"propertyImage")
s.send_keys(r"C:\Users\lenovo\Pictures\Screenshots\Screenshot 2024-06-20 011933.png")
#time.sleep(6)
driver.find_element(By.ID,"submitBtn").click()
#time.sleep(5)
driver.find_element(By.XPATH,"//button[normalize-space()='OK']").click()
driver.find_element(By.XPATH,"/html/body/div[3]/div/div/div[1]/div[3]/div/div/div[3]/div[2]/div/div/a").click()

#time.sleep(3)

time.sleep(12)
#Need to click browser and need to select PDF file
driver.find_element(By.NAME,"description").send_keys("new pdf")
driver.find_element(By.ID,"submitBtn").click()
driver.find_element(By.XPATH,"/html/body/div[3]/div/div/div[1]/div[3]/div/div/div[4]/div[2]/div/div/a").click()
driver.find_element(By.NAME,"sentTo").click()

dropele = driver.find_element(By.NAME,"sentTo")
select = Select(dropele)
select.select_by_index(1)

driver.find_element(By.ID,"remarks").send_keys("property has been sent")
driver.find_element(By.ID,"submitBtn").click()
driver.find_element(By.XPATH,"/html/body/div[5]/div/div/div[2]/button[2]").click()

#logout and login for checker
driver.find_element(By.XPATH,"//a[normalize-space()='Logout']").click()
driver.find_element(By.ID,"username").send_keys("vaidehi.checker")
driver.find_element(By.ID,"password").send_keys("Tender@123")
driver.find_element(By.ID,"loginBtn").click()
time.sleep(10)
handles = driver.window_handles
driver.switch_to.window(handles[-1])

driver.find_element(By.ID,"action").click()
driver.find_element(By.XPATH,"/html/body/div[3]/div/div/div[1]/div[3]/div/div/div[2]/form/div[1]/div[5]/div/div/div/select/option[2]").click()
driver.find_element(By.ID,"remarks").send_keys("property approved")
driver.find_element(By.ID,"confirmed").click()
driver.find_element(By.ID,"submitBtn").click()
driver.find_element(By.XPATH,"/html/body/div[5]/div/div/div[2]/button[2]").click()
time.sleep(5)

#logout and login for maker ( create auction )
driver.find_element(By.XPATH,"//a[normalize-space()='Logout']").click()
driver.find_element(By.ID,"username").send_keys("shreya")
driver.find_element(By.ID,"password").send_keys("Tender@123")
driver.find_element(By.ID,"loginBtn").click()

#click on property
driver.find_element(By.XPATH,"//div[normalize-space()='Property']").click()

