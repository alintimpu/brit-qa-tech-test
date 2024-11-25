from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_ui_search():
    # Set up the Chrome driver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        # Open the Brit Insurance website
        driver.get("https://www.britinsurance.com/")
        driver.maximize_window()
        time.sleep(2)

        # Allow all cookies
        accept_cookies = driver.find_element(By.CSS_SELECTOR, '[id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"]')
        accept_cookies.click()

        # Perform the search
        search_bar = driver.find_element(By.CSS_SELECTOR, '[type="button"]')
        search_bar.click()

        search_input = driver.find_element(By.CSS_SELECTOR, '[type="search"]')
        search_input.send_keys("IFRS 17")
        search_bar.send_keys(Keys.ENTER)


        # Validate the correct number of search results are returned
        results = driver.find_elements(By.CSS_SELECTOR, 'a.s-results__tag')  
        assert len(results) == 8, f"Expected 5 results, but found {len(results)}"

        # Check for specific title
        titles = [result.text for result in results]
        assert "Financials" in titles, "Expected title not found in search results"

        print("Test Passed")
    except Exception as e:
        print(f"Test Failed: {e}")
    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    test_ui_search()
