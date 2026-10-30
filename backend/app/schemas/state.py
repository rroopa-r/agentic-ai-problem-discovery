from typing import Annotated, List, TypedDict, Optional
from operator import add

class DiscoveryState(TypedDict):
    # 'Annotated' with 'add' allows multiple agents to append to the list
    raw_input: str
    discovered_problems: Annotated[List[str], add]
    critiques: Annotated[List[str], add]
    refined_statement: Optional[str]