import networkx as nx

class DependencyGraph:

    def __init__(self, table_map):
        self._table_map = table_map

        self._graph = nx.DiGraph()

    def generate(self):
        for table_id, table in self._table_map.items():
            print(table_id, table.direct_ancestors)
            self._graph.add_node(table_id)
            self._graph.add_edges_from([(ancestor, table_id) for ancestor in table.direct_ancestors])
        
    def get_downstream(self, table_id):
        return set(n for n in nx.traversal.bfs_successors(self._graph, source=table_id) if n != table_id)

    def get_upstream(self, table_id):
        return set(n for n in nx.traversal.bfs_predecessors(self._graph, source=table_id) if n != table_id)

    def get_root_tables(self):
        return set(n for n, d in self._graph.in_degree if d == 0)
    
    def get_leaf_tables(self):
        return set(n for n, d in self._graph.out_degree if d == 0)