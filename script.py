from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

firefox= webdriver.Firefox()
firefox.get("https://orteil.dashnet.org/cookieclicker/")

firefox.implicitly_wait(30)

#choose language
lang= firefox.find_element(By.ID, "langSelect-EN")
lang.click()
firefox.implicitly_wait(30)

cookie= firefox.find_element(By.ID, "bigCookie")
cookie_count= firefox.find_element(By.ID, "cookies")
click_upgrade= firefox.find_element(By.ID, "productPrice0")
grandma_upgrade= firefox.find_element(By.ID, "productPrice1")

actions= ActionChains(firefox)

upgrade_counter= 0
def buyUpgrade(count, upgrade_counter):
    if count >= int(click_upgrade.text) and upgrade_counter < 2:
        actions.click(click_upgrade)
        actions.perform()
        upgrade_counter+= 1
    elif count >= int(grandma_upgrade.text) and upgrade_counter == 2:
        actions.click(grandma_upgrade)
        actions.perform()
        upgrade_counter= 0
    
    return upgrade_counter

while(True):
    actions.click(cookie)
    actions.perform()
    count= int(cookie_count.text.split(" ")[0].replace(",", ""))
    upgrade_counter= buyUpgrade(count, upgrade_counter)

    print(count, upgrade_counter)
