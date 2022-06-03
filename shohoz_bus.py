import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

url = "https://www.shohoz.com/bus-tickets"
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

# From Station
fromStation = browser.find_element_by_xpath("//div[@class='form-group']//input [@id='dest_from']")
fromStation.click()
fromStationInput = input("Please Enter you From City Name")
fromStation.send_keys(fromStationInput)
# fromStation.send_keys("Rangpur")
time.sleep(10)
fromStationName = browser.find_element_by_xpath("/html/body/ul[1]/li/a")
fromStationName.click()

browser.implicitly_wait(30)
# To Station
toStation = browser.find_element_by_xpath("//div[@class='form-group']//input [@id='dest_to']")
toStation.click()
toStationInput = input("Please input your to City Name")
toStation.send_keys(toStationInput)
# toStation.send_keys("Dhaka")
toStationName = browser.find_element_by_xpath("/html/body/ul[2]/li[1]/a")
toStationName.click()

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
for journeyDateAvlbeTxt in journeyDateAvlbe:
    print(journeyDateAvlbeTxt.text,"-May-2022")
journeyDateAvlbeInputCMD = input("Enter a date of journey")
browser.implicitly_wait(30)
journeyDateInput.send_keys(journeyDateAvlbeInputCMD)
# for journeyDateAvlbeTxt in journeyDateAvlbe:
#     journeyDateAvlbeInput = journeyDateAvlbeTxt.text
#     # error point
#     if  journeyDateAvlbeInput == journeyDateAvlbeInputCMD:
#         browser.implicitly_wait(30)
#         journeyDateAvlbeTxt.click()
#     else:
#         print("date not found !")
#     break

time.sleep(10)
browser.implicitly_wait(30)
# Date of Return
journeyDateReturn = browser.find_element_by_xpath("//div[@class='col-md-6']//div[@class='form-group']//input[@id='dor']")
journeyDateReturn.click()
journeyDateReturnAvlbe = browser.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']//td[@data-event='click']//a[@class]")
# journeyDateAvlbeMonth = browser.find_elements(By.XPATH, "//table[@class= 'ui-datepicker-calendar']//tr//td[@data-event='click' ]//a").getattribute("data-month")
# journeyDateAvlbeYear = browser.find_elements(By.XPATH, "//table[@class= 'ui-datepicker-calendar']//tr//td[@data-event='click' ]//a").getattribute("data-year")
# print(journeyDateAvlbe.get_attribute("data-month"))
# print(journeyDateAvlbeYear)
for journeyDateReturnAvlbeTxt in journeyDateReturnAvlbe:
    print(journeyDateReturnAvlbeTxt.text,"-May-2022")
print("Enter zero for null value")
journeyDateReturnInputCMD = input("Enter a date of return - Optional")
browser.implicitly_wait(30)
for journeyDateReturnAvlbeTxt in journeyDateReturnAvlbe:
    journeyDateReturnInput = journeyDateReturnAvlbeTxt.text

    if journeyDateReturnInput == journeyDateReturnInputCMD:
        browser.implicitly_wait(30)
        journeyDateReturnAvlbeTxt.click()
    if journeyDateReturnInput == 0 :
        continue

browser.implicitly_wait(30)
# Find Tricket
findTricket = browser.find_element_by_xpath("//div[@class='col-md-12']//button[@type='submit']")
findTricket.click()

# Choosing Operator System
browser.implicitly_wait(30)
operatorInput = input("Please enter your operator type Nabil or Hanif")
operatorInputHanif = "Hanif"
operatorInputNabil = "Nabil"
if operatorInput == operatorInputNabil:
    operatorN = browser.find_element_by_xpath("//div[@class='row']//label[@id='1operatorfilter']")
    operatorN.click()
    operatorNType = browser.find_element_by_xpath("//div[@class='row']//label[@id='1operatorfilter']//span[@class='label_name']")
    print(operatorNType.text)
if  operatorInput == operatorInputHanif:
    operatorH = browser.find_element_by_xpath("//div[@class='row']//label[@id='70operatorfilter']")
    operatorH.click()
    operatorHType = browser.find_element_by_xpath("//div[@class='row']//label[@id='70operatorfilter']//span[@class='label_name']")
    print(operatorHType.text)

