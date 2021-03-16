from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

options = Options()
options.add_argument("--disable-infobars")
options.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 1
})
""""
To Use:
1. Type 'Pip install Selenium' in your terminal
2.1 Download the corresponding chromedriver version: https://chromedriver.chromium.org/downloads
2.2 To find which version your chrome run on; use this website: chrome://settings/help
2.3 Set up the path for your chromedriver; in this case, the path is located in the local disk
"""
path = 'C:\chromedriver.exe'
driver = webdriver.Chrome(path)


def waiting(element):
    try:
        WebDriverWait(driver, 90).until(
            EC.presence_of_all_elements_located((By.XPATH, element))
        )

    except TimeoutError:
        print('Unable to locate the element \n'
              'Do not worry, this is not your fault')
        quit()
    finally:
        pass


def Purse(username, profile, browser):
    browser.get('https://sky.shiiyu.moe/' + username + '/' + profile)
    purse_location = '/html/body/main/div[2]/div[3]/div[3]/span[2]'
    waiting(purse_location)
    purse = driver.find_elements_by_xpath(purse_location)
    print(f'{username}, has {purse[0].text} in their purse.')
    '# return purse'


def Bank(username, profile, browser):
    browser.get('https://sky.shiiyu.moe/' + username + '/' + profile)
    bank_location = '/html/body/main/div[2]/div[3]/div[5]/span[2]'
    waiting(bank_location)
    bank = driver.find_elements_by_xpath(bank_location)
    print(f'{username} has {bank[0].text} in their bank.')
    '# return bank'


"""
Example of how to use:
Bank(Thatbananaking, cucumber, driver)
Purse(Thatbananaking, cucumber, driver)
"""
