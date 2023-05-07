from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import time

driver = webdriver.Chrome()

driver.get("https://arithmetic.zetamac.com/game?key=a7220a92")

try:
    while True:
        question = driver.find_element(By.XPATH, "//*[@id='game']/div/div[1]/span").text
        question = question.replace(" ","")
        result = 0
        if "+" in question:
            operands = question.split("+")
            first = int(operands[0])
            second = int(operands[1])
            result = first+second
        elif "–" in question:
            operands = question.split("–")
            first = int(operands[0])
            second = int(operands[1])
            result = first-second
        elif "×" in question:
            operands = question.split("×")
            first = int(operands[0])
            second = int(operands[1])
            result = first*second
        else:
            operands = question.split("÷")
            first = int(operands[0])
            second = int(operands[1])
            result = int(first/second)
        print("here")
        answer = driver.find_element(By.XPATH, "//*[@id='game']/div/div[1]/input")
        answer.send_keys(str(result))
        time.sleep(100/1000)
except:
    print("something went wrong")

time.sleep(20)
driver.quit()