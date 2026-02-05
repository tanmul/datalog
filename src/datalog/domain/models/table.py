from dataclasses import dataclass, field
from functools import cached_property
from typing import Iterable, Optional

TABLE_ID_FIELDS = frozenset(['name', 'columns', 'description'])

@dataclass(slots=True, frozen=True)
class TableId:
    """Identifier class to be used for uniquely identifying tables"""
    # Subject to change, hopefully make it frozen one day
    name : str
    schema : str

    @classmethod
    def from_string(cls, table_str : str, default_schema : str = None):
        assert type(table_str) == 'str', "from_string argument must be a str"

        # TODO: Use a parser here?
        split_table_str = table_str.rsplit('.', maxsplit=1)
        if len(split_table_str) <= 1:
            assert default_schema, "Non-prefixed table names must be provided a default schema"
            return TableId(split_table_str[0], default_schema)
        return TableId(split_table_str[1], split_table_str[0])

@dataclass(slots=True)
class Table:
    """A table entity representing relevant metadata of a database Table"""
    # Instance variables (What defines a table object?)
    name : str
    schema : str
    columns : set
    description : Optional[str] = None
    load_sql : Optional[str] = None
    direct_ancestors : Optional[set[TableId]] = None

    # Creating an id that uniquely identifies a Table
    id : TableId = field(init=False)

    # A string representation used for universal searching
    _search_expr : Optional[str] = None

    def __post_init__(self):
        self.id : TableId = TableId(name=self.name, schema=self.schema)

    @property
    def search_expr(self):
        if not self._search_expr:
            self._search_expr = ' '.join([f"{field}:{getattr(self, field)}" for field in TABLE_ID_FIELDS])
        return self._search_expr

    @classmethod
    def from_dict(cls, metadata : dict):
        pass