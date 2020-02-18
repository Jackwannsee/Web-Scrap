from selenium import webdriver
import time
import threading

b = webdriver.Chrome()
b.get("https://www.worldometers.info/world-population/")

def Wait():
    b.implicitly_wait(2)
    time.sleep(2)

def WorldPopulation():
    Wait()
    Count = b.find_element_by_class_name("maincounter-number")
    print('World Population: ' + Count.text)

    threading.Timer(5.0, WorldPopulation()).start()

WorldPopulation()
