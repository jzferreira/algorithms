from collections import defaultdict
import json
import argparse
import queue

class Graph:
    def __init__(self, G, E, direct=False):
        self.direct = direct
        if (isinstance(G, list)):
            self.vertices = set(G)
        else:
            self.vertices = G
        if (isinstance(E, list)):
            self.srcEdges = [tuple(x) for x in E]
        else:
            self.srcEdges = E
        self._graph = self._set_vertices_edges()

    def _isDirect(self):
        return self.direct

    def _set_vertices_edges(self):
        edges = self.srcEdges
        g = defaultdict(list)
        for u, v in edges:
            if not self._isDirect():
                g[u].append(v)
                g[v].append(u)
        return g

    def get_neighborhood(self, vertice):
        if vertice in self.vertices:
            return self._graph[vertice]
        raise ('Vertice nao encontrado')

    def get_vertices(self):
        return self.vertices

    def print_vertices(self):
        print(self.vertices)

    def print_vertices_edges(self):
        g = self._graph
        for u in g:
            print(f'{u} => {g[u]}')

    def print_result(self, dist, previous):
        vertices = dist.keys()
        print(f'Vertex ----------- Distance from Source ----------- PREVIOUS')
        for v in vertices:
            print(f'  {v}\t\t\t\t{dist[v]}\t\t\t{previous[v]}')


def import_json(config):
    with open(config, 'r') as fs:
        return json.loads(fs.read())


def bfs(output, start, **test):
    graph = Graph(**test)
    visited = {}
    dist = {}
    prev = {}
    for vertice in graph.get_vertices():
        visited[vertice] = False
        dist[vertice] = float('INF')
        prev[vertice] = None
    
    #Configuracao Vertice de START
    visited[start] = True
    dist[start] = 0
    Q = queue.Queue()
    Q.put(start)
    while Q.empty() == False:
        u = Q.get()
        for v in graph.get_neighborhood(u):
            if visited[v] == False:
                visited[v] = True
                dist[v] = dist[u] + 1
                prev[v] = u
                Q.put(v)
    graph.print_result(dist, prev)


def tests(config, output, start):
    tests = import_json(config)
    for i in tests.keys():
        elem = tests[i]
        bfs(output, start, **elem)


def test(config, output, start):
    test = import_json(config)
    bfs(output, start, **test)


if __name__ == "__main__":
    """
        Algoritmo de busca em largura
    """
    # Add Arguments
    parser = argparse.ArgumentParser(description='BFS')
    parser.add_argument('--config',
                        type=str,
                        required=False,
                        default='graph.json',
                        help='Arquivo de configuracao do Grafo, mais no README.MD')
    parser.add_argument('--start', type=str, required=True, help='No inicial')
    parser.add_argument('--output', required=False, default='', type=str,
                        help='Imprimir a tabela com Vertices, Valores e Antecessor')
    args = parser.parse_args()
    config = args.config
    output = args.output
    start = args.start
    if (config == 'graph.json'):
        test(config, output, start)
    else:
        tests(config, output, start)
