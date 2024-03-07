from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class habiHomePage:
    url = 'https://llavero.co'
    timeout = 10

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, self.timeout)

