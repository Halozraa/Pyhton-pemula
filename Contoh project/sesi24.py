import random
<<<<<<< HEAD
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
import cv2
import time

massage = "Mau mencari apa di youtube?"
title = "Auto Search YT"
display = pyautogui.prompt(massage,title)
driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.get("https://www.youtube.com/")
driver.find_element(By.ID,'search').click()
driver.find_element(By.ID,'search').send_keys(display)
pyautogui.press('enter')
driver.find_element(By.ID,'thumbnail-container').click()
print("Saya memberikan waktu 30 detik untuk menonton")
time.sleep(30)
=======
import pandas as pd
import numpy as np

datas = "data_pengangguran.csv"
datas. pd
>>>>>>> 10b3beee9370fb304659551f671f3199e665ebf8
