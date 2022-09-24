"""DocString"""

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import undetected_chromedriver as uc

William_Hill = 'https://scoreboardslauncher.williamhill.com/scoreboards/events/OB_EV24269726/launch?lang=ru-ru&showSuggestions=true'
Liga_Stavok = 'https://www.ligastavok.ru/'


options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features")
options.add_argument("--disable-blink-features=AutomationControlled")
service = Service('/home/leo/PycharmProjects/chromedriver')
service.start()
#William = webdriver.Remote(service.service_url)



driver = uc.Chrome(executable_path=r'/home/leo/PycharmProjects/chromedriver')
driver.maximize_window()
driver.get(Liga_Stavok)
time.sleep(15)
#William.get(William_Hill)
#William.maximize_window()
player1 = 'ULISES BLANCH'
player2 = 'RINKY HIJIKATA'
'''
def checker():
    animation = William.find_element_by_class_name('animation_label').text
    animation = animation.strip()
    if animation == 'ВЫИГРАННЫЕ ОЧКИ\n%s' % player1:
        print(player1, 'win')
    elif animation == 'ВЫИГРАННЫЕ ОЧКИ\n%s' % player2:
        print(player2, 'win')
'''

def login_to_Liga(login = '9172440681', passwd = 'qazwsx12Q'):
    driver.find_element_by_id('header-sign-in').click()
    time.sleep(1)
    mobile_phone = driver.find_element_by_xpath('/html/body/div[1]/div[5]/div[2]/div[3]/div[1]/div[2]/form/div[1]/input').send_keys(login)
    password = driver.find_element_by_xpath('/html/body/div[1]/div[5]/div[2]/div[3]/div[1]/div[2]/form/div[2]/input').send_keys(passwd)
    signIn = driver.find_element_by_xpath('/html/body/div[1]/div[5]/div[2]/div[3]/div[1]/div[2]/form/button').click()
    time.sleep(100)
    


login_to_Liga()

