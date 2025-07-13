from drivers.driver_factory import get_driver
from pages.ynet_home_page import YnetHomePage
from utils.logger import create_logger
import requests

logger = create_logger(__name__)

def test_images_are_valid():
    driver = get_driver()
    broken_images = []

    try:
        driver.get("https://www.ynet.co.il")
        ynet_page = YnetHomePage(driver)
        image_urls = ynet_page.get_all_image_sources()

        for url in image_urls:
            try:
                response = requests.get(url, timeout=5)
                if response.status_code != 200:
                    logger.warning(f"Broken image: {url} | Status: {response.status_code}")
                    broken_images.append((url, response.status_code))
            except Exception as e:
                logger.error(f"Error checking image: {url} | {e}")
                broken_images.append((url, str(e)))

    except Exception as e:
        logger.exception("Test failed while loading or interacting with Ynet homepage")
        raise AssertionError("Ynet UI test failed due to a critical error.")

    finally:
        driver.quit()

    for url, status in broken_images:
        logger.warning(f"BROKEN IMAGE: {url} | STATUS: {status}")

    assert len(broken_images) == 0, f"Found broken images: {broken_images}"
