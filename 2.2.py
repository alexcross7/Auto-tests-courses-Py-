from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time
import math
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"


def calc(x):
    return str(int(x) + int(y))


def print_answer(remote: webdriver.Remote):
    alert = remote.switch_to.alert
    print(alert.text.split()[0], alert.text.split()[-1])
    alert.accept()


options = Options()
options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
browser = webdriver.Firefox(options=options,
                            executable_path=r"C:\Users\User\Desktop\geckodriver-v0.31.0-win32\geckodriver.exe")

browser.get(link)
x_element = browser.find_element(By.ID, "num1")
x_element2 = browser.find_element(By.ID, "num2")
x = x_element.text
y = x_element2.text
z = calc(x)

select = Select(browser.find_element(By.ID, "dropdown"))
select.select_by_value(str(z))
#option1 = browser.find_element(By.CSS_SELECTOR, f"[value='{z}']")
#option1.click()
option3 = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-default")
option3.click()
time.sleep(3)
print_answer(browser)
browser.quit()
