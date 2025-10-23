import pywhat.what as pw
from typing import Optional, Any

class WhatBase:
    def __init__(self, query: Optional[str] = None, filters: Optional[list[str]] = None) -> None:
        self.query = query
        self.filters = filters


    def set_filters(self, rarity: Optional[str] = "common") -> Any:
        set_filter = pw.create_filter(rarity=rarity, include=self.filters, exclude=[])
        return set_filter

    def help(self):
        pass
    
    def identifier(self):
        pass
    
    def run(self, command: str) -> None:
        return pw.main([command], filters=self.set_filters())


def main():
    what = WhatBase()
    what.run("0x3c3296fc4eaaf006a94063e8857a1459ae11b006f737bcae223c1e3bf70b9dda")


if __name__ == "__main__":
    main()