from typing import Dict, List, Iterable, Optional
from ..models.table import Table, TableId
import re
from ..domain.dependency_graph import DependencyGraph
from functools import cached_property
from typing import Union

class Catalog(object):
    """
    """

    _instance = None

    def __init__(self, tables : Dict[TableId, Table]):
        self._tables : Dict[TableId, Table] = tables
    
    @cached_property
    def _dep_graph(self) -> DependencyGraph:
        return DependencyGraph(table_map=self._tables)

    def _invalidate_dep_graph(self):
        """Invalidates the cached dependency graph property. Forcing another lazy instantiation"""
        self.__dict__.pop('_dep_graph', None)

    def index(self) -> Dict[str, List[TableId]]:
        self._name_index = dict()
        self._column_index = dict()
        self._ancestor_index = dict()
        for table_id, table in self._tables.items():
            self._name_index[table.name] = self._name_index.get(table.name, []).append(table_id)
            self._name_index[table.name] = self._name_index.get(table.name, []).append(table_id)
            self._name_index[table.name] = self._name_index.get(table.name, []).append(table_id)
            self._name_index[table.name] = self._name_index.get(table.name, []).append(table_id)
        return index
    
    # Mutation methods
    def add_table(self):
        pass

    def remove_table(self):
        pass

    def update_table_metadata(self):
        pass

    def refresh(self):
        pass

    def save(self):
        pass
    
    # Search methods
    def search(self, term : str, filter : Optional[str] = None):
        """
        A universal search, that searches across all possible filters
        
        :param self: An instance of the Catalog class
        :param regex: Description
        :type regex: str
        """
        if not filter:
            pattern = re.compile(f'.*{term}.*')

            results = []
            for table in self._tables.values():
                if pattern.search(table.search_expr):
                    results.append(table)
        else:
            # Indexed Searches


        return results

    # Dependency Methods
    @staticmethod
    def _standardize_table_id_input(table_input : Union[str, TableId, Table]) -> TableId:
        if isinstance(table_input, TableId):
            return table_input
        elif isinstance(table_input, Table):
            return table_input.id
        elif isinstance(table_input, str):
            return TableId.from_string(table_input)
        
        raise TypeError("Unsupported argument! Must be one of str, TableId, Table")

    def get_upstream(self, table : Union[str, TableId, Table]):
        return self._dep_graph.get_upstream(Catalog._standardize_table_input(table))
    
    def get_downstream(self, table : Union[str, TableId, Table]):
        return self._dep_graph.get_downstream(Catalog._standardize_table_input(table))

    # @classmethod
    # def __new__(cls, *args, **kwargs):
    #     if not cls._instance:
    #         cls._instance = super().__new__(cls(*args, *kwargs))
    #     return cls._instance
    
    @classmethod
    def build_from_dict(cls, table_metadata_mapping : Dict):
        for table, metadata in table_metadata_mapping:
            pass