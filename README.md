# Brit QA Tech Test - Automated Tests

## Overview
This repository contains automated tests for the Brit Insurance website. The tests are written in Python using Selenium and include UI automation for the search functionality.

## Prerequisites
- Python 3.10+
- Google Chrome browser
- ChromeDriver (or another WebDriver based on your browser)

## Setup Instructions
1. Clone the repository:
    git clone https://github.com/alintimpu/brit-qa-tech-test


## Create and activate a virtual environment:
python3 -m venv venv
source venv/bin/activate

## Install dependencies:
pip install -r requirements.txt

##  Run the test:
Ensure that the virtual environment is active.
python test_ui.py


## What the Test Does
The script automates the following steps:

1. Opens the Brit Insurance website.
2. Searches for the term "IFRS 17" in the search bar.
3. Asserts that 5 search results are displayed.
4. Verifies that one of the titles is "Interim results for the six months ended 30 June 2022".

## Notes
Ensure Google Chrome is installed on your system.
WebDriver Manager is used to handle the ChromeDriver version automatically.
If the test fails, check the CSS selectors or ensure that the website layout has not changed.

