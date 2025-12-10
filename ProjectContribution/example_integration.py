# simulation.py
# INFO: Example of pipeline usage with the pyWhat API Wrapper
#       We simulate scraping an html page to find valuable information

# TODO: Finish Simulation of pipeline using pyWhatInterface

import os
import requests

from pywhat.printer import Printing
from pywhat import Keys

from src.wrapper_interface import pyWhatInterface




class Examples:
    def __init__(self, text_or_file_path: str) -> None:
        self.interface = pyWhatInterface(match_level=2)

    # Showing options template implemented
    def get_options(self) -> None:
        self.interface.get_filter()

    # Example of identifying an Ethereum Address        
    def example_eth_address(self, text_input: str) -> dict:
        results = self.interface.identify(text_input)
        return results

    # Example of changing default option level
    def example_change_default_option(self, match_level: int) -> None:
        self.interface.set_option(match_level)
        print(f"Changed option to level {match_level}.")
        print(f"Current option template: {self.interface.get_filter()}")

    # Example of creating a custom filter
    def example_custom_filter(self, rarity: float, include: list, exclude: list) -> None:
        self.interface.create_filter(rarity, include, exclude)
        print("Created custom filter with the following parameters:")
        print(f"Rarity: {rarity}, Include: {include}, Exclude: {exclude}")

    # Get available pyWhat tags
    def example_get_tags(self) -> None:
        self.interface.get_tags()

    def example_return_json(self):
        self.interface.print_json()

    # Saves results into json file
    def save_results_session(self, results: dict) -> None:
        """Save the results to previous results history.
        :param results: Results to save
        :type results: dict
        """
        self.interface.save_history(results)


def main():
    # Initialize your example class
    Example_Pipeline = Examples("0x4838B106FCe9647Bdf1E7877BF73cE8B0BAD5f97")

    # Example: Get Default Options Template
    Example_Pipeline.get_options()

    # Example: Change Alternative Default Option Level
    Example_Pipeline.example_change_default_option(match_level=1)
    
    # Example: Identify an Ethereum Address
    eth_results = Example_Pipeline.example_eth_address("0x4838B106FCe9647Bdf1E7877BF73cE8B0BAD5f97")
    print("Ethereum Address Results:", eth_results)

    # Example: Return Json Output
    Example_Pipeline.example_return_json()

    # Example: Create a Custom Filter
    Example_Pipeline.example_custom_filter(rarity=0.55, include=["Ethereum Address"], exclude=[])

    # Example: Get Tags
    Example_Pipeline.example_get_tags()

    # Save Results Session
    Example_Pipeline.save_results_session(eth_results)


if __name__ == "__main__":
    main()
