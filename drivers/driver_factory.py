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
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from utils.config_loader import load_config

def get_driver():
    config = load_config()
    browser = config.get("browser", "chrome").lower()

    if browser == "chrome":
        chrome_options = Options()
        chrome_options.add_argument("--headless=new")  # important for GitHub : Runs Chrome without opening a visible browser (needed in CI)
        chrome_options.add_argument("--no-sandbox") #Prevents permission errors in GitHub’s environment
        chrome_options.add_argument("--disable-dev-shm-usage")#Avoids memory issues
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--remote-debugging-port=9222")

        return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    elif browser == "firefox":
        # You can also configure headless Firefox here if needed
        return webdriver.Firefox()

    else:
        raise ValueError(f"Unsupported browser: {browser}")
