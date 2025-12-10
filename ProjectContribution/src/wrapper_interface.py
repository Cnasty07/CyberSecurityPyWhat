import os
from typing import Optional


from src.wrappers import what_wrapper, pyWhat_api
from .options import StandardOption , LooseOption , StrictOption 
from pywhat import Filter, Distribution

class pyWhatInterface:
    """Interface for Wrapper classes.
    """
    def __init__(self, match_level: Optional[int] = None, include: Optional[list] = None, exclude: Optional[list] = None) -> None:
        # connections to our two api layers
        self.what_main = what_wrapper.pyWhatWrapper()
        self.wrapper = pyWhat_api.PyWhatAPI()

        # Setting Filters
        self.filter: Filter
        self.distribution: Distribution
        
        # Adding previous results history
        self.previous_results: list = []
        
        # Setting Include and Exclude Lists if provided
        self.include: list = [] if include is None else include
        self.exclude: list = [] if exclude is None else exclude
        
        # Setting Filter Level
        self.match_level: int | None = match_level
        self.option_template: StandardOption | LooseOption | StrictOption
        if  self.match_level == 1:
            self.option_template =  LooseOption()
        elif self.match_level == 2:
            self.option_template =  StandardOption()
        elif self.match_level == 3:
            self.option_template =  StrictOption()
        else:
            self.option_template =  StandardOption()
        
        self.filter = self.wrapper.create_filter(rarity=self.option_template.rarity, include=self.include, exclude=self.exclude)
        self.distribution = self.wrapper.create_distribution((self.filter))

    def set_option(self, option_level: int) -> None:
        """Set the option level for the interface.
        :param option_level: Level of option to set (1: Loose, 2: Standard, 3: Strict)
        :type option_level: int
        """
        if option_level == 1:
            self.option_template = LooseOption()
        elif option_level == 2:
            self.option_template = StandardOption()
        elif option_level == 3:
            self.option_template = StrictOption()
        else:
            raise ValueError("Invalid option level. Choose 1 (Loose), 2 (Standard), or 3 (Strict).")
        
        # Update filter and distribution based on new option
        self.filter: Filter = self.wrapper.create_filter(rarity=self.option_template.rarity, include=self.include, exclude=self.exclude)
        self.distribution: Distribution = self.wrapper.create_distribution(self.filter)

            
    # Getters
    def get_previous_results(self) -> list:
        """Get the previous results from the last identification.
        :return: List of previous results
        :rtype: list
        """
        return self.previous_results

    def get_filter(self) -> StandardOption | LooseOption | StrictOption:
        """Get the option level based on match_level.
        :return: Option level instance
        :rtype: StandardOption | LooseOption | StrictOption
        """
        return self.option_template

    def create_filter(self, rarity: Optional[float] = None, include: Optional[list] = None, exclude: Optional[list] = None):
        self.wrapper.create_filter(rarity, include, exclude)
        self.filter = self.wrapper.create_filter(rarity, include, exclude)
        self.distribution = what_wrapper.Distribution(self.filter)

    def get_tags(self) -> None:
        """Get available pyWhat tags.
        """
        self.what_main.get_tags()

    # API Calls to Layers
    
    ## identifies the input data
    def identify(self, text_or_path_input: str) -> dict:
        """Identify input data using the wrapper.
        :param input_data: Input data to identify
        :type input_data: str
        :return: Identification results
        :rtype: dict
        """
        self.filter = self.wrapper.create_filter(rarity=self.option_template.rarity, include=self.include, exclude=self.exclude)
        self.distribution = self.wrapper.create_distribution(self.filter)
        # print("Wrapper distribution:", self.distribution)
        
        # result = self.wrapper.identify(text_or_path_input, distribution=Distribution(Filter({})), options=self.option_template)
        result = self.wrapper.identify(text_or_path_input, distribution=Distribution(self.filter), options=self.option_template)
        print(result)
        self.previous_results.append(result)
        return result

    def print_json(self) -> None:
        """Print the results in JSON format.
        :param format: Format to print
        """
        last = self.previous_results.pop()
        self.wrapper.print_json(last)
        print(last)

    def save_history(self, results: dict) -> None:
        """Save the results to previous results history.
        :param results: Results to save
        :type results: dict
        """
        with open("history_results.json", "a", encoding="utf-8") as file:
            file.write(str(results) + "\n")
            file.close()

def main():
    import sys
    print(sys.path)
    interface = pyWhatInterface(match_level=2)
    print(interface.option_template)

if __name__ == "__main__":
    main()
