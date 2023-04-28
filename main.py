# (4) Компоненты связности (найти количество компонент связности графа,
# вывести компоненты списком вершин согласно нумерации в матрице смежности)

# - Использовать стандартный вход/выход (stdin/stdout), либо через файлики - done
# - Не использовать специфичные для вашей OS библиотеки - done
# - Подавать граф на вход матрицей смежности/матрицей весов (целиком, даже если она симметричная) - done
# - Рассматривать обыкновенные графы (неориентированные, без петель и кратных ребер), связные и несвязные - done
# - Примеры, на которых тестировали - done

# test 1
# nodes number 7, components 2
# 0 1 0 1 1 0 0
# 1 0 0 0 1 0 0
# 0 0 0 1 0 0 0
# 1 0 1 0 1 0 0
# 1 1 0 1 0 0 0
# 0 0 0 0 0 0 1
# 0 0 0 0 0 1 0

# test 2
# nodes number 7, components 3
# 0 1 0 1 1 0 0
# 1 0 0 0 1 0 0
# 0 0 0 1 0 0 0
# 1 0 1 0 1 0 0
# 1 1 0 1 0 0 0
# 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0

# test 3
# nodes number 4, components 1
# 0 1 1 0
# 1 0 0 1
# 1 0 0 1
# 0 1 1 0
# [[0, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1], [0, 1, 1, 0]]

# test 4
# nodes number 6, components 3
# 0 0 1 0 0 1
# 0 0 0 1 0 1
# 1 0 0 0 0 0
# 0 1 0 0 0 0
# 0 0 0 0 0 0
# 1 0 1 0 0 0


# nodes numeration starting from zero, due numeration in the adjacency matrix
class Graph(object):

    def __init__(self, mat, nodes_number):
        self.nodes_number = nodes_number
        self.mat = mat
        self.n_components = 0
        self.visited = [False] * (nodes_number + 1)

    def print_list(self, n_list):
        for i in n_list:
            if i:
                print(sorted(i))

    def BFS_find_comp(self):
        nodes_list = [[] for i in range(self.nodes_number)]

        if self.nodes_number < 1:
            return "Impossible to count components of null-graph"

        if self.nodes_number == 1:
            self.n_components = 1
            return nodes_list[self.n_components-1].append(0)

        for i in range(self.nodes_number):
            if self.visited[i]:
                continue

            self.n_components += 1
            nodes_list[self.n_components-1].append(i)
            self.visited[i] = True
            queue = [i]
            while queue:
                ver = queue.pop()
                for nod, to in enumerate(self.mat[ver]):
                    if not self.visited[nod] and to != 0:
                        self.visited[nod] = True
                        nodes_list[self.n_components-1].append(nod)
                        queue.append(nod)
        return self.print_list(nodes_list)


# nodes = 7
# matrix = [[0, 1, 0, 1, 1, 0, 0], [1, 0, 0, 0, 1, 0, 0], [0, 0, 0, 1, 0, 0, 0],
#          [1, 0, 1, 0, 1, 0, 0], [1, 1, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]

# nodes = 6
# matrix = [[0, 0, 1, 0, 0, 1], [0, 0, 0, 1, 0, 0], [1, 0, 0, 0, 0, 0],
#          [0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 0, 0, 0]]

print("Enter nodes number and then one by one enter the whole adjacency matrix")
nodes = int(input())

matrix = []
for _ in range(nodes):
    row = []
    for _ in range(nodes):
        row.append(int(input()))
    matrix.append(row)

graph = Graph(matrix, nodes)
graph.BFS_find_comp()
print(graph.n_components)