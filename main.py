import pyautogui as pyA
import time
import re
import cv2
from twilio.rest import Client

# Make sure all programs are minimized and that Valorant is in a small window, not full screen on every single account
# Use GUI automation to take 3 screenshots of skins on rotation

def logIn(username, password):
    print("Starting in 5 seconds")
    time.sleep(5)
    pic3 = pyA.locateOnScreen('Images/valicon.PNG', confidence=0.85)
    if pic3 is not None:
        pic3 = pyA.center(pic3)
        pic3X, pic3Y = pic3
        pyA.moveTo(pic3X, pic3Y)
        pyA.click(pic3X, pic3Y)
        pyA.click(pic3X, pic3Y)
    else:
        print("Send text: valicon not found, exiting program.")
        return
    
    time.sleep(10)
    pic3 = pyA.locateOnScreen('Images/confirmedOpen.PNG', confidence=0.95)
    if pic3 is None:
        print("Send text: VAL did not open up after icon clicked")
        return
    
    pyA.typewrite(username)
    time.sleep(3)
    pyA.hotkey("tab")
    pyA.typewrite(password)
    pyA.hotkey("enter")

    time.sleep(3)
    pic3 = pyA.locateOnScreen('Images/bigPlay.PNG', confidence=0.95)
    if pic3 is not None:
        pic3 = pyA.center(pic3)
        pic3X, pic3Y = pic3
        pyA.moveTo(pic3X, pic3Y)
        pyA.click(pic3X, pic3Y)

def checkSkins():
    time.sleep(30)
    time.sleep(5)
    pic3 = pyA.locateOnScreen('Images/iUnderstand.PNG', confidence=0.55)
    if pic3 is not None:
        pic3 = pyA.center(pic3)
        pic3X, pic3Y = pic3
        pyA.moveTo(pic3X, pic3Y)
        pyA.click(pic3X, pic3Y)
        print("i understand found and clicked")
        pyA.moveTo(0, 0)
        pyA.moveTo(pic3X, pic3Y)
        pyA.click(pic3X, pic3Y)

    time.sleep(2)
    pic3 = pyA.locateOnScreen('Images/store.PNG', confidence=0.95)
    if pic3 is not None:
        pic3 = pyA.center(pic3)
        pic3X, pic3Y = pic3
        pyA.moveTo(pic3X, pic3Y)
        pyA.click(pic3X, pic3Y)

    time.sleep(2)
    pyA.hotkey("win", "prtsc")
    time.sleep(2)
    pyA.hotkey("alt", "f4")


# Increase the speed of execution
pyA.PAUSE = 0.5

# Login and check skins for multiple accounts
accounts = [
    {"username": "EddieTGH12", "password": "sexyboi123321123"},
    {"username": "flawlessduettt", "password": "edgoo1212"},
    {"username": "cypherismydaddy", "password": "edgoo1212"}
]

for account in accounts:
    logIn(account["username"], account["password"])
    checkSkins()
    time.sleep(5)
