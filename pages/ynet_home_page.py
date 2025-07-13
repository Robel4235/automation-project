from selenium.webdriver.common.by import By
from utils.logger import create_logger
logger = create_logger(__name__)

class YnetHomePage:
    def __init__(self, driver):
        self.driver = driver

    def get_all_image_sources(self):
        try:
            logger.info("Locating all image elements on Ynet homepage")
            images = self.driver.find_elements(By.TAG_NAME, "img")
            srcs= [img.get_attribute("src") for img in images if img.get_attribute("src")]
            logger.info(f"Found {len(srcs)} images")
            return srcs
        except Exception as e:
            logger.exception("Failed to extract image sources")
            raise Exception(f"Could not get image sources from the homepage: {e}")


