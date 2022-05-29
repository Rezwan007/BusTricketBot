import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

url = "https://eticket.railway.gov.bd/"
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

# login button
logIn = browser.find_element_by_xpath("//div[@class='container-wrapper']//nav[@class='main-navigation']//li//a[@title='Login']")
logIn.click()

# usernameinput = input("Please enter your EmailId")
# Xpath = //div[@class='login-form-control-single']//input[@type='tel']
username_textbox = browser.find_element_by_id("mobile_number")
username_textbox.click()
# username_textbox.send_keys("01741532908")
username_input = input("Please Input The Mobile Number")
username_textbox.send_keys(username_input)
# username_textbox.send_keys(usernameinput)

# passwordinput = input("Please Enter your Password")
# Xpath = //div[@class='login-form-control-single']//input[@type='password']
password_textbox = browser.find_element_by_id("password")
password_textbox.click()
# password_textbox.send_keys("Rezwan@007")
password_input = input("Please Input Password")
password_textbox.send_keys(password_input)
# password_textbox.send_keys(passwordinput)

browser.implicitly_wait(30)
# Final button fit for to login
loginButton1 = browser.find_element_by_xpath("//div[@class='login-form-control-single']//button[@class='login-form-submit-btn']")
time.sleep(10)
print("login Successful")
loginButton1.click()

browser.implicitly_wait(30)
# From Station
fromStation = browser.find_element_by_xpath("//div[@class='col-md-6']//input[@id='dest_from']")
fromStation.click()
fromStationInput = input("please Enter The From Station Name")
fromStation.send_keys(fromStationInput)
fromStationSelection = browser.find_element_by_xpath("//ul[@id='ui-id-1']//li[@class='ui-menu-item']//a[@class='ui-corner-all']")
fromStationSelection.click()

browser.implicitly_wait(30)
# To Station
toStation = browser.find_element_by_xpath("//div[@class='col-md-6']//input[@id='dest_to']")
toStation.click()
toStationInput = input("Please Input The Destination Station Name")
toStation.send_keys(toStationInput)
toStationInputSelection = browser.find_element_by_xpath("//ul[@id='ui-id-2']//li[@class='ui-menu-item']//a[@class='ui-corner-all']")
toStationInputSelection.click()

browser.implicitly_wait(30)
# Date of Journey
journeyDateInput = browser.find_element_by_xpath("//div[@class='col-md-6']//div[@class='form-group']//input[@id='doj']")
journeyDate = browser.execute_script("arguments[0].removeAttribute('readonly')",
                                             WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH,
                                                                                                          "//div[@class='col-md-6']//div[@class='form-group']//input[@id='doj']"))))
journeyDateAvlbe = browser.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']//td[@data-event='click']//a[@class]")
# journeyDateAvlbeMonth = browser.find_elements(By.XPATH, "//table[@class= 'ui-datepicker-calendar']//tr//td[@data-event='click' ]//a").getattribute("data-month")
# journeyDateAvlbeYear = browser.find_elements(By.XPATH, "//table[@class= 'ui-datepicker-calendar']//tr//td[@data-event='click' ]//a").getattribute("data-year")
# print(journeyDateAvlbe.get_attribute("data-month"))
# print(journeyDateAvlbeYear)
journeyDateMonth = browser.find_element_by_xpath("//div[@class='ui-datepicker-title']//span[@class='ui-datepicker-month']")
print(journeyDateMonth.text)
journeyDateYear = browser.find_element_by_xpath("//div[@class='ui-datepicker-title']//span[@class='ui-datepicker-year']")
print(journeyDateYear.text)
print("Only 5 Days tickets are available")
for journeyDateAvlbeTxt in journeyDateAvlbe:
    print(journeyDateAvlbeTxt.text,"-",journeyDateMonth.text,"-",journeyDateYear.text)
journeyDateAvlbeInputCMD = input("Enter a date of journey")
browser.implicitly_wait(30)
journeyDateInput.send_keys(journeyDateAvlbeInputCMD)

browser.implicitly_wait(30)
# Choose Class
chooseClassClick = browser.find_element_by_xpath("//div[@class='form-group']//select[@name='choose_class']")
chooseClassClick.click()
chooseClass = browser.find_elements_by_xpath("//div[@class='col-md-6']//div[@class='form-group']//select[@name='choose_class']")
for chooseClassTxt in chooseClass:
    print(chooseClassTxt.text)
chooseClassInput = input("Please Enter Your Journey Class From Above List")
chooseClassInputSelection = browser.find_element_by_xpath("//div[@class='col-md-6']//div[@class='form-group']//select[@name='choose_class']//option[@value='"+chooseClassInput+"']")
chooseClassInputSelection.click()

