#from selenium import webdriver
#from selenium.webdriver.chrome.service import Service

#from utils.config_loader import load_config

#def get_driver():
    #config = load_config()
    #browser = config.get("browser", "chrome").lower()
    #service_obj = Service(r'C:\Users\avrah\Documents\chromedriver-win64\chromedriver.exe')

    #if browser == "chrome":
        #return webdriver.Chrome(service=service_obj)
    #elif browser == "firefox":
       # return webdriver.Firefox()
   # else:
        #raise ValueError(f"Unsupported browser: {browser}")
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from utils.config_loader import load_config

def get_driver():
    config = load_config()
    browser = config.get("browser", "chrome").lower()

    is_ci = os.getenv("GITHUB_ACTIONS") == "true"  # Detect GitHub Actions

    if browser == "chrome":
        options = ChromeOptions()
        if is_ci:
            options.add_argument("--headless=new")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
        service = ChromeService(ChromeDriverManager().install())
        return webdriver.Chrome(service=service, options=options)

    elif browser == "firefox":
        options = FirefoxOptions()
        if is_ci:
            options.add_argument("--headless")
        service = FirefoxService(GeckoDriverManager().install())
        return webdriver.Firefox(service=service, options=options)

    elif browser == "edge":
        options = EdgeOptions()
        if is_ci:
            options.add_argument("--headless=new")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
        service = EdgeService(EdgeChromiumDriverManager().install())
        return webdriver.Edge(service=service, options=options)

    else:
        raise ValueError(f"Unsupported browser: {browser}")
