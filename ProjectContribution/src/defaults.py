
# INFO: Unsure if deleting this or changing it yet. 

# -- Options defaults for API wrapper --
# Setting default options for api wrapper rather than 

import os

class DefaultOptions:

        #     self,
        # text: str,
        # only_text: bool,
        # key,
        # reverse: bool,
        # boundaryless: Filter,
        # include_filenames: bool,


    @staticmethod
    def normal():
        filters: dict = {
            "rarity": 0.1
        }
        sorting: dict = {
            "key": None,
            "reverse": False
        }
        exporting: dict = {
            "format": "json",
        }
        formatting: dict = {
            "format_str": "pretty"
        }
        boundaryless: bool = True
        return filters, sorting, exporting, formatting, boundaryless

    @staticmethod
    def loose():
        # set rarity to low and include common tags
        pass

    @staticmethod
    def strict():
        # set rarity to high and exclude common tags
        pass


def main():
    testing_normal = DefaultOptions.normal()
    print(testing_normal)

if __name__ == "__main__":
    main()
