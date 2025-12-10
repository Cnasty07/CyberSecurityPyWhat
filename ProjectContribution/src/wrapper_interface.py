import os
from typing import Optional


from src.wrappers import what_wrapper, pyWhat_api
from .options import StandardOption , LooseOption , StrictOption


class pyWhatInterface:
    """Interface for Wrapper classes.
    """
    def __init__(self, match_level: Optional[int] = None, include: Optional[list] = None, exclude: Optional[list] = None) -> None:
        # connections to our two api layers
        self.what_main = what_wrapper.pyWhatWrapper()
        self.wrapper = pyWhat_api.PyWhatAPI()
        
        # Setting Filter Level
        self.match_level = match_level
        if  self.match_level == 1:
            self.match_level = 1  # Default match level
            self.option_template =  LooseOption()
        elif self.match_level == 2:
            self.option_template =  StandardOption()
        elif self.match_level == 3:
            self.option_template =  StrictOption()
        else:
            self.option_template =  StandardOption()

        # Adding previous results history
        self.previous_results = []
        
        # Setting Include and Exclude Lists if provided
        self.include = include
        self.exclude = exclude

        self.filter = self.wrapper.create_filter(rarity=str(f"{self.option_template.rarity}:1"), include=self.include, exclude=self.exclude)
        self.distribution = what_wrapper.Distribution(self.filter)

        
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

    def create_filter(self, rarity: Optional[str] = None, include: Optional[list] = None, exclude: Optional[list] = None):
        self.wrapper.create_filter(rarity, include, exclude)

    def get_tags(self) -> None:
        self.what_main.get_tags()

    # identifies the input data
    def identify(self, text_or_path_input: str) -> dict:
        """Identify input data using the wrapper.
        :param input_data: Input data to identify
        :type input_data: str
        :return: Identification results
        :rtype: dict
        """
        result = self.wrapper.identify(text_or_path_input, distribution= self.distribution)
        self.previous_results.append(result)
        return result

    def configure(self, options: dict) -> None:
        """Configure the wrapper with given options.
        :param options: Configuration options
        :type options: dict
        """
        raise NotImplementedError("Subclasses must implement this method.")

def main():
    pass

if __name__ == "__main__":
    main()
