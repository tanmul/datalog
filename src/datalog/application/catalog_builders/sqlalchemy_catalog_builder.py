from ...domain.models.table import Table
from ...domain.catalog_data import CatalogData
from ...infrastructure.database.db_metadata_manager import DatabaseMetadataManager

from sqlalchemy.engine.base import Engine

class SqlAlchemyCatalogBuilder():

    def __init__(self, engine : Engine):
        self._engine : Engine = engine
    
    def build(self) -> CatalogData:
        db_mtd_mgr = DatabaseMetadataManager(self._engine)
        table_meta_list = db_mtd_mgr.retrieve_table_metadata()

        # Now we create the correct map for CatalogData
        table_map = {}
        for table_meta in table_meta_list:
            table = Table(name=table_meta.name, schema=table_meta.schema, columns=table_meta.columns)
            table_map[table.id] = table

        return table_map