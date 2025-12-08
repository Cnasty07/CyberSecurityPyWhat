# INFO: First draft but probably wont use so forget this when i delete it later.

# -- pyWhat Wrapper Object Module -- 
#   INFO: Wrapper module for pyWhat to simplify calls to its modules.
#       AUTHOR: Chris Nastasi, Andrew Gonzalez, Henry Francis
#       VERSION: 1.0.0
#       Milestone 3: Wrapper Object for pyWhat, Add Default Options, Implement different output options for pipeline.


# Importing Standard Libraries
from typing import Optional, Any

# Importing pyWhat Modules
from pywhat.printer import Printing as pw_printer
from pywhat.filter import Filter as pw_filter
from pywhat.identifier import Identifier as pw_identifier
import pywhat.what as pw


class WhatBase:
    """Base class for the pyWhat wrapper object.
    """
    def __init__(self, query: Optional[str] = None, filters: Optional[list[str]] = None) -> None:
        """Initialize the WhatBase class.
        
        :param self: Description
        :param query: Description
        :type query: Optional[str]
        :param filters: Description
        :type filters: Optional[list[str]]
        """
        self.query = query
        self.filters = filters

    # Milestone 3 default options settings
    def set_defaults(self) -> None:
        """Function to set default options for pyWhat.
            Options Include:
                - Rarity: common
        
        :param self: Description
        """
        pass

    def set_filters(self, rarity: Optional[str] = "common") -> Any:
        """Function to set filters for pyWhat.
        
        :param self: Description
        :param rarity: Description
        :type rarity: Optional[str]
        :return: Description
        :rtype: Any
        """
        set_filter = pw.create_filter(rarity=rarity, include=self.filters, exclude=[])
        return set_filter

    # Wrapper functions for pyWhat modules
    def help(self):
        """Function to display help information for pyWhat.
        
        :param self: Description
        """
        pass
    
    def identifier(self):
        """Function to identify the type of the query.
        
        :param self: Description
        """
        pass

    def printer(self):
        """Function to print the results of the query.
        
        :param self: Description
        """
        pass
    
    def run(self, command: str) -> None:
        return pw.main([command], filters=self.set_filters())


def main():
    what = WhatBase()
    what.set_defaults()
    what.run("0x3c3296fc4eaaf006a94063e8857a1459ae11b006f737bcae223c1e3bf70b9dda")


if __name__ == "__main__":
    main()