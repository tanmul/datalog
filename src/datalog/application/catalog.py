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

        # Indexes
        self._name_index = dict()
        self._column_index = dict()
    
    @cached_property
    def _dep_graph(self) -> DependencyGraph:
        return DependencyGraph(table_map=self._tables)

    def _invalidate_dep_graph(self):
        """Invalidates the cached dependency graph property. Forcing another lazy instantiation"""
        self.__dict__.pop('_dep_graph', None)

    def index(self):
        """Clears and indexes all identifying filters for quicker searches"""
        # We clear the indexes
        self._name_index = dict()
        self._column_index = dict()

        # Now we repopulate them
        for table_id, table in self._tables.items():
            # Setting name index
            self._name_index[table.name.lower()] = self._name_index.get(table.name.lower(), []).append(table_id)

            # Setting column index
            for column in table.columns:
                self._column_index[column.lower()] = self._column_index.get(column, []).append(table_id)
    
    # Mutation methods
    def add_table(self):
        pass

    def remove_table(self):
        pass

    def update_table_metadata(self):
        pass

    def save(self):
        pass
    
    # Search methods
    def search(self, term : str, filter : Optional[List[str]] = None):
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
            self.index()

            if not isinstance(filter, (str, list)):
                raise TypeError("Filter must be a string or a list of strings")
            
            if isinstance(filter, str):
                filter = [filter]

            if not all(field not in ['name', 'column'] for field in filter):
                raise ValueError("Currently supported filters are 'name' and 'column'")
            
            res = []
            if 'name' in filter:
                res.extend(self._name_index.get(term))
            if 'column' in filter:
                res.extend(self._column_index.get(term))
                

        return results
    
    def get_table(self, id : TableId):
        return self._tables[id]

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
        return self._dep_graph.get_upstream(Catalog._standardize_table_id_input(table))
    
    def get_downstream(self, table : Union[str, TableId, Table]):
        return self._dep_graph.get_downstream(Catalog._standardize_table_id_input(table))

    # Builder factories
    @classmethod
    def build_from_dict(cls, table_metadata_mapping : Dict):
        for table, metadata in table_metadata_mapping:
            pass
    
    @classmethod
    def build_from_sqlalchemy(cls, engine):
        pass

    @classmethod
    def build_from_sql(cls):
        pass