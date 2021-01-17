import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager


class getUniversityinfo:
    def __init__(self, url):
        self.url = url
        self.university_list = []

    def start(self):
        print("Don't Touch Chrome When I Search the colleges")
        browser = webdriver.Chrome(ChromeDriverManager().install())
        browser.get(self.url)
        universities = WebDriverWait(browser, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "search-result__title")))
        for university in universities:
            self.university_list.append(university.text)
        browser.quit()
        self.search()

    def search(self):
        opts = ChromeOptions()
        opts.add_experimental_option("detach", True)
        browser = webdriver.Chrome(
            ChromeDriverManager().install(), chrome_options=opts)
        browser.get("https://google.com")
        for index, university_text in enumerate(self.university_list):
            if(index != 0):
                browser.execute_script(
                    "window.open('https://google.com')")
            browser.switch_to.window(browser.window_handles[-1])
            input = browser.find_element_by_class_name("gLFyf")
            input.send_keys(university_text)
            input.send_keys(Keys.ENTER)
        for university_text in self.university_list:
            browser.execute_script(
                "window.open('https://google.com')")
            browser.switch_to.window(browser.window_handles[-1])
            input = browser.find_element_by_class_name("gLFyf")
            input.send_keys(university_text + " min toefl score")
            input.send_keys(Keys.ENTER)
        print("Done! Find Your College")
