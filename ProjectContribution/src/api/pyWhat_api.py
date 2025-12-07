import os
from typing import Dict, List, Optional, Union

from pywhat import printer, what, helper, identifier


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
        pass

    def print_format(self, format_option) -> None:
        """Print the results in a formatted way.
        :param self: Description
        :param printer: Printer instance
        :type printer: pywhat.printer.Printer
        """
        pass

def main():
    pass

if __name__ == "__main__":
    main()
