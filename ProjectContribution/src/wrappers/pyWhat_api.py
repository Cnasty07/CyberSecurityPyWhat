# -- PyWhat API Class --
#   INFO: API class for pyWhat interactions
#     --  Using this one to create a more complex version of the API Wrapper.

import os
from typing import Any, Dict, List, Optional, Union

from pywhat import Filter , Distribution , Identifier , Keys

from src.options.defaultFilters import StandardOption , LooseOption , StrictOption


# PyWhat API For new interactions
class  PyWhatAPI:

    @staticmethod
    def create_distribution(filter: Filter) -> Distribution:
        """Create a pyWhat Distribution.
        :param self: Description
        :param filter: Filter to be used in the distribution
        :type filter: Filter
        :return: A pyWhat Distribution object
        :rtype: Distribution
        """
        distribution = Distribution(filter)
        return distribution

    @staticmethod
    def create_filter(rarity: Optional[str] = None, include: Optional[List[str]] = None, exclude: Optional[List[str]] = None) -> Filter:
        """Create a pyWhat Filter.
        :param self: Description
        :param rarity: Unlikelyhood of False-Positive Matches (default: 0.1)
        :type rarity: Optional[str]
        :param include: List of items to include (if None will use default pywhat options)
        :type include: Optional[List[str]]
        :param exclude: List of items to exclude (if None will use default pywhat options)
        :type exclude: Optional[List[str]]
        :return: A pyWhat Filter object
        :rtype: Filter
        """
        py_filter = Filter({MinrRarity=rarity, Include=include, Exclude=exclude)
        return py_filter
        
    @staticmethod
    def print_format(format) -> None:
        """Print the results in a formatted way.
        :param self: Description
        :param printer: Printer instance
        :type printer: pywhat.printer.Printer
        """
        print(format)

    @staticmethod
    def identify(text_input: str, distribution: Distribution) -> Dict:
        """Basic run function to identify text input.
        :param self: Description
        :param text_input: Text input to identify
        :type text_input: str
        :return: Identification results
        :rtype: Dict
        """
        identifier = Identifier(distribution=distribution)
        results = identifier.identify(text_input=text_input)
        return results


def main():
    api = PyWhatAPI()
    print(api)
    # api = PyWhatAPI(filters={}, sorting={}, exporting={}, formatting={})
    # api.new_query()

if __name__ == "__main__":
    main()
