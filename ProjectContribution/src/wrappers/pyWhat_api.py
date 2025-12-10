# -- PyWhat API Class --
#   INFO: API class for pyWhat interactions
#     --  Using this one to create a more complex version of the API Wrapper.

import os
from typing import Any, Dict, List, Optional, Union

from pywhat import Filter , Distribution , Identifier , Keys , pywhat_tags, printer
import pywhat

from src.options.defaultFilters import StandardOption , LooseOption , StrictOption


# PyWhat API For new interactions
class  PyWhatAPI:
    Filter: pywhat.Filter
    Distribution: pywhat.Distribution
    
    """API class for pyWhat interactions.
    """
    @staticmethod
    def create_distribution(filter: pywhat.Filter):
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
    def create_filter(rarity: Optional[float] = None, include: Optional[List[str]] = None, exclude: Optional[List[str]] = None) -> pywhat.Filter:
        """Create a pyWhat Filter.
        :param self: Description
        :param rarity: Unlikelyhood of False-Positive Matches (default: 0.1)
        :type rarity: Optional[float]
        :param include: List of items to include (if None will use default pywhat options)
        :type include: Optional[List[str]]
        :param exclude: List of items to exclude (if None will use default pywhat options)
        :type exclude: Optional[List[str]]
        :return: A pyWhat Filter object
        :rtype: Filter
        """
        tags = pywhat.pywhat_tags
        if include is None:
            include = tags
        if exclude is None:
            exclude = []
        py_filter = Filter({"Tags": tags, "ExcludeTags": exclude, "MinRarity": rarity})
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
    def identify(text_input: str, options: StandardOption | LooseOption | StrictOption ,distribution: Optional[pywhat.Distribution] = None) -> Dict:
        """Basic run function to identify text input.
        :param self: Description
        :param text_input: Text input to identify
        :type text_input: str
        :return: Identification results
        :rtype: Dict
        """
        if distribution is None:
            distribution = Distribution(Filter({}))
        if distribution["MinRarity"] > 0.14:
            boundaryless = Filter({"MinRarity": 0.0, "Tags": [], "ExcludeTags": []})
        else:
            boundaryless = None
        print("Identify distribution:", distribution)
        identifier = Identifier(dist=distribution, boundaryless=boundaryless)
        results = identifier.identify(text=text_input, reverse=options.reverse, include_filenames=options.include_filenames)
        return results

    @staticmethod
    def get_tags() -> None:
        """Get available pyWhat tags.
        :param self: Description
        """
        print(pywhat_tags)

    @staticmethod
    def print_json(results: Dict) -> None:
        """Print the results in JSON format.
        :param self: Description
        :param results: Results to print
        :type results: Dict
        """
        print_result = printer.Printing()
        print_result.print_json(results)

def main():
    api = PyWhatAPI()
    print(api)
    
if __name__ == "__main__":
    main()
