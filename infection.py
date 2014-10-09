# graph: a hash table where keys represent a vertex and values will be
# an adjacency list
# user: a vertex contained in graph
def total_infection(users, graph, v_user, visited=None):
    if visited == None:
        visited = [False for x in users]
    if not visited[v_user]:
        print("Visited vertex {}".format(v_user))
        visited[v_user] = True
        users[v_user].update(1)
        for v_u in graph[v_user]:
            total_infection(users, graph, v_u, visited)


def limited_infection():
    pass

class User():
    """Defines a simple user object with a version property that defines
    which site version they're using"""
    def __init__(self, ver):
        self.version = ver
    def update(self, ver):
        self.version = ver
