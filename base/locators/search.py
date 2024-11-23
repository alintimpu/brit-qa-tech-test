from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SearchLocators:
    # Locators for the search bar
    SEARCH_BAR = (By.CSS_SELECTOR, '[type="button"]')
    SEARCH_INPUT = (By.CSS_SELECTOR, '[type="search"]')
    
    # Locator for the search result titles
    SEARCH_RESULTS = (By.CSS_SELECTOR, "a.s-results__tag")



class SearchFunctions:
    def __init__(self, driver):
        self.driver = driver

    def open_brit_insurance(self):
        # Navigate to the Brit Insurance homepage
        self.driver.get("https://www.britinsurance.com/")
        self.driver.maximize_window()

    def search_for_term(self, term):
        # Search for a specific term in the search bar
        search_bar = self.driver.find_element(*SearchLocators.SEARCH_BAR)
        search_bar.click()
        search_bar.send_keys(term)
        search_bar.send_keys(Keys.RETURN)

    def get_search_results(self):
        # Retrieve all search result titles
        WebDriverWait(self.driver, 2).until(
            EC.presence_of_all_elements_located(SearchLocators.SEARCH_RESULTS)
        )
        return self.driver.find_elements(*SearchLocators.SEARCH_RESULTS)

    def validate_number_of_results(self, expected_count):
        # Validate the number of search results returned
        results = self.get_search_results()
        actual_count = len(results)
        assert actual_count == expected_count, (
            f"Expected {expected_count} results, but found {actual_count}."
        )
        return results

    def validate_specific_title(self, expected_title):
        # Validate a specific title exists in the search results
        results = self.get_search_results()
        titles = [result.text for result in results]
        assert expected_title in titles, (
            f"Expected title '{expected_title}' not found in search results."
        )