import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from random import randint, choice
import pyautogui
from pywinauto.application import Application
import vpn
from vpn import vpn_list

URL = 'https://getgeek.ro/category/periferice/'
# disconnect_url = 'child_window(title="Disconnect", auto_id="connect_button", control_type="Button")'
# connect_url = 'child_window(title="Connect", auto_id="connect_button", control_type="Button")'

chrome_options = webdriver.ChromeOptions()
chrome_options.page_load_strategy = 'eager'
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                            'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3')
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(5)

app = Application(backend='uia').connect(best_match="Surfshark")
# disconnect = app.Surfshark.disconnect_url
# connect = app.Surfshark.connect_url

tabs_index = 0
tabs_back = 29
count = 0
vpn_list_edit = vpn_list
# countries = len(vpn_list_edit) - 1
print(f"{len(vpn_list_edit)} locations available for vpn routing.")

while vpn_list_edit != []:
    for x in range(1, 12):
        if count % 11 == 0 and count > 1:
            try:
                country = random.choice(vpn_list_edit)
                vpn_list_edit.remove(country)
                country()
            except IndexError:
                break
        else:
            pass
        if x == 1:
            driver.get(URL)
            articles = driver.find_elements(By.CLASS_NAME, 'post-gallery')
            sleep(randint(1, 3))
            for y in range(0, 11):
                try:
                    articles = driver.find_elements(By.CLASS_NAME, 'post-gallery')
                    try:
                        articles[y].click()
                    except:
                        app.Surfshark.child_window(title="Disconnect", auto_id="connect_button",
                                                   control_type="Button").click()
                        sleep(0.5)
                        app.Surfshark.child_window(title="Connect", auto_id="connect_button",
                                                   control_type="Button").click()
                        sleep(3)
                        refresh = driver.current_url
                        driver.get(refresh)
                    app.Surfshark.child_window(title="Disconnect", auto_id="connect_button",
                                               control_type="Button").click()
                    sleep(1)
                    app.Surfshark.child_window(title="Connect", auto_id="connect_button", control_type="Button").click()
                    sleep(3)
                    count += 1
                    print(f"Current count: {count}")
                    if tabs_index == 29:
                        driver.switch_to.window(driver.window_handles[tabs_index - tabs_back])
                        if tabs_back == 0:
                            tabs_back += 29
                        else:
                            tabs_back -= 1
                    else:
                        driver.execute_script("window.open('');")
                        tabs_index += 1
                        driver.switch_to.window(driver.window_handles[tabs_index])
                    driver.get(URL + 'page/' + str(x))
                    sleep(0.5)
                    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                except IndexError:
                    pass
        else:
            driver.get(URL + 'page/' + str(x))
            articles = driver.find_elements(By.CLASS_NAME, 'post-gallery')
            sleep(randint(1, 3))
            for y in range(0, 11):
                try:
                    articles = driver.find_elements(By.CLASS_NAME, 'post-gallery')
                    try:
                        articles[y].click()
                    except:
                        app.Surfshark.child_window(title="Disconnect", auto_id="connect_button",
                                                   control_type="Button").click()
                        sleep(1)
                        app.Surfshark.child_window(title="Connect", auto_id="connect_button",
                                                   control_type="Button").click()
                        sleep(3)
                        refresh = driver.current_url
                        driver.get(refresh)
                    app.Surfshark.child_window(title="Disconnect", auto_id="connect_button",
                                               control_type="Button").click()
                    sleep(0.5)
                    app.Surfshark.child_window(title="Connect", auto_id="connect_button", control_type="Button").click()
                    sleep(3)
                    count += 1
                    print(f"Current count: {count}")
                    if tabs_index == 29:
                        driver.switch_to.window(driver.window_handles[tabs_index - tabs_back])
                        if tabs_back == 0:
                            tabs_back += 29
                        else:
                            tabs_back -= 1
                    else:
                        driver.execute_script("window.open('');")
                        tabs_index += 1
                        driver.switch_to.window(driver.window_handles[tabs_index])
                    driver.get(URL + 'page/' + str(x))
                    sleep(0.5)
                    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                except IndexError:
                    pass
