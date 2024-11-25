# Brit QA Tech Test - Automated Tests

## Overview
This repository contains the solutions for the Brit QA Tech Test, which includes:
1. A UI Automation Task to verify search functionality on the Brit Insurance website.
2. An API Automation Task to test the PATCH endpoint of a RESTful API.
Both solutions are implemented in Python using Selenium for UI testing and the requests library for API testing. 

Detailed instructions and dependencies are provided below.

## Prerequisites
- Python 3.10 or later
- Google Chrome browser
- ChromeDriver (compatible with your installed Chrome version)
- Internet access for Selenium to load the website and for the API calls

## Setup Instructions
1. Clone the repository:
    git clone https://github.com/alintimpu/brit-qa-tech-test
    cd brit-qa-tech-test

## Create and activate a virtual environment:
python3 -m venv venv
source venv/bin/activate

## Install dependencies:
pip install -r requirements.txt

The dependencies include:
- selenium
- requests

## Ensure chromedriver is installed and added to your PATH. To verify, run:
chromedriver --version


##  Running the UI tests:
1. Ensure that the virtual environment is active.
2. Navigate to the ui_test directory:
    cd ui_tests
3. Run the UI test:
    python test_ui.py

## What the Test Does
The script automates the following steps:

1. Opens the Brit Insurance website.
2. Searches for the term "IFRS 17" in the search bar.
3. Asserts that 8 search results are displayed.
4. Verifies that one of the titles is "Financials".

## Notes
Ensure Google Chrome is installed on your system.
WebDriver Manager is used to handle the ChromeDriver version automatically.
If the test fails, check the CSS selectors or ensure that the website layout has not changed.


## Running the API tests:
1. Navigate to the api_test directory:
    cd api_test
2. Run the API test:
    python test_api.py

## What the Test Does
The API test validates the PATCH endpoint of the RESTful API by updating an object's attributes and verifying the response.


## Known Issues
UI test relies on dynamic elements; any changes to the website structure may require script updates.