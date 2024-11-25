from selenium import webdriver
from base.functions import SearchFunctions

# Initialize WebDriver
driver = webdriver.Chrome()  

try:
    # Initialize functions
    brit = SearchFunctions(driver)

    # Run the search test
    brit.open_brit_insurance()
    brit.search_for_term("IFRS 17")
    brit.validate_number_of_results(expected_count=8)
    brit.validate_specific_title(expected_title="Financials")
    print("Test passed: Correct number of results and expected title found.")

finally:
    # Close the browser
    driver.quit()