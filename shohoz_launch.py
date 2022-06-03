import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

url = "https://www.shohoz.com/launch/"
# web driver import with path
# PATH = '../../Documents/Python_Scripts\chromedriver.exe'
# browser = webdriver.Chrome(PATH)

browser.get(url)

browser.implicitly_wait(30)
time.sleep(10)

# Current Time
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
timeOff1 = now.strftime("23:45:00")
timeOff2 = now.strftime("7:55:00")
print("Current Time =", current_time)
print("Please try to login 8 AM to 11 PM")
if current_time < timeOff1 and current_time > timeOff2:
    print("Please Try to login After 8 AM")
    time.sleep(5)

browser.maximize_window()
browser.implicitly_wait(30)
# From Destination

destFrom = browser.find_element_by_xpath("//div[@class='form-group']//input[@id='dest_from']")
# destFrom.click()
destFromInput = input("Please Enter your from destination")
destFrom.send_keys(destFromInput)
destFromFinal = browser.find_element_by_xpath("//ul[@id='ui-id-1']//li[@class='ui-menu-item']//a")
destFromFinal.click()

browser.implicitly_wait(30)
# To Destination
destTo = browser.find_element_by_xpath("//div[@class='form-group']//input[@id='dest_to']")
# destTo.click()
destToInput = input("Please enter you destination name")
destTo.send_keys(destToInput)
destToFinal = browser.find_element_by_xpath("//ul[@id='ui-id-2']//li[@class='ui-menu-item']//a")
destToFinal.click()

browser.implicitly_wait(30)
# Date of Journey
journeyDateInput = browser.find_element_by_xpath("//div[@class='col-md-12']//div[@class='form-group']//input[@id='doj']")
journeyDate = browser.execute_script("arguments[0].removeAttribute('readonly')",
                                             WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH,
                                                                                                          "//div[@class='col-md-12']//div[@class='form-group']//input[@id='doj']"))))
journeyDateAvlbe = browser.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']//td[@data-event='click']//a[@class]")
# journeyDateAvlbeMonth = browser.find_elements(By.XPATH, "//table[@class= 'ui-datepicker-calendar']//tr//td[@data-event='click' ]//a").getattribute("data-month")
# journeyDateAvlbeYear = browser.find_elements(By.XPATH, "//table[@class= 'ui-datepicker-calendar']//tr//td[@data-event='click' ]//a").getattribute("data-year")
# print(journeyDateAvlbe.get_attribute("data-month"))
# print(journeyDateAvlbeYear)
journeyDateMonth = browser.find_element_by_xpath("//div[@class='ui-datepicker-title']//span[@class='ui-datepicker-month']")
print(journeyDateMonth.text)
journeyDateYear = browser.find_element_by_xpath("//div[@class='ui-datepicker-title']//span[@class='ui-datepicker-year']")
print(journeyDateYear.text)
print("Only 8 Days tickets are available")
for journeyDateAvlbeTxt in journeyDateAvlbe:
    print(journeyDateAvlbeTxt.text,"-",journeyDateMonth.text,"-",journeyDateYear.text)
journeyDateAvlbeInputCMD = input("Enter a date of journey")
browser.implicitly_wait(30)
journeyDateInput.send_keys(journeyDateAvlbeInputCMD)

time.sleep(10)
browser.implicitly_wait(30)
# Find Ticket Button
findTricketButton = browser.find_element_by_xpath("//form[@name='launchsearch']//div[@class='form-group']//button[@type='submit']")
findTricketButton.click()

browser.implicitly_wait(30)
# Trip All
tripAll = browser.find_elements_by_xpath("//table[@id='trips']//tr[@class='trip-row']")
for tripAllText in tripAll:
    print(tripAllText.text)
    print("--------------------------------------------")
    for tripAllTextId in tripAll:
        print(tripAllTextId.get_attribute("id"))
    print("---------------------------------------------")

browser.implicitly_wait(30)
# Select Cabin
tripFinalId = input("Please Enter your final trip ID from above")
tripViewSeatsButton = browser.find_element_by_xpath("//table[@id='trips']//td[@class='tbl_col6']//ul//li//button[@id='"+tripFinalId+"']")
tripViewSeatsButton.click()
time.sleep(10)

browser.implicitly_wait(30)
# Cabin-wise seat availability
tripAllFareHead = browser.find_elements_by_xpath("//div[@class='seat_layout clearfix']//table[@class='table table-striped']//th")
tripAllFare = browser.find_elements_by_xpath("//div[@class='seat_layout clearfix']//table[@class='table table-striped']//td")
for tripAllFareHeadText in tripAllFareHead:
    print(tripAllFareHeadText.text)
    print("--------------------------------------------")
    for tripAllFareText in tripAllFare:
        print(tripAllFareText.text)
    print("--------------------------------------------")