# Choosing Operator Type AC or NonAC
browser.implicitly_wait(30)
operatorTypeInput = input("Please enter your operator type AC or NonAC")
operatorTypeInputAC = "AC"
operatorTypeInputNonAC = "NonAC"
if operatorTypeInput == operatorTypeInputAC:
    operatorTypeAC = browser.find_element_by_xpath("//div[@id='demo1']//label[@id='1typesfilter']")
    operatorTypeAC.click()
    operatorTypeACLabel = browser.find_element_by_xpath("//div[@id='demo1']//label[@id='1typesfilter']//span[@class='label_name']")
    print(operatorTypeACLabel.text)
if  operatorTypeInput == operatorTypeInputNonAC:
    operatorTypeNonAC = browser.find_element_by_xpath("//div[@id='demo1']//label[@id='2typesfilter']")
    operatorTypeNonAC.click()
    operatorTypeNonACLabel = browser.find_element_by_xpath("//div[@id='demo1']//label[@id='2typesfilter']//span[@class='label_name']")
    print(operatorTypeNonACLabel.text)

# Choosing Operator Departure Time
browser.implicitly_wait(30)
operatorDepartTime = input("Please enter your operator depart time morning or afternoon or night")
operatorDepartTimeMorning = "morning"
operatorDepartTimeAfternoon = "afternoon"
operatorDepartTimeNight = "night"
if operatorDepartTime == operatorDepartTimeMorning:
    operatorDepartTimeM = browser.find_element_by_xpath("//div[@id='demo5']//label[@id='6-12departure-time-filter-label']")
    operatorDepartTimeM.click()
    operatorDepartTimeMLabel = browser.find_element_by_xpath("//div[@id='demo5']//label[@id='6-12departure-time-filter-label']//span[@class='label_name']")
    print(operatorDepartTimeMLabel.text)
if  operatorDepartTime == operatorDepartTimeAfternoon:
    operatorDepartTimeA = browser.find_element_by_xpath("//div[@id='demo5']//label[@id='12-18departure-time-filter-label']")
    operatorDepartTimeA.click()
    operatorDepartTimeALabel = browser.find_element_by_xpath("//div[@id='demo5']//label[@id='12-18departure-time-filter-label']//span[@class='label_name']")
    print(operatorDepartTimeALabel.text)
if  operatorDepartTime == operatorDepartTimeNight:
    operatorDepartTimeN = browser.find_element_by_xpath("//div[@id='demo5']//label[@id='18-24departure-time-filter-label']")
    operatorDepartTimeN.click()
    operatorDepartTimeNLabel = browser.find_element_by_xpath("//div[@id='demo5']//label[@id='18-24departure-time-filter-label']//span[@class='label_name']")
    print(operatorDepartTimeNLabel.text)

browser.implicitly_wait(30)
# Trip list
tripAvlbAll = browser.find_elements_by_xpath("//div[@id='bus_tckt_rows']//table//tr[@style='display: table-row;'][@class='trip-row']")
for tripAvlbAllTxt in tripAvlbAll:
    print("Trip List")
    print(tripAvlbAllTxt.text)
    print("--------------------------------------------")
    for finalTripId in tripAvlbAll:
        print(finalTripId.get_attribute("id"))
    print("--------------------------------------------")

# # Trip List by individual label of operator

# tripAvlb = browser.find_elements_by_xpath("//div[@id='bus_tckt_rows']//table//tr[@style='display: table-row;']//td[@data-title='Operator']//ul//li")
# # for tripListAll in tripAvlbAll:
# print("Operation List")
# for tripAvlbTxt in tripAvlb:
#     print("Operation List")
#     print(tripAvlbTxt.text)

# print("Depart Time")
# tripAvlbDepTime = browser.find_elements_by_xpath("//div[@id='bus_tckt_rows']//table//tr[@style='display: table-row;']//td[@data-title='Dep. Time']")
# for tripAvlbDepTimeTxt in tripAvlbDepTime:
#     print("Depart Time")
#     print(tripAvlbDepTimeTxt.text)

