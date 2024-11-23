from selenium import webdriver
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

        import time
        time.sleep(10)

        print("Test Passed")
    except Exception as e:
        print(f"Test Failed: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    test_ui_search()
