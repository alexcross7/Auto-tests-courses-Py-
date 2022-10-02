from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
import unittest
from faker import Faker
#Я работаю с  Firefox, нужно скачать 'geckodriver'

f = Faker()

link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"


class TestsWelcome(unittest.TestCase):

    def test_welcome_text1(self):
        options = Options()
        options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
        browser = webdriver.Firefox(options=options,
                                    executable_path=r"C:\Users\User\Desktop\geckodriver-v0.31.0-win32\geckodriver.exe")

        browser.get(link1)
        name = browser.find_elements_by_css_selector('.first_block .first')
        for element in name:
            element.send_keys(f.unique.first_name())
        last_name = browser.find_elements_by_css_selector('.first_block .second')
        for element in last_name:
            element.send_keys(f.unique.last_name())
        email1 = browser.find_elements_by_css_selector('.first_block .third')
        for element in email1:
            element.send_keys(f.unique.email())
        time.sleep(3)

        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text

        assert "Congratulations! You have successfully registered!" == welcome_text
        browser.close()

    def test_welcome_text2(self):   #без try, т.к тест по заданию и должен падать
        options = Options()
        options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
        browser = webdriver.Firefox(options=options,
                                    executable_path=r"C:\Users\User\Desktop\geckodriver-v0.31.0-win32\geckodriver.exe")
        browser.get(link2)
        name = browser.find_element_by_css_selector('.first_block .first')
        name.send_keys("Имя")
        last_name = browser.find_element_by_css_selector('.first_block .second')
        last_name.send_keys("Фамилия")
        email = browser.find_element_by_css_selector('.first_block .third')
        email.send_keys("Почта")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text

        assert "Congratulations! You have successfully registered!" == welcome_text


if __name__ == "__main__":
    unittest.main()
