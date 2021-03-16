from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import selenium.webdriver.support.ui as ui
import selenium.webdriver.support.expected_conditions as EC
import os
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
options = Options()
options.add_argument("--disable-infobars")
options.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 1
})
PATH = 'C:\chromedriver.exe'
browser = webdriver.Chrome(PATH)
username = input('username?: ')
profile = input('profile?: ')


def waiting():

    try:
        WebDriverWait(browser, 90).until(
            EC.presence_of_all_elements_located((By.XPATH, element))
            )
    finally:
        pass


class Bot:
    def __init__(self, username, profile, browser):

        self.driver = browser
        self.username = username
        self. profile = profile

    def website(self):
        self.driver.get('https://sky.lea.moe/' + username + '/' + profile)

    def coins(self):
        bank = self.driver.find_elements_by_xpath('/html/body/div[7]/div[2]/div[1]/div[13]/div[5]/span[2]')
        purse = self.driver.find_elements_by_xpath('/html/body/div[7]/div[2]/div[1]/div[13]/div[4]/span[2]')
        money = [bank, purse]
        for i in range(2):
            print('')
        print('Money:')
        print('')
        print('Bank:', bank[0].text)
        print('Purse:', purse[0].text)
        print('')
    
    def stat(self):
        heath = self.driver.find_elements_by_xpath('/html/body/div[7]/div[2]/div[1]/div[1]/span/span[2]')
        defense = self.driver.find_elements_by_xpath('/html/body/div[7]/div[2]/div[1]/div[2]/span/span[2]')
        strength = self.driver.find_elements_by_xpath('//*[@id="base_stats_container"]/div[3]/span/span[2]')
        speed = self.driver.find_elements_by_xpath('//*[@id="base_stats_container"]/div[4]/span/span[2]')
        crit_chance = self.driver.find_elements_by_xpath('/html/body/div[7]/div[2]/div[1]/div[5]/span/span[2]')
        crit_damage = self.driver.find_elements_by_xpath('//*[@id="base_stats_container"]/div[6]/span/span[2]')
        attack_speed = self.driver.find_elements_by_xpath('//*[@id="base_stats_container"]/div[7]/span/span[2]')
        intelligence = self.driver.find_elements_by_xpath('//*[@id="base_stats_container"]/div[7]/span/span[2]')
        SC_chance = self.driver.find_elements_by_xpath('//*[@id="base_stats_container"]/div[9]/span/span[2]')
        MF = self.driver.find_elements_by_xpath('//*[@id="base_stats_container"]/div[10]/span/span[2]')
        PL = self.driver.find_elements_by_xpath('/html/body/div[7]/div[2]/div[1]/div[11]/span/span[2]')
        stats = [heath, defense, strength, speed, crit_chance, crit_damage,
                 attack_speed, intelligence, SC_chance, MF, PL]
        print('Stats:')
        print('')
        print('Health:', heath[0].text)
        print('Defense:', defense[0].text)
        print('Strength:', strength[0].text)
        print('Speed:', speed[0].text)
        print('Crit chance:', crit_chance[0].text)
        print('Crit Damage:', crit_damage[0].text)
        print('Attack Speed:', attack_speed[0].text)
        print('Intelligence', intelligence[0].text)
        print('Sea Creature Chance:', SC_chance[0].text)
        print('Magic Find:', MF[0].text)
        print('Pet Luck:', PL[0].text)
        print('')
    
    def skill(self):

        combat = self.driver.find_elements_by_xpath('/html/body/div[7]/div[2]/div[2]/div[1]/div[4]/div[2]/span')
        foraging = self.driver.find_elements_by_xpath('//*[@id="other_skills"]/div[5]/div[2]/span')
        alchemy = self.driver.find_elements_by_xpath('/html/body/div[7]/div[2]/div[2]/div[1]/div[8]/div[2]/span')
        mining = self.driver.find_elements_by_xpath('/html/body/div[7]/div[2]/div[2]/div[1]/div[3]/div[2]/span')
        fishing = self.driver.find_elements_by_xpath('/html/body/div[7]/div[2]/div[2]/div[1]/div[6]/div[2]/span')
        farming = self.driver.find_elements_by_xpath('/html/body/div[7]/div[2]/div[2]/div[1]/div[2]/div[2]/span')
        taming = self.driver.find_elements_by_xpath('//*[@id="other_skills"]/div[1]/div[2]/span')
        enchanting = self.driver.find_elements_by_xpath('/html/body/div[7]/div[2]/div[2]/div[1]/div[7]/div[2]/span')
        rune = self.driver.find_elements_by_xpath('/html/body/div[7]/div[2]/div[2]/div[1]/div[10]/div[2]/span')
        carpentry = self.driver.find_elements_by_xpath('//*[@id="other_skills"]/div[9]/div[2]/span')
        skill_lvl = [combat, foraging, alchemy, mining, fishing,
                     farming, taming, enchanting, rune, carpentry]
        print('Skills:')
        print('')
        print('Combat:', combat[0].text)
        print('Foraging:', foraging[0].text)
        print('Alchemy:', alchemy[0].text)
        print('Mining:', mining[0].text)
        print('Fishing:', fishing[0].text)
        print('Farming:', farming[0].text)
        print('Taming:', taming[0].text)
        print('Enchanting:', enchanting[0].text)
        print('Rune Crafting:', rune[0].text)
        print('Carpentry:', carpentry[0].text)


element = '//*[@id="additional_stats_container"]/div[4]/span[2]'


bot = Bot(username, profile, browser)
bot.website()
bot.coins()
bot.stat()
bot.skill()
browser.quit()
