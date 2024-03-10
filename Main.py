#Windows automation
#by Eric Lee

#base setup
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time 
import string
import random


def main():   
    global driver
    global options
    options = Options()
    options.add_experimental_option("detach" , True)
    driver = webdriver.Edge()
    for i in range(0, 10):    
        randomizer()
        driver.get("https://www.bing.com")
        time.sleep(1)
        search()
        time.sleep(1)
    driver.quit()    
    

def search(): 
    global bigbar 
    bigbar= driver.find_element(by=By.ID , value="sb_form_q")
    bigbar.send_keys(str(random_ID))
    bigbar.send_keys(Keys.ENTER)

def randomizer(): 
    global random_ID
    random_ID = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k=35))
    
main()
