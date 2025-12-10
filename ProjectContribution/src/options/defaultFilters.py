# -- defaultFilters.py --
# INFO: This module defines default filter options for pyWhat identifications.
#       It includes Standard, Loose, and Strict options with different rarity settings.

import os
from dataclasses import dataclass, Field
from typing import Any, Optional 
from enum import auto, Enum

from pywhat import Filter , Keys


@dataclass(frozen=False)
class BaseOptions:
    """Base Options Class for pyWhat Identifications
    """
    rarity: float = 0.1 # Default rarity value
    key: Enum | Any = Keys.RARITY # sorts by rarity with most likely match first
    reverse: bool = False # reverse sorting output
    format: str = "json" # output format default is json
    boundaryless: Optional[Filter] = None # enable boundaryless matching (disabled by default in API)
    include_filenames: bool = True # include filenames in identification
    

@dataclass
class StandardOption(BaseOptions):
    """Standard Level For Balanced Matching
    """
    rarity: float = 0.15

@dataclass
class LooseOption(BaseOptions):
    """Loose Level For Broad Matching"""
    rarity: float = 0.05 # Lower rarity value to include more results

@dataclass
class StrictOption(BaseOptions):
    """Strict Level For Rigourous Matching
    """
    rarity: float = 0.4 # Higher rarity value to narrow results


def main():
    test_std = StandardOption()
    test_loose = LooseOption()
    test_strict = StrictOption()
    
    print(f"{test_std}\n{test_loose}\n{test_strict}")


if __name__ == "__main__":
    main()
