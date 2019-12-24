from selenium import webdriver
import sys
import os
from time import sleep
import chromedriver_binary
import pickle
from selenium.webdriver.chrome.options import Options
import csv
import unicodedata


def formatName(nameTXT):
    preFormatted = unicodedata.normalize('NFKD', str(nameTXT))
    return u"".join([c for c in preFormatted if not unicodedata.combining(c)])


computerUserName = 'Kroos'
webAppURL = 'https://www.easports.com/fifa/ultimate-team/web-app/'
CookiesDir = "user-data-dir=C:\\Users\\"+computerUserName + \
    "\\AppData\\Local\\Google\\Chrome Beta\\User Data\\Default\\"
ChromeBinaryDir = "C:\\Program Files (x86)\\Google\\Chrome Beta\\Application\\chromedriver.exe"
cwd = os.getcwd()+"\\"
opt = webdriver.ChromeOptions()
opt.add_argument(CookiesDir)
browser = webdriver.Chrome(ChromeBinaryDir, options=opt)

print("Loading The Page")
browser.get(webAppURL)
input("Done loading?")

clubBtn = browser.find_element_by_xpath(
    "/html/body/main/section/nav/button[5]")
clubBtn.click()
print("Moving to Club")
input("Done loading?")

print("Done Moving to Club, Moving To Players")
PlayersBtn = browser.find_element_by_xpath(
    "/html/body/main/section/section/div[2]/div/div/div[1]/div[2]")
PlayersBtn.click()
input("Done loading?")

nextBtn = browser.find_element_by_xpath(
    "/html/body/main/section/section/div[2]/div/div/div/div[2]/div/button[2]")
numOfSkips = int(input('How many pages do you want to skip? '))
for i in range(0, numOfSkips):
    nextBtn.click()
    sleep(0.5)
sleep(0.5)
print("Done Skipping")

with open(cwd+'Players.csv') as f:
    d = dict(filter(None, csv.reader(f)))

print("Done Loading The Database")
sleep(1)
counter = 0

targetPriceChampionLeagueAndGold = int(
    input("what is the minimum price you want for Champion League and Gold? ")) - 1
targetPriceForCommonGold = int(
    input("what is the minimum price you want for Common Gold? ")) - 1
targetPriceForSilverAndBronze = int(
    input("what is the minimum price you want for Silver and Bronze? ")) - 1
currentPage = numOfSkips

while True:
    print("Current Page = " + str(currentPage))
    for i in range(1, 19):
        try:
            name = browser.find_element_by_xpath(
                "/html/body/main/section/section/div[2]/div/div/div/div[2]/ul/li[" + str(i) + "]/div/div[1]/div[2]")
            name.click()
            name = formatName(name.text)
            sleep(0.5)
            bioBtn = browser.find_element_by_xpath(
                "/html/body/main/section/section/div[2]/div/div/section/div/div/div[2]/div[3]/button[1]")
            bioBtn.click()
            rarety = browser.find_element_by_xpath(
                "/html/body/main/section/section/div[2]/div/div/section/div[2]/article/div[2]/div[2]/ul[1]/li[1]/h2").text
            flag = False
            if name not in d:
                flag = True
                sleep(1.5)
                name = browser.find_element_by_xpath(
                    "/html/body/main/section/section/div[2]/div/div/section/div[2]/article/div[2]/div[2]/ul[1]/li[2]/h2")
                name = formatName(name.text)
            # get value from csv and then ask to sell or skip\
            price = ""
            para = ""
            if name in d:
                sleep(2)
                if flag:
                    backBtn = browser.find_element_by_xpath(
                        "/html/body/main/section/section/div[2]/div/div/section/div[1]/button")
                    backBtn.click()
                price = d[name].split(";")
                price = price[0]
                link = d[name].split(";")
                link = link[1]
                print(i, "Found " + name + " Price = " +
                      price + " link: " + link)
                if len(price) > 1:
                    para = price[len(price)-1]
                    if "K" in para or "M" in para:
                        price = float(price[0:len(price)-1])
                        if para == "K":
                            price = float(price * 1000)
                        elif para == "M":
                            price = float(price * 1000000)
                    price = float(price)

                    isCommonGoldAndHigh = rarety == "Common Gold" and price > targetPriceForCommonGold
                    isSilverOrBronzeAndHigh = (
                        "Silver" in rarety or "Bronze" in rarety) and price > targetPriceForSilverAndBronze
                    isChampionLeagueOrGoldAndHigh = price > targetPriceForSilverAndBronze
                    if(isCommonGoldAndHigh or isSilverOrBronzeAndHigh or isChampionLeagueOrGoldAndHigh):
                        sleep(3)
                        listBtn = browser.find_element_by_xpath(
                            "/html/body/main/section/section/div[2]/div/div/section/div[2]/div/div[2]/div[2]/div[1]/button")
                        listBtn.click()
                        sleep(1)
                        priceInput = browser.find_element_by_xpath(
                            "/html/body/main/section/section/div[2]/div/div/section/div[2]/div/div[2]/div[2]/div[2]/div[3]/div[2]/input")
                        priceInput.click()
                        sleep(2)
                        priceInput.send_keys(str(price))
                        inp = input("1 to sell or any key to skip: ")
                        if inp == "1":
                            listItemBtn = browser.find_element_by_xpath(
                                "/html/body/main/section/section/div[2]/div/div/section/div[2]/div/div[2]/div[2]/div[2]/button")
                            listItemBtn.click()
                            counter += 1
                            print(str(counter) +
                                  "/100 Listed in The Current Session")
                            sleep(3)
            else:
                print(i, "Not Found", name)
        except Exception as e:
            print(e)
            print("Error Occured, skipping")
            pass
    print("Moving To The Next Page")
    try:
        nextBtn = browser.find_element_by_xpath(
            "/html/body/main/section/section/div[2]/div/div/div/div[2]/div/button[2]")
        nextBtn.click()
    except:
        pass
    currentPage = currentPage + 1
    sleep(3)
