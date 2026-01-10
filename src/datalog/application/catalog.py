from typing import Dict, List
from models import Table

class Catalog(object):
    """"""

    def __init__(self):
        self._table_list = List[Table]

    def save(self):
        pass
    
    @classmethod
    def build_from_dict(cls, table_metadata_mapping : Dict):
        pass