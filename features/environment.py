from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def before_all(context):
    chrome_options = Options()

    if 'headless' in context.config.userdata:
        if context.config.userdata['headless'].lower() == 'true':
            chrome_options.add_argument("--headless")

    context.browser = webdriver.Chrome(options=chrome_options)
    context.browser.maximize_window()
    context.browser.implicitly_wait(10)


def after_all(context):
    context.browser.quit()
