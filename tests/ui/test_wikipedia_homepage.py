from drivers.driver_factory import get_driver
from selenium.webdriver.common.by import By

def test_wikipedia_homepage_ui():
    driver = get_driver()
    driver.get("https://www.wikipedia.org/")

    # Check heading
    heading = driver.find_element(By.XPATH, "/html/body/main/div[1]/h1/span").text
    print(heading)
    assert "Wikipedia" in heading, "Main heading not found"

    # Check search input
    search_input = driver.find_element(By.ID, "searchInput")
    assert search_input.is_displayed(), "Search input not visible"
    assert search_input.is_enabled(), "Search input not enabled"

    # Check language links
    language_elements = driver.find_elements(By.CLASS_NAME, "central-featured-lang")
    assert len(language_elements) >= 5, f"Expected >= 5 languages, found {len(language_elements)}"

    driver.quit()
