from selenium import webdriver
import time
import json
import smtplib

#password and username
with open ("/Users/jackthekewlkid/Desktop/All/Coding/WebScrap/credentials/credentials.json","r+") as jf:
    creds = json.load(jf)

options = webdriver.ChromeOptions()
options.add_argument("headless")
b = webdriver.Chrome(options=options)

#b = webdriver.Chrome()        #This is to run it with a browser
b.get("https://accounts.veracross.eu/asb/portals/login")

Username = b.find_element_by_id("username")
Username.send_keys(creds["username"])
Password = b.find_element_by_id("password")
Password.send_keys(creds["password"])
Login = b.find_element_by_id("recaptcha")
Login.click()
b.implicitly_wait(2)
Directory = b.find_element_by_xpath("/html/body/nav/ul/li[6]/a")
Directory.click()
b.implicitly_wait(1)
Grades = b.find_element_by_xpath("/html/body/div[2]/div[2]/div[3]/div[2]/div/div/a")
Grades.click()
b.implicitly_wait(2)
Grade = b.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[2]/a[14]")
Grade.click()
b.implicitly_wait(1)
Next = b.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/a")
Next.click()
b.implicitly_wait(1)

def getInfo():
    Name = b.find_elements_by_class_name("directory-Entry_Title")
    
    with open('TestDataBase.txt', 'w') as f:
        for item in Name:
            f.write("%s\n" % item.text)

getInfo()
