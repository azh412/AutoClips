from selenium import webdriver
from time import sleep
driver = webdriver.Chrome("driver/chromedriver")
driver.get("https://www.decisionproblem.com/paperclips/index2.html")
unlockedClippers = False
unlockedProjects = False
while True:
    availablefunds = float(driver.find_element_by_id("funds").text.replace(',', ''))
    paperclips = int(driver.find_element_by_id("clips").text)
    makepaperclips = driver.find_element_by_id("btnMakePaperclip")
    buywire = driver.find_element_by_id("btnBuyWire")
    wire = driver.find_element_by_id("wire")
    makeclipper = driver.find_element_by_id("btnMakeClipper")
    if unlockedProjects:
        projects = driver.find_element_by_class_name("projectButton")
    else:
        if paperclips >= 2000:
            unlockedProjects = True
    if unlockedClippers == False:
        if availablefunds > 5.00:
            unlockedClippers = True
            print("Unlocked AutoClippers!")
            clippercost = float(driver.find_element_by_id("clipperCost").text)
    else:
        clippercost = float(driver.find_element_by_id("clipperCost").text)
    expandmarketing = driver.find_element_by_id("btnExpandMarketing")
    availablewire = int(wire.text.replace(',', ''))
    increasedemand = driver.find_element_by_id("btnLowerPrice")
    decreasedemand = driver.find_element_by_id("btnRaisePrice")
    demand = int(driver.find_element_by_id("demand").text)
    if demand < 160:
        increasedemand.click()
    if expandmarketing.is_enabled:
        expandmarketing.click()
    if availablewire < 400:
        buywire.click()
    if unlockedClippers:
        if availablefunds > clippercost:
            if availablewire >= 450:
                makeclipper.click()
    makepaperclips.click()