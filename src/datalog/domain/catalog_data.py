from ..models.table import Table, TableId

from typing import Dict

class CatalogData(object):
    """
    Handles all concrete 
    """

    def __init__(self, table_map : Dict[TableId, Table]):
        self.table_map : Dict[TableId, Table] = table_map