browser.implicitly_wait(30)
# Find Ticket Button
findTricketButton = browser.find_element_by_xpath("//div[@class='col-md-12']//div[@class='railway-ticket-search-submit-btn']//button[@type='submit']")
findTricketButton.click()

browser.implicitly_wait(30)
# Trip All
tripAll = browser.find_elements_by_xpath("//table[@id='trips']//tr[@class='trip-row'][@style !='display: none;']")
for tripAllText in tripAll:
    print(tripAllText.text)
    print("--------------------------------------------")
    for tripAllTextId in tripAll:
        print(tripAllTextId.get_attribute("id"))
    print("---------------------------------------------")


browser.implicitly_wait(30)
# View Seats Button
tripFinalId = input("Please Enter your final trip ID from above")
tripViewSeatsButton = browser.find_element_by_xpath("//table[@id='trips']//tr[@class='trip-row'][@style !='display: none;']//td[@class='tbl_col6 border-fix-seat']//ul//button[@id='"+tripFinalId+"']")
tripViewSeatsButton.click()
time.sleep(10)

browser.implicitly_wait(30)
# choosing seat
chooseSeat = browser.find_elements_by_xpath("//div[@class='col-md-6 seat_layout clearfix']//ul//li//a[@onclick='chooseSeat(this)']")
# for chooseSeatTxt in chooseSeat:
#     print(chooseSeatTxt.text)
#     print("--------------------------------------------------")
print("Avble Seat")
for chooseSeatTitle in chooseSeat:
    print(chooseSeatTitle.get_attribute("title"))

chooseSeatCMD = input("Please choose your seat from above list")
chooseSeatPath = browser.find_element_by_xpath("//div[@class='seat_layout clearfix ']//ul//li//a[@onclick='chooseSeat(this)'][@title='"+chooseSeatCMD+"']")
chooseSeatPath.click()

browser.implicitly_wait(30)
# Booking point
bookingPoint = browser.find_element_by_xpath("//div[@id='Div3']//div[@id='Div4']//form[@id='confirmbooking']//select[@id='boardingpoint']")
browser.implicitly_wait(30)
bookingPoint.click()
bookingPointAvlbe = browser.find_elements_by_xpath("//div[@id='Div3']//div[@id='Div4']//form[@id='confirmbooking']//select[@id='boardingpoint']//option[@value!=0]")
for bookingPointAvlbeTxt in bookingPointAvlbe:
    print(bookingPointAvlbeTxt.text)
    for bookingPointAvlbeValue in bookingPointAvlbe:
        print(bookingPointAvlbeValue.get_attribute("value"))
browser.implicitly_wait(30)

bookingPointCMD = input("Please Enter Your Booking point")
browser.implicitly_wait(30)
bookingPointAvlbeSelected = browser.find_element_by_xpath("//div[@id='Div3']//div[@id='Div4']//form[@id='confirmbooking']//select[@id='boardingpoint']//option[@value='"+bookingPointCMD+"']")
bookingPointAvlbeSelected.click()

browser.implicitly_wait(30)
# Continue Button
continueBtn = browser.find_element_by_xpath("//div[@id='Div3']//div[@id='Div4']//a[@onclick='submitConfirm(this)']")
continueBtn.click()

browser.implicitly_wait(30)
# Booked ticket detail
print("Journey Detail")
print("----------------------------------------------")
journeyDetail = browser.find_elements_by_xpath("//aside[@id='journey']//li")
for journeyDetailTxt in journeyDetail:
    print(journeyDetailTxt.text)
    print("----------------------------------------------")

browser.implicitly_wait(30)
# Total Amount Payable
payableAmount = browser.find_element_by_xpath("//div[@id='amnt_pay']")
print(payableAmount.text)

browser.implicitly_wait(30)
# bKash
bKash = browser.find_element_by_xpath("//div[@id='bKash']//div[@id='bkash_payment']")
bKash.click()

# browser.implicitly_wait(30)
# # Confirm Reservation
# confirmReservationBtn = browser.find_element_by_xpath("//div[@class='mid_cont_btn']//button[@id='confirm_button']")
# confirmReservationBtn.click()
# print("Please Pay The Amount Within 30 min")
#
# finalConfirmation = input("Please type Done after Payment")
# time.sleep(60)
# if finalConfirmation == "Done":
#     print("Please Check you Email for Ticket")
#     time.sleep(1000)
#     browser.quit()








time.sleep(100000)