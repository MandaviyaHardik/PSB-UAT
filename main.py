import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
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
driver.find_element(By.ID,"propertyUniqueId").send_keys(52118050)
driver.find_element(By.ID,"propertyTypeId").click()
driver.find_element(By.XPATH,"/html/body/div[3]/div/div/div[1]/div[3]/div/div[2]/form/div[1]/div[1]/div[2]/div[2]/div/select/option[2]").click()
driver.find_element(By.ID,"propertySubTypeId").click()
driver.find_element(By.XPATH,"/html/body/div[3]/div/div/div[1]/div[3]/div/div[2]/form/div[1]/div[1]/div[2]/div[3]/div/select/option[2]").click()
driver.find_element(By.ID,"propertyTitleDeedTypeId").click()
driver.find_element(By.XPATH,"/html/body/div[3]/div/div/div[1]/div[3]/div/div[2]/form/div[1]/div[1]/div[2]/div[5]/div/select/option[2]").click()
driver.find_element(By.NAME,"borrowerName").send_keys("hardik")
driver.find_element(By.ID,"borrowerAddress").send_keys("Sarkhej - Gandhinagar Hwy, Thaltej, Ahmedabad, Gujarat 380054")
driver.find_element(By.ID,"isCoBorrowerAvailable").click()
driver.find_element(By.XPATH,"/html/body/div[3]/div/div/div[1]/div[3]/div/div[2]/form/div[1]/div[1]/div[2]/div[9]/div/select/option[3]").click()
driver.find_element(By.ID,"propertyOwnershipTypeId").click()
driver.find_element(By.XPATH,"/html/body/div[3]/div/div/div[1]/div[3]/div/div[2]/form/div[1]/div[1]/div[4]/div[5]/div/select/option[3]").click()
driver.find_element(By.ID,"address").send_keys("Sarkhej - Gandhinagar Hwy, Thaltej, Ahmedabad, Gujarat 380054")
driver.find_element(By.ID,"stateID").click()
driver.find_element(By.XPATH,"/html/body/div[3]/div/div/div[1]/div[3]/div/div[2]/form/div[1]/div[1]/div[4]/div[8]/div/select/option[12]").click()
driver.find_element(By.ID,"districtID").click()
driver.find_element(By.XPATH,"/html/body/div[3]/div/div/div[1]/div[3]/div/div[2]/form/div[1]/div[1]/div[4]/div[9]/div/select/option[8]").click()
driver.find_element(By.ID,"cityID").click()
driver.find_element(By.XPATH,"/html/body/div[3]/div/div/div[1]/div[3]/div/div[2]/form/div[1]/div[1]/div[4]/div[10]/div/select/option[2]").click()
driver.find_element(By.ID,"pincode").send_keys("361559")
driver.find_element(By.ID,"propertyPossessionTypeId").click()
driver.find_element(By.XPATH,"/html/body/div[3]/div/div/div[1]/div[3]/div/div[2]/form/div[1]/div[1]/div[4]/div[12]/div/select/option[2]").click()
driver.find_element(By.ID,"propertyPrice").send_keys("9900000")
driver.find_element(By.ID,"submitBtn").click()

time.sleep(5)
driver.find_element(By.XPATH,"/html/body/div[7]/div/div/div[2]/button[2]").click()
driver.find_element(By.XPATH,"/html/body/div[3]/div/div/div[1]/div[3]/div/div/form/div[2]/div/div/button[1]").click()
driver.find_element(By.NAME,"isMainImage").click()
driver.find_element(By.XPATH,"/html/body/div[3]/div/div/div[1]/div[3]/div/div/form/div[1]/div[1]/div[2]/div/div/div/select/option[2]").click()
time.sleep(6)
s = driver.find_element(By.NAME,"propertyImage")
s.send_keys(r"C:\Users\hardik.mandaviya\Desktop\Pi7_Tool_a2 (1).jpeg")
time.sleep(6)
driver.find_element(By.ID,"submitBtn").click()
time.sleep(5)
driver.find_element(By.XPATH,"//button[normalize-space()='OK']").click()
driver.find_element(By.XPATH,"/html/body/div[3]/div/div/div[1]/div[3]/div/div/div[3]/div[2]/div/div/a").click()

time.sleep(5)
driver.find_element(By.XPATH,"/html/body/div[3]/div/div/div[1]/div[3]/div/div/div[3]/form/div[1]/div[2]/div/div[1]/div[3]/div[2]/div/input").click()
time.sleep(50)
#upfile.send_keys(r"C:/Users/hardik.mandaviya/Downloads/View-Property-Details%20(1).pdf")
#driver.find_element(By.NAME,"description").send_keys("new file")
#driver.find_element(By.XPATH,"//button[@id='submitBtn']").click()
#time.sleep(100)


