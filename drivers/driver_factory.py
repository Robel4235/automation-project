from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from utils.config_loader import load_config

def get_driver():
    config = load_config()
    browser = config.get("browser", "chrome").lower()
    service_obj = Service(r'C:\Users\avrah\Documents\chromedriver-win64\chromedriver.exe')

    if browser == "chrome":
        return webdriver.Chrome(service=service_obj)
    elif browser == "firefox":
        return webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {browser}")