# print("Arrival Time")
# tripAvlbArrTime = browser.find_elements_by_xpath("//div[@id='bus_tckt_rows']//table//tr[@style='display: table-row;']//td[@data-title='Arr. Time']")
# for tripAvlbArrTimeTxt in tripAvlbArrTime:
#     print("Arrival Time")
#     print(tripAvlbArrTimeTxt.text)

# print("Seat Available")
# tripAvlbSeatsAvailable = browser.find_elements_by_xpath("//div[@id='bus_tckt_rows']//table//tr[@style='display: table-row;']//td[@data-title='Seats Available']")
# for tripAvlbSeatsAvailableTxt in tripAvlbSeatsAvailable:
#     print("Seats Available")
#     print(tripAvlbSeatsAvailableTxt.text)

# print("Fare")
# tripAvlbFare = browser.find_elements_by_xpath("//div[@id='bus_tckt_rows']//table//tr[@style='display: table-row;']//td[@data-title='Fare']")
# for tripAvlbFareTxt in tripAvlbFare:
#     print("Fare")
#     print(tripAvlbFareTxt.text)

time.sleep(5)
browser.execute_script("window.scrollTo(0,400)")
time.sleep(5)

browser.implicitly_wait(30)
tripFinalId = input("Please Enter your final trip ID from above")
tripViewSeatsButton = browser.find_element_by_xpath("//div[@id='bus_tckt_rows']//table//tr[@style='display: table-row;']//button[@type='submit'] [@id='"+tripFinalId+"']//div[@class='view-seats-spinner']")
tripViewSeatsButton.click()
time.sleep(10)

time.sleep(5)
browser.execute_script("window.scrollTo(0,400)")
time.sleep(5)

browser.implicitly_wait(30)
# choosing seat
chooseSeat = browser.find_elements_by_xpath("//div[@class='seat_layout clearfix ']//ul//li//a[@onclick='chooseSeat(this)']")
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

# Passenger Detail

browser.implicitly_wait(30)
# Name
namePath = browser.find_element_by_xpath("//ul[@class='list-inline clearfix']//input[@id='pname']")
namePath.click()
name = input("Please Input Passenger Name")
namePath.send_keys(name)

browser.implicitly_wait(30)
# Gender
male= "M"
female= "F"
gender = input("Please Enter M or F")
browser.implicitly_wait(30)
genderMale = browser.find_element_by_xpath("//li[@class='srch_input_gender']//label[@class='radio-inline']//input[@value='male']")
genderFemale = browser.find_element_by_xpath("//li[@class='srch_input_gender']//label[@class='radio-inline']//input[@value='female']")
if gender == male:
    genderMale.click()
if gender ==female:
    genderFemale.click()

browser.implicitly_wait(30)
# Passenger Mobile NUmber
mobile = browser.find_element_by_xpath("//div[@class='col-md-5']//input[@id='pmobile']")
mobile.click()
mobileCMD = input("Please Passenger Mobile NUmber")
mobile.send_keys(mobileCMD)

browser.implicitly_wait(30)
# Passenger Email
email = browser.find_element_by_xpath("//div[@class='form-group']//input[@id='pemail']")
email.click()
emailCMD = input("Please Enter Passenger Email Address")
email.send_keys(emailCMD)

browser.implicitly_wait(30)
# Total Amount Payable
payableAmount = browser.find_element_by_xpath("//div[@id='amnt_pay']")
print(payableAmount.text)

browser.implicitly_wait(30)
# bKash
bKash = browser.find_element_by_xpath("//div[@id='bKash']//div[@id='bkash_payment']")
bKash.click()

browser.implicitly_wait(30)
# Confirm Reservation
confirmReservationBtn = browser.find_element_by_xpath("//div[@class='mid_cont_btn']//button[@id='confirm_button']")
confirmReservationBtn.click()
print("Please Pay The Amount Within 30 min")

finalConfirmation = input("Please type Done after Payment")
time.sleep(60)
if finalConfirmation == "Done":
    print("Please Check you Email for Ticket")
    time.sleep(1000)
    browser.quit()


time.sleep(100000)