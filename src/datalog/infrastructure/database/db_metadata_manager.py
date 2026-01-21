from sqlalchemy.engine.base import Engine
from sqlalchemy import inspect
from typing import Dict, List
from collections import namedtuple

SQLAlchemyTableMeta = namedtuple("SQLAlchemyTableMeta", ["name", "schema", "columns"])

class DatabaseMetadataManager():

    def __init__(self, engine : Engine):
        self._engine = engine

    def retrieve_table_metadata(self) -> List[SQLAlchemyTableMeta]:
        res = []

        insp = inspect(self._engine)
        for schema in insp.get_schema_names():
            for table in insp.get_table_names(schema=schema):
                res.append(SQLAlchemyTableMeta(name=table, schema=schema, columns=insp.get_columns(table, schema=schema)))
        
        return res
        
        
            