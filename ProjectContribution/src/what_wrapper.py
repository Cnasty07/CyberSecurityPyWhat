# -- pyWhat Wrapper Class --
# Wrapper around pyWhat functionality for easier integration

import os
from typing import Optional

# pyWhat Imports for Wrapper
from pywhat.what import What_Object
from pywhat.what import create_filter
from pywhat import Distribution, Filter
from pywhat.printer import Printing

class pyWhatWrapper(What_Object):

    
    def __init__(self, distribution, option_template: Optional[dict] = None):
        self.option_template = option_template
        self.filter = self.create_py_filter()
        if distribution is None:
            distribution = Distribution(self.filter)
        self.distribution = distribution
        super().__init__(distribution)

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
        py_filter = create_filter(rarity, include, exclude)
        return py_filter

    def identify(self, text_input: str):
        """Identify the given item using pyWhat.
        
        :param text_input: Item to be identified
        :type text_input: str
        """
        return self.what_is_this(
            text_input,
            only_text=False,
            key=None,
            reverse=False,
            boundaryless=self.create_py_filter(),
            include_filenames=False,
        )

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
    # add file input later
    results = wrapper.identify(text_input)
    print(results)
    # Printing().pretty_print(results, text_input, print_tags=True)

if __name__ == "__main__":
    main()
