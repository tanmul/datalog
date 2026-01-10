from dataclasses import dataclass

@dataclass(slots=True)
class Table:
    name : str
    column : set
    description : str = ''
    load_sql : str
    direct_descendents : str