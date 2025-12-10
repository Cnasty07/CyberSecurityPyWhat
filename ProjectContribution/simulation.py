# simulation.py
# INFO: Example of pipeline usage with the pyWhat API Wrapper
#       We simulate scraping an html page to find valuable information

import os
from src.wrapper_interface import pyWhatInterface

# Step 1: Finding a suitable input
def scan():
    pass

# use pywhat to scan file or text input for important information
def find_valuable_info(input_data: str):
    what = pyWhatInterface(match_level=2)
    what.get_tags()
    results = what.identify(input_data)
    return results


def main():
    sample_input = "<html><body>Contact us at email@example.com or call 123-456-7890.</body></html>"
    valuable_info = find_valuable_info(sample_input)
    print("Valuable Information Found:", valuable_info)

if __name__ == "__main__":
    main()
