# -- pyWhat Wrapper Class --
#      -- Wrapper around pyWhat functionality for easier integration
#      -- This one models the what.py structure strictly

import os
from typing import Optional

# pyWhat Imports for Wrapper
from pywhat.what import What_Object
from pywhat.what import create_filter
from pywhat import Distribution, Filter , pywhat_tags , Keys
from pywhat.printer import Printing

# Importing Filters and Options
from src.options.defaultFilters import StandardOption, LooseOption, StrictOption

class pyWhatWrapper(What_Object):
    def __init__(self, distribution: Optional[Distribution] = None, option_template: Optional[int] = None):
        if option_template == 1 or option_template is None:
            self.option_template = StandardOption()
        if option_template == 2:
            self.option_template = LooseOption()
        if option_template == 3:
            self.option_template = StrictOption()
        self.filter = self.create_py_filter(rarity=str(f"{self.option_template.rarity}:1"))
        
        if distribution is None:
            distribution = Distribution(self.filter)
        self.distribution = distribution
        super().__init__(distribution)

        self.previous_results = []

    def create_py_filter(self, rarity: Optional[str] = None, include: Optional[list[str]] = None, exclude: Optional[list[str]] = None) -> Filter:
        """Wrapper for creating a pyWhat Filter.
        
        :param rarity: Unlikelyhood of False-Positive Matches (default: 0.1)
        :type rarity: Optional[str]
        :param include: List of items to include (if None will use default pywhat options)
        :type include: Optional[list[str]]
        :param exclude: List of items to exclude (if None will use default pywhat options)
        :type exclude: Optional[list[str]]
        :return: A pyWhat Filter object
        :rtype: Filter
        """
        py_filter: Filter
        try:
            py_filter = create_filter(rarity, include, exclude)
        except Exception as e:
            print(f"Error creating filter: {e}")
            py_filter = create_filter(None, None, None)
        return py_filter

    def identify(self, text_input: str) -> dict:
        """Identify the given item using pyWhat.
        
        :param text_input: Item to be identified
        :type text_input: str
        """
        print(f"Using options: {self.option_template}")

        result = self.what_is_this(
            text_input,
            only_text = False,
            key = self.option_template.key,
            reverse = self.option_template.reverse,
            boundaryless = None,
            include_filenames = self.option_template.include_filenames,
        )
        self.previous_results.append(result)
        # change to json format
        return result

    def get_tags(self):
        print(pywhat_tags)

    def json_results(self, text_input: str):
        """Get identification results for the given input.
        
        :param text_input: Item to be identified (Could be a file path or text)
        :type text_input: str
        :return: Identification results
        :rtype: json/dict
        """
        results = self.identify(text_input)
        return Printing().print_json(results)



def main():
    wrapper = pyWhatWrapper(distribution=None, option_template=None)
    text_input = '0x4838B106FCe9647Bdf1E7877BF73cE8B0BAD5f97'
    results = wrapper.json_results(text_input=text_input)
    print(results)
    # add file input later
    # results = wrapper.identify(text_input)
    # print(results)
    # print(wrapper.get_tags())

if __name__ == "__main__":
    main()
