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
from selenium import webdriver
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

    if browser == "chrome":
        service = ChromeService(ChromeDriverManager().install())
        return webdriver.Chrome(service=service)

    elif browser == "firefox":
        service = FirefoxService(GeckoDriverManager().install())
        return webdriver.Firefox(service=service)

    elif browser == "edge":
        service = EdgeService(EdgeChromiumDriverManager().install())
        return webdriver.Edge(service=service)

    else:
        raise ValueError(f"Unsupported browser: {browser}")