browser.implicitly_wait(30)
# Cabin Class
cabinClass = browser.find_elements_by_xpath("//div[@class='col-md-7']//select[@id='seatclass_select']//option[@value!=0]")
for cabinClassText in cabinClass:
    print(cabinClassText.text)
    print("-----------------------------------")
    print(cabinClassText.get_attribute("value"))
    print("-----------------------------------")
cabinClassInput = input("Please enter the value of cabin class")
cabinClassValue = browser.find_element_by_xpath("//div[@class='col-md-7']//select[@id='seatclass_select']//option[@value!=0][@value='"+cabinClassInput+"']")
cabinClassValue.click()

browser.implicitly_wait(30)
# Select Number of cabins
numberOfCabin = browser.find_elements_by_xpath("//div[@class='col-md-5']//select[@id='noofcabins']//option[@value!=0]")
for numberOfCabinText in numberOfCabin:
    print(numberOfCabinText.text)
numberOfCabinInput = input("Please enter number of cabin")
numberOfCabinValue = browser.find_element_by_xpath("//div[@class='col-md-5']//select[@id='noofcabins']//option[@value!=0][@value='"+numberOfCabinInput+"']")
numberOfCabinValue.click()

browser.implicitly_wait(30)
# Choose Boarding point
boardingPoint = browser.find_elements_by_xpath("//form[@id='confirmbooking']//div//div[@class='col-md-12']//select[@id='boardingpoint']//option[@value!=0]")
for boardingPointText in boardingPoint:
    print(boardingPointText.text)
    print("--------------------------")
    print(boardingPointText.get_attribute("value"))
boardingPointValue = input("Please Enter boarding point value")
boardingPointSelectedValue = browser.find_element_by_xpath("//form[@id='confirmbooking']//div//div[@class='col-md-12']//select[@id='boardingpoint']//option[@value!=0][@value='"+boardingPointValue+"']")
boardingPointSelectedValue.click()

browser.implicitly_wait(30)
# Total Payable amount
totalAmount = browser.find_element_by_xpath("//form[@id='confirmbooking']//div//div[@class='col-md-8']")
print(totalAmount.text)

browser.implicitly_wait(30)
# Final Continue Button
continueButton = browser.find_element_by_xpath("//form[@id='confirmbooking']//div//button[@id='continuebutton']")
continueButton.click()

browser.implicitly_wait(30)
# Journey Detail
journeyDetail = browser.find_elements_by_xpath("//aside[@id='journey']//ul//li")
for journeyDetailText in journeyDetail:
    print("Journey Detail")
    print(journeyDetailText.text)
    print("---------------------------------------")

browser.implicitly_wait(30)
# Passenger Detail
# Name
name = browser.find_element_by_xpath("//div[@id='p_contact']//input[@id='pname']")
name.click()
nameInput = input("Please Enter Passenger Name")
name.send_keys(nameInput)

browser.implicitly_wait(30)
# Age
age = browser.find_element_by_xpath("//div[@id='p_contact']//input[@id='page']")
age.click()
ageInput = input("Please Enter Passenger Age")
age.send_keys(ageInput)

browser.implicitly_wait(30)
# Gender
genderInput = input("Please Enter male or female")
if genderInput == "female":
    gender = browser.find_element_by_xpath("//div[@id='p_contact']//li[@class='srch_input_gender']//input[@id][@value='"+genderInput+"']")
    gender.click()

browser.implicitly_wait(30)
# Mobile
mobileNumber = browser.find_element_by_xpath("//div[@id='p_contact']//li[@class='srch_input_wd']//input[@id='pmobile']")
mobileNumber.click()
mobileNumberInput = input("Please Enter Mobile Number")
mobileNumber.send_keys(mobileNumberInput)

browser.implicitly_wait(30)
# Email
email = browser.find_element_by_xpath("//div[@id='p_contact']//li[@class='srch_input_wd']//input[@id='pemail']")
email.click()
emailInput = input("Please Enter Email Address")
email.send_keys(emailInput)

browser.implicitly_wait(30)
# bKash Online
bKashOnline = browser.find_element_by_xpath("//div[@id='payment_options']//div[@class='mid_cont_btn']//button[@name='bkash-online']")
bKashOnline.click()

finalConfirmation = input("Please type Done after Payment")
time.sleep(60)
if finalConfirmation == "Done":
    print("Please Check you Email for Ticket")
    time.sleep(1000)
    browser.quit()


# This is a online payment gateway system so I didn't worked yet


time.sleep(100000)
