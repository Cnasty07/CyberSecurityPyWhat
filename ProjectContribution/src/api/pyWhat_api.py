import os
from typing import Dict, List, Optional, Union

from pywhat import what
from pywhat.printer import Printing
from pywhat import Filter , Distribution , Identifier 
from pywhat.what import main, What_Object , create_filter

# PyWhat API
class  PyWhatAPI:
    """PyWhatAPI class for calls to pyWhat.

    :param filters: Filters for the query.
    :param sorting: Sorting options for the query.
    :param exporting: Exporting options for the query.
    :param formatting: Formatting options for the query.
    :type filters: dict
    :type sorting: dict
    :type exporting: dict
    :type formatting: dict
    :return: PyWhatAPI instance
    """
    _filters = {
        "rarity": "",
        "include_tags": [],
        "exclude_tags": []
    }
    
    def __init__(self, filters: Dict, sorting: Dict, exporting: Dict, formatting: Dict) -> None:
        self.filters = filters
        self.sorting = sorting
        self.exporting = exporting
        self.formatting = formatting
        self.pwhat = what

    def new_query(self) -> Union[None, List, Dict]:
        """Start a new query into a resource.
        :param self: Description
        """
        text_input = '0x396343362be2A4dA1cE0C1C210945346fb82Aa49'
        self.pwhat.main(text_input = text_input)

    def print_format(self, format_option) -> None:
        """Print the results in a formatted way.
        :param self: Description
        :param printer: Printer instance
        :type printer: pywhat.printer.Printer
        """
        pass


def main():
    api = PyWhatAPI(filters={}, sorting={}, exporting={}, formatting={})
    api.new_query()

if __name__ == "__main__":
    main()
