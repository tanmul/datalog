from dataclasses import dataclass

@dataclass(slots=True)
class Table:
    name : str
    column : set
    parents : set
    children : set
