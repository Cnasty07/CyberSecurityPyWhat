import os
from dataclasses import dataclass

@dataclass
class Standard:
    rarity: float = 0.1
    key: None = None
    reverse: bool = False
    format: str = "json"
    format_str: str = "pretty"
    # boundaryless: bool = True
    

    
def main():
    pass

if __name__ == "__main__":
    main()
